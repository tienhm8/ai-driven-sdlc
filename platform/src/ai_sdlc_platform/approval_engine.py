from pathlib import Path
import json
from .config import load_yaml
from .audit import emit_event

class ApprovalEngine:
    def __init__(self, project: Path, framework: Path | None = None):
        self.project = project
        self.policy = {}
        if framework:
            self.policy = load_yaml(framework / "governance/human-review-gates/gate-policy.yaml")
        self.policy = _merge(self.policy, load_yaml(project / ".ai-sdlc/approval-policy.yaml"))

    def required(self, gate):
        return self.policy.get("gates", {}).get(gate, {}).get("required", gate in {f"G{i}" for i in range(1,8)})

    def approve(self, execution_id, gate, approver, decision, comment=""):
        if decision not in {"approved","rejected","changes_requested"}: raise ValueError("Invalid decision")
        record = {"execution_id":execution_id,"gate_id":gate,"approver":approver,
                  "decision":decision,"comment":comment}
        folder = self.project / ".ai-sdlc/audit"
        folder.mkdir(parents=True, exist_ok=True)
        with (folder / "approvals.jsonl").open("a",encoding="utf-8") as f:
            f.write(json.dumps(record,ensure_ascii=False)+"\n")
        emit_event(self.project, execution_id, "approval_recorded", gate=gate, approver=approver, decision=decision)
        return record

    def latest_decision(self, execution_id, gate):
        path = self.project / ".ai-sdlc/audit/approvals.jsonl"
        if not path.exists(): return None
        latest = None
        for line in path.read_text(encoding="utf-8").splitlines():
            try: row = json.loads(line)
            except json.JSONDecodeError: continue
            if row.get("execution_id")==execution_id and row.get("gate_id")==gate: latest=row.get("decision")
        return latest

def _merge(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=_merge(out[k],v) if isinstance(v,dict) and isinstance(out.get(k),dict) else v
    return out
