from pathlib import Path
from .constants import STAGES
from .audit import new_execution_id, emit_event
from .approval_engine import ApprovalEngine

class WorkflowEngine:
    def __init__(self, project: Path, framework: Path | None = None):
        self.project=project
        self.approvals=ApprovalEngine(project,framework)

    def start(self, stage, actor="system"):
        if stage not in STAGES: raise ValueError(f"Unknown stage: {stage}")
        run_id=new_execution_id()
        emit_event(self.project,run_id,"workflow_started",stage=stage,actor=actor,status="in_progress")
        return {"execution_id":run_id,"stage":stage,"status":"in_progress"}

    def complete_stage(self, execution_id, stage, actor="ai", output_refs=None):
        if stage not in STAGES: raise ValueError(f"Unknown stage: {stage}")
        index=STAGES.index(stage)
        gate=f"G{index+1}" if index < 7 else None
        if gate and self.approvals.required(gate):
            decision=self.approvals.latest_decision(execution_id,gate)
            if decision != "approved":
                status="awaiting_approval" if decision is None else "blocked"
                emit_event(self.project,execution_id,"stage_blocked",stage=stage,gate=gate,status=status)
                return {"execution_id":execution_id,"stage":stage,"status":status,"required_gate":gate}
        emit_event(self.project,execution_id,"stage_completed",stage=stage,actor=actor,output_refs=output_refs or [])
        next_stage=STAGES[index+1] if index < 7 else None
        return {"execution_id":execution_id,"stage":stage,"status":"completed","next_stage":next_stage}
