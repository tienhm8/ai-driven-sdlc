"""Local Story/Feature ledger. Amounts are integer microdollars, never floats."""
from contextlib import closing, contextmanager
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import sqlite3
from stat import S_ISDIR, S_ISREG
from uuid import uuid4

from .budget_usage import (BASES, ITEM, RANK, BudgetError, identifier, invalid, normalize_usage, note,
                           usd_micros, usd_text)

BUDGET_WARN_PCT = 80
_SCHEMA = (
    """CREATE TABLE IF NOT EXISTS items(
           id TEXT PRIMARY KEY, parent TEXT REFERENCES items(id), cap INTEGER, hold TEXT, required_cap INTEGER,
           reviewed_until INTEGER)""",
    """CREATE TABLE IF NOT EXISTS usage(
           provider TEXT, account TEXT, event TEXT, item TEXT REFERENCES items(id), session TEXT, unit TEXT,
           request TEXT, sequence INTEGER, rank INTEGER, active INTEGER NOT NULL, micros INTEGER, metadata TEXT NOT NULL,
           PRIMARY KEY(provider, account, event))""",
    "CREATE INDEX IF NOT EXISTS usage_session ON usage(provider, account, session)",
    "CREATE INDEX IF NOT EXISTS usage_item ON usage(item, active)",
    """CREATE UNIQUE INDEX IF NOT EXISTS usage_request ON usage(provider, account, request)
       WHERE request IS NOT NULL""",
    """CREATE TABLE IF NOT EXISTS reservations(
           id TEXT PRIMARY KEY, item TEXT REFERENCES items(id), run TEXT, attempt INTEGER, quote INTEGER,
           status TEXT NOT NULL, metadata TEXT NOT NULL, settled TEXT UNIQUE, UNIQUE(run, attempt))""",
    "CREATE INDEX IF NOT EXISTS reservations_item ON reservations(item, status)",
    """CREATE TABLE IF NOT EXISTS history(
           id INTEGER PRIMARY KEY, item TEXT REFERENCES items(id), event TEXT, at TEXT, data TEXT NOT NULL)""",
    """CREATE TABLE IF NOT EXISTS usage_receipts(
           provider TEXT, account TEXT, event TEXT, metadata TEXT, PRIMARY KEY(provider,account,event,metadata))""",
)


def _now():
    return datetime.now(timezone.utc).isoformat()


def _json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _item(value):
    return identifier(value, "work-item ID", pattern=ITEM)


