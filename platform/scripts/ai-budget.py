#!/usr/bin/env python3
"""Operate the AI budget ledger for a project (register, approve, import usage, report, review).

Trust model: the operator identity (--approver/--reviewer/--actor) is a label recorded in the
ledger. Authority comes from OS permissions on the protected state directory, not from this flag.
The CLI never reads credentials or raw content and makes no network calls.
"""

from pathlib import Path
import argparse
import csv
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ai_sdlc_platform.ai_budget import BudgetError, BudgetLedger
from ai_sdlc_platform.progress import DEFAULT_STATE_DIR


def flatten(value, prefix=""):
    """Flatten nested mappings/lists to dotted keys for CSV output."""
    items = {}
    if isinstance(value, dict):
        for key, child in value.items():
            items.update(flatten(child, f"{prefix}.{key}" if prefix else str(key)))
    elif isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            items.update(flatten(child, f"{prefix}.{index}"))
    else:
        items[prefix] = "" if value is None else value
    return items


def dump_json(value, out) -> None:
    json.dump(value, out, indent=2, sort_keys=True, default=str)
    out.write("\n")


def emit_report(report: dict, fmt: str, out) -> None:
    if fmt == "json":
        dump_json(report, out)
        return
    flat = flatten(report)
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(list(flat))
    writer.writerow([str(v) for v in flat.values()])


def _unique_keys(pairs):
    result = dict(pairs)
    if len(result) != len(pairs):
        raise ValueError("Duplicate JSON keys")
    return result


def read_json(path: str, what: str):
    try:
        text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        raise BudgetError("INVALID_USAGE_FILE", f"cannot read {what} file") from None
    try:
        return json.loads(text, object_pairs_hook=_unique_keys)
    except (ValueError, RecursionError):
        raise BudgetError("INVALID_USAGE_FILE", f"{what} file is not valid JSON") from None


def load_records(path: str) -> list:
    records = read_json(path, "usage")
    if not isinstance(records, list) or not all(isinstance(r, dict) for r in records):
        raise BudgetError("INVALID_USAGE_FILE", "usage file must be a JSON array of objects")
    return records


def load_usage(path: str) -> dict:
    usage = read_json(path, "usage")
    if not isinstance(usage, dict):
        raise BudgetError("INVALID_USAGE_FILE", "usage file must be a JSON object")
    return usage


def build_parser():
    parser = argparse.ArgumentParser(description="AI budget ledger")
    parser.add_argument("--project", type=Path, default=Path.cwd(), help="Project directory (default: cwd)")
    parser.add_argument("--state-dir", type=Path, default=DEFAULT_STATE_DIR,
                        help=f"Protected governance state directory (default: {DEFAULT_STATE_DIR})")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("register", help="Register a work item")
    p.add_argument("item_id")
    p.add_argument("--parent")

    p = sub.add_parser("approve", help="Approve a USD limit for a work item")
    p.add_argument("item_id")
    p.add_argument("--usd", required=True, help="Decimal USD limit, e.g. 25.00")
    p.add_argument("--approver", required=True)
    p.add_argument("--reason", required=True)

    p = sub.add_parser("import-usage", help="Import usage records from a JSON array file ('-' for stdin)")
    p.add_argument("file")

    p = sub.add_parser("settle", help="Settle a reservation with a usage JSON object ('-' for stdin)")
    p.add_argument("reservation_id")
    p.add_argument("--usage", required=True, help="JSON object file; identity fields come from the reservation")

    p = sub.add_parser("report", help="Report budget status for a work item")
    p.add_argument("item_id")
    p.add_argument("--format", choices=("json", "csv"), default="json")

    p = sub.add_parser("review", help="Record a budget review")
    p.add_argument("item_id")
    p.add_argument("--reviewer", required=True)
    p.add_argument("--completed", required=True)
    p.add_argument("--remaining", required=True)
    p.add_argument("--reason", required=True)
    p.add_argument("--projected-usd", required=True)

    p = sub.add_parser("hold", help="Hold a work item for budget review")
    p.add_argument("item_id")
    p.add_argument("--reason", required=True)
    p.add_argument("--actor", required=True)

    p = sub.add_parser("pending", help="List pending reservations for a work item")
    p.add_argument("item_id")

    p = sub.add_parser("usage", help="Show active usage with repo, task and model attribution")
    p.add_argument("item_id")

    p = sub.add_parser("history", help="Show audit events for a work item")
    p.add_argument("item_id")
    return parser


def run(args, out) -> None:
    ledger = BudgetLedger(args.project.expanduser(), args.state_dir.expanduser())
    cmd = args.command
    if cmd == "register":
        ledger.register_item(args.item_id, parent=args.parent)
        print(f"[OK] registered {args.item_id}", file=out)
    elif cmd == "approve":
        ledger.approve_limit(args.item_id, args.usd, approver=args.approver, reason=args.reason)
        print(f"[OK] approved {args.usd} USD for {args.item_id}", file=out)
    elif cmd == "import-usage":
        count = ledger.import_usage(load_records(args.file))
        print(f"[OK] imported {count} usage record(s)", file=out)
    elif cmd == "settle":
        status = ledger.settle(args.reservation_id, usage=load_usage(args.usage))
        print(f"[OK] {status}: {args.reservation_id}", file=out)
    elif cmd == "report":
        emit_report(ledger.report(args.item_id), args.format, out)
    elif cmd == "review":
        dump_json(ledger.review(args.item_id, reviewer=args.reviewer, completed=args.completed,
                                remaining=args.remaining, reason=args.reason,
                                projected_usd=args.projected_usd), out)
    elif cmd == "hold":
        ledger.hold_for_review(args.item_id, reason=args.reason, actor=args.actor)
        print(f"[OK] {args.item_id} held for review", file=out)
    elif cmd == "pending":
        dump_json(ledger.pending(args.item_id), out)
    elif cmd == "usage":
        dump_json(ledger.usage(args.item_id), out)
    elif cmd == "history":
        dump_json(ledger.history(args.item_id), out)


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        run(args, sys.stdout)
    except BudgetError as error:
        print(f"[ERROR] {error.code}: {error}", file=sys.stderr)
        return 1
    except OSError:
        print("[ERROR] Cannot access the project or protected budget state", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
