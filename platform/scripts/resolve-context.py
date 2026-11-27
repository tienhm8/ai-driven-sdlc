#!/usr/bin/env python3
"""Explain the planned context and route without opening an AI session."""
import argparse
import json
from pathlib import Path
import sys

from yaml import YAMLError

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "platform" / "src"))

from ai_sdlc_platform.context_resolver import ContextRequest, resolve_context
from ai_sdlc_platform.context_resources import FOCUS_TAGS
from ai_sdlc_platform.manifest_schema import strict_yaml_mapping
from ai_sdlc_platform.progress import DEFAULT_STATE_DIR
from ai_sdlc_platform.tool_adapters import ToolAdapterRegistry


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True, help="Project Instance root")
    parser.add_argument("--workspace-config", type=Path, required=True, help="Trusted config outside workspaces")
    parser.add_argument("--state-dir", type=Path, default=DEFAULT_STATE_DIR, help="Trusted governance state directory")
    parser.add_argument("--adapters-dir", type=Path, help="Trusted adapter registry for approved binding preview")
    for field in ("work-item-id", "repo", "revision", "role", "stage", "task", "risk"):
        parser.add_argument(f"--{field}", required=True)
    parser.add_argument("--path", action="append", required=True, help="File or module path relative to the repo")
    parser.add_argument("--focus", action="append", default=[], choices=sorted(FOCUS_TAGS))
    parser.add_argument("--action", choices=("prepare", "coding", "merge"), default="prepare")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)
    try:
        request = ContextRequest(args.work_item_id, args.repo, args.revision, args.role, args.stage, args.task,
                                 args.risk, tuple(args.path), frozenset(args.focus), args.action)
        request.validate()
    except ValueError as exc:
        parser.error(str(exc))
    try:
        config_path = args.workspace_config.resolve(strict=True)
        workspace = strict_yaml_mapping(config_path.read_text(encoding="utf-8"))
        roots = [args.project.resolve(), *(Path(entry["checkout"]).resolve()
                                           for entry in workspace.get("repositories", {}).values())]
        if any(config_path.is_relative_to(root) for root in roots):
            raise ValueError("Workspace configuration is inside a checkout")
        adapters = ToolAdapterRegistry(args.adapters_dir) if args.adapters_dir is not None else None
        if adapters is not None:
            adapters.require_outside(roots)
    except (OSError, ValueError, RuntimeError, TypeError, AttributeError, KeyError, YAMLError):
        parser.error("Expected trusted workspace and adapter configuration outside the instance and registered checkouts")
    result = resolve_context(args.project, ROOT / "framework", ROOT / "shared-ai", workspace, args.state_dir, request,
                             adapters=adapters)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"{result['status']}: {request.work_item_id} / {request.repo}@{request.revision} (preview, no authority)")
        for key, policy in result.get("policies", {}).items():
            print(f"{key}: {policy['id']} (v{policy['version'] or '?'})")
        for technology, versions in result.get("stack", {}).items():
            print(f"Stack {technology}: declared={versions['declared']}, observed={versions['observed'] or 'unverified'}")
        if route := result["route"]:
            native = f", native effort: {route['native_effort']}" if route['native_effort'] else ""
            print(f"Route: {route['profile']}/{route['effort']} via {route['tool']} → {route['model']}"
                  f" ({route['status']}{native})")
        if gate := result["gate"]:
            print(f"Gate: {gate['id']} {gate['status']} ({gate['reason']})")
        for kind in ("rules", "skills"):
            print(kind.capitalize() + ":")
            for item in result[kind]:
                marker = "+" if item["selected"] else "-"
                print(f"  {marker} {item['id']} [{item['source']}] — {item['reason']}")
                for ref in item.get("references", ()):
                    print(f"      {ref}")
        for key, label in (("warnings", "Warning"), ("blockers", "Blocker")):
            for issue in result[key]:
                print(f"{label} {issue['code']}: {issue.get('message', issue.get('technology', ''))}")
    return 1 if result["status"] == "blocked" else 0


if __name__ == "__main__":
    raise SystemExit(main())
