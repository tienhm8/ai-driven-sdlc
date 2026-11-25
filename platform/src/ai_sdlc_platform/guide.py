"""Load and validate guide data, and embed it into the guide page."""
import json
from pathlib import Path
import re

import yaml

from .constants import STAGES
from .governance import GATES, STAGE_GATES

MARKER = re.compile(r'(<script id="guide-data" type="application/json">)(.*?)(</script>)', re.S)
KINDS = {"do", "confirm", "approve"}


def load_guide_data(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("guide data must be a mapping")
    return data


def validate_guide_data(data: dict, framework: Path) -> list[str]:
    """Return problems: unknown ids, stage/gate drift from code, missing link targets."""
    problems = []
    roles = {role["id"] for role in data["roles"]}
    groups = {group["id"] for group in data["groups"]}
    for role in data["roles"]:
        if role["group"] not in groups:
            problems.append(f"role {role['id']}: unknown group {role['group']}")
    if [s["id"] for s in data["stages"]] != STAGES:
        problems.append("stages do not match platform STAGES")

    def check_link(owner, path):
        if not (framework / path).exists():
            problems.append(f"{owner}: missing file {path}")

    for stage in data["stages"]:
        sid = stage["id"]
        gate = stage.get("gate")
        code_gate = STAGE_GATES.get(sid)
        if gate is None:
            # Stage 08 is covered by G7, which belongs to no stage in code.
            if code_gate:
                problems.append(f"{sid}: guide has no gate but code defines {code_gate}")
        else:
            expected = code_gate or ("G7" if sid == STAGES[-1] else None)
            if gate["id"] != expected:
                problems.append(f"{sid}: gate {gate['id']} does not match {expected}")
            elif gate["id"] in GATES:
                code_roles = GATES[gate["id"]].roles
                if not set(gate["approvers"]) <= code_roles:
                    problems.append(f"{sid}: approvers {gate['approvers']} not allowed by {gate['id']}")
                if bool(gate.get("all_required")) != GATES[gate["id"]].require_all_roles:
                    problems.append(f"{sid}: all_required differs from code for {gate['id']}")
            for approver in gate["approvers"]:
                if approver not in roles:
                    problems.append(f"{sid}: unknown approver {approver}")
            check_link(f"{sid} gate doc", gate["doc"])
        for key in ("guide", "inputs_link", "outputs_link"):
            check_link(f"{sid} {key}", stage[key])
        for task in stage["tasks"]:
            if set(task) != {"role", "kind", "text", "link"}:
                problems.append(f"{sid}: task keys {sorted(task)} (quote text containing commas)")
                continue
            if task["role"] not in roles:
                problems.append(f"{sid}: unknown role {task['role']}")
            if task["kind"] not in KINDS:
                problems.append(f"{sid}: unknown kind {task['kind']}")
            check_link(f"{sid} task link", task["link"])
    return problems


def render_guide_html(page_text: str, data_path: Path) -> str:
    data = load_guide_data(data_path)
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    if len(MARKER.findall(page_text)) != 1:
        raise ValueError("index.html must contain exactly one guide-data script block")
    return MARKER.sub(lambda m: m.group(1) + payload + m.group(3), page_text)
