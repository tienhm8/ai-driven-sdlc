"""Read-only project progress, derived from the governance event store.

The SQLite event store written by WorkflowEngine is the single source of
workflow and gate state. Required-output presence is derived from the file
system. Nothing here writes to the store or to the project.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import sqlite3

from .approval_engine import ApprovalEngine
from .config import load_yaml
from .constants import STAGES
from .governance import GATES, STAGE_GATES, WORKFLOW_SCHEMA_VERSION, latest_review

DEFAULT_STATE_DIR = Path.home() / ".ai-sdlc" / "state"
# Project working copies that init-project.py seeds from a differently named template.
TEMPLATE_ALIASES = {
    "outputs/11-requirement-traceability/requirement-traceability-matrix.md": "templates/requirement-traceability.md",
}
REOPEN_EVENTS = {"qa_reopened": "Quay lại QA", "development_reopened": "Quay lại Development"}


def store_path(state_dir: Path, project: Path) -> Path:
    """Where WorkflowEngine keeps this project's database (see ApprovalEngine.__init__)."""
    key = sha256(os.fsencode(project.resolve())).hexdigest()
    return Path(state_dir) / key / "governance.sqlite3"


def latest_sdlc_events(db: Path) -> list[dict]:
    """Events of the newest current-schema SDLC execution; [] when none exists. Opens read-only."""
    if not db.is_file():
        return []
    connection = sqlite3.connect(f"{db.resolve().as_uri()}?mode=ro", uri=True)
    try:
        try:
            rows = connection.execute("SELECT execution_id, event FROM events ORDER BY id").fetchall()
        except sqlite3.OperationalError:
            return []  # file exists but has no events table yet
    finally:
        connection.close()
    runs: dict[str, list[dict]] = {}
    for execution_id, raw in rows:
        runs.setdefault(execution_id, []).append(json.loads(raw))
    sdlc = [events for events in runs.values()
            if events[0].get("kind") == "sdlc" and events[0].get("schema_version") == WORKFLOW_SCHEMA_VERSION]
    return sdlc[-1] if sdlc else []


def _same_bytes(a: Path, b: Path) -> bool:
    try:
        return a.read_bytes() == b.read_bytes()
    except OSError:
        return False


def output_status(project: Path, framework: Path, stage: str, required: list[str]) -> dict:
    """A required output counts as present once it exists and differs from the seeded template."""
    present, missing = [], []
    docs = project / "docs" / stage
    for rel in required:
        path = docs / rel
        if not path.is_file():
            missing.append(rel)
            continue
        sources = [framework / stage / "outputs" / rel.removeprefix("outputs/"),
                   framework / stage / "templates" / Path(rel).name]
        if rel in TEMPLATE_ALIASES:
            sources.append(framework / stage / TEMPLATE_ALIASES[rel])
        (missing if any(_same_bytes(path, s) for s in sources if s.is_file()) else present).append(rel)
    return {"present": present, "missing": missing}


def replay(events: list[dict]) -> dict:
    """Fold events into completed stages, the active stage and notable events."""
    completed: set[str] = set()
    current = events[0]["stage"]
    notes = []
    for event in events:
        kind = event["event_type"]
        if kind == "stage_completed":
            completed.add(event["stage"])
        elif kind in REOPEN_EVENTS:
            keep = STAGES.index(event["next_stage"])
            completed = {s for s in completed if STAGES.index(s) < keep}
            notes.append({"at": event["timestamp"], "note": f"{REOPEN_EVENTS[kind]}: {event['reason']}"})
        elif kind == "action_failed":
            notes.append({"at": event["timestamp"], "note": f"Hành động của {event['gate']} thất bại"})
        elif kind == "gate_blocked":
            notes.append({"at": event["timestamp"], "note": f"{event['gate']} bị chặn ({event['status']})"})
        if "next_stage" in event:
            current = event["next_stage"]
    return {"completed": completed, "current": current, "notes": notes}


def gate_state(events: list[dict], stage: str, completed: bool) -> dict | None:
    gate = STAGE_GATES.get(stage)
    if gate is None:
        return None
    if completed:
        return {"id": gate, "state": "approved"}
    review = latest_review(events, gate)
    if review is None:
        return {"id": gate, "state": "pending"}
    status, _, _ = ApprovalEngine._decision(events, review)
    state = {"blocked": "blocked", "awaiting_approval": "review_requested",
             "exception_authorized": "exception_authorized"}.get(status, "approved")
    return {"id": gate, "state": state}


def _lead_role(stage_meta: dict) -> str:
    return next((t["role"] for t in stage_meta["tasks"] if t["kind"] == "do"), stage_meta["tasks"][0]["role"])


def collect_progress(project: Path, framework: Path, state_dir: Path = DEFAULT_STATE_DIR) -> dict:
    project = project.resolve()
    guide = load_yaml(framework / "guide" / "guide-data.yml", required=True)
    meta = {s["id"]: s for s in guide["stages"]}
    events = latest_sdlc_events(store_path(state_dir, project))
    folded = replay(events) if events else {"completed": set(), "current": None, "notes": []}
    stages, actions = [], []

    for stage in STAGES:
        done = stage in folded["completed"]
        outputs = output_status(project, framework, stage, meta[stage].get("required_outputs", []))
        gate = gate_state(events, stage, done) if events else (
            {"id": STAGE_GATES[stage], "state": "pending"} if stage in STAGE_GATES else None)
        if done:
            status = "completed"
        elif stage == folded["current"]:
            status = {"blocked": "blocked", "review_requested": "awaiting_gate"}.get(gate["state"] if gate else "", "in_progress")
        else:
            status = "not_started"
        stages.append({"id": stage, "status": status, "gate": gate, "outputs": outputs})

        if stage != folded["current"] or done:
            continue
        lead = _lead_role(meta[stage])
        approvers = (meta[stage].get("gate") or {}).get("approvers", [])
        if status == "awaiting_gate":
            actions += [{"role": r, "text": f"Duyệt {gate['id']} cho giai đoạn {stage}"} for r in approvers]
        elif gate and gate["state"] in {"approved", "exception_authorized"}:
            action = GATES[gate["id"]].action
            actions.append({"role": lead, "text": f"{gate['id']} đã có quyết định: "
                            + (f"thực hiện hành động được duyệt ({action}) rồi hoàn tất giai đoạn" if action
                               else "hoàn tất giai đoạn và bàn giao")})
        elif status == "blocked":
            actions.append({"role": lead, "text": f"{gate['id']} đang bị chặn: xử lý ý kiến từ chối hoặc yêu cầu sửa rồi trình lại"})
        else:
            actions += [{"role": lead, "text": f"Hoàn thiện đầu ra: {m}"} for m in outputs["missing"]]
            if not outputs["missing"]:
                actions.append({"role": lead, "text": "Đủ đầu ra bắt buộc: hoàn tất checklist và trình duyệt gate" if gate
                                else "Hoàn tất checklist và bàn giao sang giai đoạn sau"})

    if not events:
        state = "not_started"
        actions = [{"role": _lead_role(meta[STAGES[0]]),
                    "text": f"Dự án chưa có workflow trong governance store. Bắt đầu từ giai đoạn {STAGES[0]}"}]
    elif folded["current"] is None or len(folded["completed"]) == len(STAGES):
        state = "completed"
    else:
        state = next(s["status"] for s in stages if s["id"] == folded["current"])
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "workflow": {"state": state, "current_stage": folded["current"]},
        "stages": stages,
        "next_actions": actions,
        "events": folded["notes"][-10:],
    }