class BudgetLedger:
    """Trusted operator/adapter boundary; OS access to state supplies authority, not actor labels."""

    def __init__(self, project: Path, state_dir: Path):
        self.project = project.resolve(strict=True)
        if not self.project.is_dir():
            raise invalid("Project Instance must be a directory")
        # Resolve the operator-supplied root once, as governance state does. Everything below it
        # (per-project directory, database and sidecars) is still checked for symlinks.
        self.state_dir = Path(state_dir).expanduser().resolve()
        self._require_root_private()
        self.path = self.state_dir / sha256(os.fsencode(self.project)).hexdigest() / "cost" / "budget.sqlite3"
        self._check_location()

    def _require_root_private(self):
        """The resolved root may be reached through a symlink, but it must not be swappable by another user.

        Every existing ancestor is checked too: a root owned by the operator inside a world-writable directory
        could otherwise be renamed or replaced by another user. Sticky directories (such as /tmp) are accepted.
        """
        euid = os.geteuid()
        for directory in self.state_dir.parents:
            try:
                stat = directory.stat()
            except FileNotFoundError:
                continue
            sticky = stat.st_mode & 0o1000
            if not S_ISDIR(stat.st_mode) or stat.st_uid not in (0, euid) or (stat.st_mode & 0o022 and not sticky):
                raise invalid("Budget state root must sit under directories the operator controls, not writable by others")
        try:
            stat = self.state_dir.stat()
        except FileNotFoundError:
            return  # created on first write, with private permissions
        if not S_ISDIR(stat.st_mode) or stat.st_uid != euid or stat.st_mode & 0o022:
            raise invalid("Budget state root must be a directory owned by the operator and not writable by others")

    def _create_private_tree(self):
        """Create every missing directory from the first existing ancestor down to the database, as 0700."""
        missing = []
        probe = self.path.parent
        while not probe.exists():  # climbs past missing root levels, so a multi-level root is created too
            missing.append(probe)
            probe = probe.parent
        for directory in reversed(missing):
            directory.mkdir(mode=0o700, exist_ok=True)
            directory.chmod(0o700)  # mkdir's mode is masked by the umask; make the result explicit

    def _check_location(self):
        self._require_root_private()
        for suffix in ("", "-journal", "-wal", "-shm"):
            entry = self.path.with_name(self.path.name + suffix)
            if entry.resolve() != entry or entry.is_relative_to(self.project):
                raise invalid("Budget state must be outside the project and must not traverse symlinks")

    @staticmethod
    def _require_private(path, mode_check):
        stat = path.stat()
        if not mode_check(stat.st_mode) or stat.st_mode & 0o077 or stat.st_uid != os.geteuid():
            raise invalid("Budget state directory and database must be private to the operator identity")

    @contextmanager
    def _db(self, *, write=False):
        self._check_location()
        if write:
            self._create_private_tree()
            self._check_location()
            # The private directory protects the database and SQLite sidecars.
            self._require_private(self.path.parent, S_ISDIR)
            flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
            try:
                fd = os.open(self.path, flags, 0o600)
            except FileExistsError:
                pass
            else:
                os.close(fd)
        elif not self.path.is_file():
            raise BudgetError("BUDGET_STATE_MISSING", "Budget ledger has not been created")
        self._check_location()
        self._require_private(self.path.parent, S_ISDIR)
        self._require_private(self.path, S_ISREG)
        try:
            uri = self.path.as_uri() + ("?mode=rw" if write else "?mode=ro")
            with closing(sqlite3.connect(uri, uri=True, timeout=10)) as conn:
                conn.row_factory = sqlite3.Row
                conn.execute("PRAGMA foreign_keys = ON")
                with conn:
                    conn.execute("BEGIN IMMEDIATE" if write else "BEGIN")
                    version = conn.execute("PRAGMA user_version").fetchone()[0]
                    if version == 0 and write:
                        for statement in _SCHEMA:
                            conn.execute(statement)
                        conn.execute("PRAGMA user_version = 1")
                    elif version != 1:
                        raise BudgetError("BUDGET_STATE_INVALID", "Unsupported budget database version")
                    yield conn
        except sqlite3.Error:
            raise BudgetError("BUDGET_STATE_UNAVAILABLE", "Budget database unavailable; inspect protected state") from None

    @staticmethod
    def _row(conn, item):
        row = conn.execute("SELECT * FROM items WHERE id=?", (_item(item),)).fetchone()
        if row is None:
            raise BudgetError("WORK_ITEM_UNKNOWN", "Register the work item from the backlog first")
        return row

    @staticmethod
    def _event(conn, item, event, **data):
        conn.execute("INSERT INTO history(item,event,at,data) VALUES (?,?,?,?)", (item, event, _now(), _json(data)))

    def register_item(self, item_id, parent=None):
        item_id = _item(item_id)
        if parent is not None:
            _item(parent)
        with self._db(write=True) as conn:
            old = conn.execute("SELECT parent FROM items WHERE id=?", (item_id,)).fetchone()
            if old is not None:
                if old["parent"] != parent:
                    raise invalid("An existing work item's parent cannot be reassigned")
                return
            if parent is not None and (self._row(conn, parent)["parent"] is not None or parent == item_id):
                raise invalid("Only a top-level Feature may be the parent")
            conn.execute("INSERT INTO items(id,parent) VALUES (?,?)", (item_id, parent))
            self._event(conn, item_id, "registered", parent=parent)

    def approve_limit(self, item_id, usd, *, approver, reason):
        cap = usd_micros(usd)
        approver, reason = identifier(approver, "approver"), note(reason, "reason")
        with self._db(write=True) as conn:
            row = self._row(conn, item_id)
            if row["cap"] == cap:
                raise invalid("Approved amount is unchanged")
            clear = row["hold"] == "awaiting-approval" and row["required_cap"] is not None and cap >= row["required_cap"]
            reviewed_until = None
            if clear:
                spent, coverage, _, _, reserved, pending = self._totals(conn, row)
                if not (pending or coverage["unmeasured"]) and sum(spent.values()) + reserved <= row["required_cap"]:
                    reviewed_until = row["required_cap"]
            hold = (None if reviewed_until is not None else "review-required") if clear else row["hold"]
            conn.execute("UPDATE items SET cap=?, reviewed_until=?, hold=?, required_cap=? WHERE id=?",
                         (cap, reviewed_until, hold, None if clear else row["required_cap"], item_id))
            self._event(conn, item_id, "limit-approved", old_usd=usd_text(row["cap"]), new_usd=usd_text(cap),
                        approver=approver, reason=reason)
            return self._report(conn, item_id)

    @staticmethod
    def _group(row):
        return ("item=? OR item IN (SELECT id FROM items WHERE parent=?)", (row["id"], row["id"])) if row["parent"] is None else (
            "item=?", (row["id"],))

    def _totals(self, conn, row):
        where, args = self._group(row)
        spent = dict.fromkeys(BASES, 0)
        coverage = dict.fromkeys(BASES, 0)
        seat_coverage = {"estimated": 0, "unmeasured": 0}
        seat = 0
        for usage in conn.execute(f"SELECT micros,metadata FROM usage WHERE active=1 AND ({where})", args):
            data = json.loads(usage["metadata"])
            basis, micros = data["basis"], usage["micros"]
            if data["charge"] == "seat":
                seat_coverage[basis] += 1
                if micros is not None:
                    seat += micros
            else:
                coverage[basis] += 1
                if micros is not None:
                    spent[basis] += micros
        reservations = list(conn.execute(f"SELECT quote,status FROM reservations WHERE status IN ('active','pending') AND ({where})", args))
        return (spent, coverage, seat, seat_coverage, sum(r["quote"] for r in reservations),
                sum(r["status"] == "pending" for r in reservations))

    @staticmethod
    def _status(row, spent, missing, pending, reserved):
        cap = row["cap"]
        if row["hold"] == "awaiting-approval":
            return "awaiting-approval"
        if row["hold"] == "review-required":
            return "review-required"
        if missing or pending:
            return "incomplete-coverage"
        if cap is None:
            return "no-approved-limit"
        if spent > cap:
            return "review-required"
        if row["reviewed_until"] is not None and spent + reserved > row["reviewed_until"]:
            return "review-required"
        if cap > 0 and spent * 100 >= cap * BUDGET_WARN_PCT and row["reviewed_until"] is None:
            return "review-required"
        return "ready"

    def _report(self, conn, item):
        row = self._row(conn, item)
        spent, coverage, seat, seat_coverage, reserved, pending = self._totals(conn, row)
        used = sum(spent.values())
        cap = row["cap"]
        remaining = None if cap is None or coverage["unmeasured"] or pending else cap - used - reserved
        need = None if row["required_cap"] is None or cap is None else max(0, row["required_cap"] - cap)
        return {"work_item_id": item, "parent": row["parent"], "approved": usd_text(cap),
                "spent": {basis: usd_text(spent[basis]) if basis != "unmeasured" else None for basis in BASES},
                "known_metered_total": usd_text(used),
                "seat_estimates": usd_text(seat) if seat_coverage["estimated"] else None,
                "reserved": usd_text(reserved), "remaining": usd_text(remaining),
                "coverage": {"metered_records": coverage, "seat_records": seat_coverage, "pending_attempts": pending,
                             "outside_managed_runner": "not-enforced"},
                "budget_warn_pct": BUDGET_WARN_PCT, "enforcement": "projected-soft-cap",
                "increase_needed": usd_text(need), "reviewed_until": usd_text(row["reviewed_until"]),
                "status": self._status(row, used, coverage["unmeasured"], pending, reserved)}

    def report(self, item_id):
        with self._db() as conn:
            return self._report(conn, item_id)

    def hold_for_review(self, item_id, *, reason, actor):
        reason, actor = note(reason, "reason"), identifier(actor, "actor")
        with self._db(write=True) as conn:
            self._hold(conn, item_id, reason, actor)
            return self._report(conn, item_id)

    def _hold(self, conn, item, reason, actor):
        row = self._row(conn, item)
        if row["hold"] != "awaiting-approval":
            conn.execute("UPDATE items SET hold='review-required' WHERE id=?", (item,))
        self._event(conn, item, "review-hold", reason=reason, actor=actor)

    def _hold_managed_scope(self, conn, item):
        work = self._row(conn, item)
        for scope in (item, work["parent"]):
            if scope is not None and self._row(conn, scope)["cap"] is not None:
                self._hold(conn, scope, "Managed attempt hit provider budget limit or exceeded its quote", "managed-runner")

    def review(self, item_id, *, reviewer, completed, remaining, reason, projected_usd):
        reviewer = identifier(reviewer, "reviewer")
        summaries = {key: note(value, key) for key, value in (("completed", completed), ("remaining", remaining), ("reason", reason))}
        projected = usd_micros(projected_usd)
        with self._db(write=True) as conn:
            row = self._row(conn, item_id)
            spent, coverage, _, _, reserved, pending = self._totals(conn, row)
            cap = row["cap"]
            if cap is None or pending or coverage["unmeasured"]:
                raise BudgetError("BUDGET_REVIEW_INCOMPLETE", "Resolve missing costs/pending attempts and set an approved limit first")
            required = sum(spent.values()) + reserved + projected
            shortfall = max(0, required - cap)
            if required > 9_000_000_000_000_000_000:
                raise invalid("Projected total exceeds the supported budget range")
            if row["hold"] == "awaiting-approval" and required < row["required_cap"]:
                raise BudgetError("BUDGET_INCREASE_PENDING", "A pending increase must be decided by the budget approver")
            conn.execute("UPDATE items SET hold=?, required_cap=?, reviewed_until=? WHERE id=?",
                         ("awaiting-approval" if shortfall else None, required if shortfall else None, required, item_id))
            self._event(conn, item_id, "budget-reviewed", reviewer=reviewer, projected_usd=usd_text(projected),
                        increase_needed=usd_text(shortfall), **summaries)
            return self._report(conn, item_id)

    def history(self, item_id):
        with self._db() as conn:
            self._row(conn, item_id)
            return [{"event": row["event"], "at": row["at"], **json.loads(row["data"])} for row in conn.execute(
                "SELECT * FROM history WHERE item=? ORDER BY id", (item_id,))]

    def _ingest(self, conn, data, micros, *, link_pending=False):
        item, provider, account, key, session = (data[k] for k in ("work_item_id", "provider", "account", "event_id", "session_id"))
        self._row(conn, item)
        encoded = _json(data)
        identity = (provider, account, key)
        if conn.execute("SELECT 1 FROM usage_receipts WHERE provider=? AND account=? AND event=? AND metadata=?",
                        (*identity, encoded)).fetchone():
            return False
        existing = conn.execute("SELECT * FROM usage WHERE provider=? AND account=? AND event=?", identity).fetchone()
        sequence = data.get("sequence", 1)
        rank = RANK[data["basis"]]
        if existing:
            prior = json.loads(existing["metadata"])
            immutable = ("work_item_id", "repo", "stage", "task", "run_id", "session_id", "unit", "charge", "request_id", "attempt")
            if any(data.get(k) != prior.get(k) for k in immutable) or sequence != existing["sequence"]:
                raise BudgetError("USAGE_ID_CONFLICT", "An existing usage event cannot change attribution or sequence")
            if not existing["active"]:
                raise BudgetError("USAGE_SNAPSHOT_CONFLICT", "Reconcile the current session total, not an archived snapshot")
            if rank <= existing["rank"]:
                raise BudgetError("USAGE_ID_CONFLICT", "Use the identical event for a replay or a stronger basis for reconciliation")
        else:
            for row in conn.execute("SELECT * FROM usage WHERE provider=? AND account=? AND session=? AND active=1",
                                    (provider, account, session)):
                prior = json.loads(row["metadata"])
                if (row["item"] != item or row["unit"] != data["unit"] or prior["charge"] != data["charge"]):
                    raise BudgetError("USAGE_SCOPE_CONFLICT", "A provider/account/session must use one work item, charge and accounting unit")
                if data["unit"] == "session":
                    if (sequence <= row["sequence"] or rank < row["rank"]
                            or (micros is not None and row["micros"] is not None and micros < row["micros"] and rank == row["rank"])):
                        raise BudgetError("USAGE_SNAPSHOT_CONFLICT", "Cumulative updates require newer sequence and non-regressing cost/basis")
                    conn.execute("UPDATE usage SET active=0 WHERE provider=? AND account=? AND event=?",
                                 (provider, account, row["event"]))
            if data.get("request_id") and conn.execute(
                "SELECT 1 FROM usage WHERE provider=? AND account=? AND request=?",
                (provider, account, data["request_id"]),
            ).fetchone():
                raise BudgetError("USAGE_ID_CONFLICT", "The request is already attributed to another event")
        conn.execute("""INSERT INTO usage(provider,account,event,item,session,unit,request,sequence,rank,active,micros,metadata)
                     VALUES (?,?,?,?,?,?,?,?,?,1,?,?) ON CONFLICT(provider,account,event) DO UPDATE SET
                     rank=excluded.rank,micros=excluded.micros,metadata=excluded.metadata""",
                     (*identity, item, session, data["unit"], data.get("request_id"), sequence, rank, micros, encoded))
        conn.execute("INSERT INTO usage_receipts VALUES (?,?,?,?)", (*identity, encoded))
        self._event(conn, item, "usage-reconciled" if existing else "usage-imported",
                    provider=provider, account=account, source_event=key, basis=data["basis"], usd=usd_text(micros))
        linked = conn.execute("SELECT id,quote,status FROM reservations WHERE settled=?", (_json(identity),)).fetchone()
        if linked is None and link_pending and data.get("run_id") and data.get("attempt") and data["unit"] == "request":
            # Only an operator import may close a pending reservation by run and attempt. settle() already holds
            # the reservation it is settling, and must not have it closed (and its history written) underneath it.
            # The provider and tool must match the dispatched attempt so an unrelated or mislabeled record with
            # the same run and attempt cannot clear the pending/incomplete-coverage gate.
            candidate = conn.execute(
                "SELECT id,quote,status,metadata FROM reservations WHERE run=? AND attempt=? AND item=? "
                "AND status='pending' AND settled IS NULL", (data["run_id"], data["attempt"], item)).fetchone()
            if candidate is not None and self._same_dispatch(json.loads(candidate["metadata"]), data):
                linked = candidate
                conn.execute("UPDATE reservations SET settled=? WHERE id=?", (_json(identity), linked["id"]))
        if linked is not None and linked["status"] == "pending" and micros is not None:
            conn.execute("UPDATE reservations SET status='settled' WHERE id=?", (linked["id"],))
            self._event(conn, item, "settled", reservation_id=linked["id"])
        if linked is not None and micros is not None and micros > linked["quote"]:
            self._hold_managed_scope(conn, item)
        return True

    @staticmethod
    def _same_dispatch(reservation, data):
        """Repo/stage/task must match the dispatched attempt. `tool` is optional on invoices, so it is compared only
        when the record carries it. The provider (always present on a record) must match when the reservation
        recorded one; reservations made without a configured provider cannot be checked on it."""
        tool = data.get("tool")
        if tool is not None and tool != reservation.get("tool"):
            return False
        if "provider" in reservation and data.get("provider") != reservation["provider"]:
            return False
        return all(data.get(key) == reservation.get(key) for key in ("repo", "stage", "task"))

    def import_usage(self, records):
        if not isinstance(records, list) or not records or len(records) > 10_000:
            raise invalid("Import requires an array of 1–10000 usage records")
        inputs = [normalize_usage(raw) for raw in records]
        with self._db(write=True) as conn:
            return sum(self._ingest(conn, data, micros, link_pending=True) for data, micros in inputs)

    def reserve(self, item_id, quote_usd, *, run_id, attempt, repo, stage, task, tool, provider=None):
        quote = usd_micros(quote_usd, positive=True)
        if type(attempt) is not int or not 1 <= attempt <= 1_000_000_000:
            raise invalid("Invalid attempt number")
        fields = {k: identifier(v, k) for k, v in (("run_id", run_id), ("repo", repo), ("stage", stage),
                                                   ("task", task), ("tool", tool))}
        if provider is not None:  # operator-configured provider of the dispatch; checked on import and settlement
            fields["provider"] = identifier(provider, "provider")
        with self._db(write=True) as conn:
            row = self._row(conn, item_id)
            scopes = [row] + ([self._row(conn, row["parent"])] if row["parent"] else [])
            if not any(scope["cap"] is not None for scope in scopes):
                raise BudgetError("BUDGET_NOT_APPROVED", "No approved work-item or parent limit")
            if conn.execute("SELECT 1 FROM reservations WHERE run=? AND attempt=?", (run_id, attempt)).fetchone():
                raise BudgetError("BUDGET_DUPLICATE_ATTEMPT", "This run attempt already has a reservation")
            for scope in scopes:
                costs, coverage, _, _, reserved, pending = self._totals(conn, scope)
                spent = sum(costs.values())
                status = self._status(scope, spent, coverage["unmeasured"], pending, reserved)
                if status not in {"ready", "no-approved-limit"}:
                    raise BudgetError("BUDGET_" + status.upper().replace("-", "_"), f"{scope['id']}: {status}")
                cap = scope["cap"]
                projected = spent + reserved + quote
                if cap is not None and projected > cap:
                    raise BudgetError("BUDGET_LIMIT_EXCEEDED", f"{scope['id']}: projected next attempt exceeds the limit")
                if scope["reviewed_until"] is not None and projected > scope["reviewed_until"]:
                    raise BudgetError("BUDGET_REVIEW_REQUIRED", f"{scope['id']}: next attempt exceeds the reviewed projection")
            reservation = uuid4().hex
            fields.update(work_item_id=item_id, attempt=attempt)
            conn.execute("INSERT INTO reservations VALUES (?,?,?,?,?,'active',?,NULL)",
                         (reservation, item_id, run_id, attempt, quote, _json(fields)))
            self._event(conn, item_id, "reserved", reservation_id=reservation, quote_usd=usd_text(quote), **fields)
            return reservation

    def settle(self, reservation_id, *, usage=None, not_dispatched=False, budget_cutoff=False):
        identifier(reservation_id, "reservation ID")
        if not_dispatched and (usage is not None or budget_cutoff):
            raise invalid("Only an undispatched attempt may be released without usage")
        with self._db(write=True) as conn:
            row = conn.execute("SELECT * FROM reservations WHERE id=?", (reservation_id,)).fetchone()
            if row is None:
                raise BudgetError("RESERVATION_UNKNOWN", "Unknown reservation")
            item = row["item"]
            if usage is None:
                status = "released" if not_dispatched else "pending"
                if row["status"] == status and not budget_cutoff:
                    return status
                if row["status"] not in ("active", "pending") or (not_dispatched and row["status"] != "active"):
                    raise BudgetError("RESERVATION_CLOSED", "Reservation cannot be changed")
                conn.execute("UPDATE reservations SET status=? WHERE id=?", (status, reservation_id))
            else:
                if not isinstance(usage, dict):
                    raise invalid("Settlement requires a usage object")
                fields = json.loads(row["metadata"])
                if (any(key in usage and usage[key] != value for key, value in fields.items())
                        or usage.get("unit", "request") != "request" or usage.get("charge", "metered") != "metered"):
                    raise invalid("Settlement cannot override reservation attribution or accounting unit")
                data, micros = normalize_usage({**usage, **fields, "unit": "request"})
                identity = tuple(data[k] for k in ("provider", "account", "event_id"))
                key = _json(identity)
                if row["status"] == "released" or (row["settled"] is not None and row["settled"] != key):
                    raise BudgetError("RESERVATION_CLOSED", "Reservation already has a different settlement")
                if conn.execute("SELECT 1 FROM reservations WHERE settled=? AND id<>?", (key, reservation_id)).fetchone():
                    raise BudgetError("USAGE_ID_CONFLICT", "This usage event belongs to another settlement")
                self._ingest(conn, data, micros)
                # An identical older-basis replay must not return a settled reservation to pending.
                current = conn.execute("SELECT micros FROM usage WHERE provider=? AND account=? AND event=?",
                                       identity).fetchone()[0]
                status = "pending" if current is None else "settled"
                if row["status"] == status and row["settled"] == key:
                    return status
                conn.execute("UPDATE reservations SET status=?,settled=? WHERE id=?", (status, key, reservation_id))
                if row["settled"] is None and current is not None and current > row["quote"]:
                    budget_cutoff = True
            self._event(conn, item, status, reservation_id=reservation_id)
            if budget_cutoff:
                self._hold_managed_scope(conn, item)
            return status

    def usage(self, item_id):
        """Active accounting rows, with child attribution and no archived duplicates."""
        with self._db() as conn:
            row = self._row(conn, item_id)
            where, args = self._group(row)
            return [{**json.loads(entry["metadata"]), "usd": usd_text(entry["micros"]),
                     "parent": entry["parent"]} for entry in conn.execute(
                f"SELECT usage.metadata,usage.micros,items.parent FROM usage JOIN items ON items.id=usage.item "
                f"WHERE active=1 AND ({where}) ORDER BY provider,account,event", args)]

    def pending(self, item_id):
        with self._db() as conn:
            where, args = self._group(self._row(conn, item_id))
            return [{**json.loads(row["metadata"]), "reservation_id": row["id"], "status": row["status"],
                     "quote_usd": usd_text(row["quote"])} for row in conn.execute(
                f"SELECT * FROM reservations WHERE status IN ('active','pending') AND ({where}) ORDER BY rowid", args)]
