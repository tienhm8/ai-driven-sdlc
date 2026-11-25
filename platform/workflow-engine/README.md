# Workflow Engine

Set up `WorkflowEngine(project, state_dir=protected_path, verify_identity=trusted_verifier, can_approve=scoped_role_check)`. Use a protected state directory outside the project and start a new execution for schema v3. See [Architecture](../docs/architecture.md) for state protection, audit and adapter responsibilities, and the [Framework gate policy](../../framework/governance/human-review-gates/gate-policy.md) for gate conditions and roles.

## Run a local G1 example

Run this from the repository root with Python 3.10+ and the [platform dependencies](../scripts/README.md#cách-chạy-script). The temporary project and state are cleaned up on exit. The identity, role check and evidence below are **test fixtures**, not production authentication or approval evidence.

```bash
PYTHONPATH=platform/src python3 -B - <<'PY'
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory

from ai_sdlc_platform.approval_engine import VerifiedApprover
from ai_sdlc_platform.workflow_engine import WorkflowEngine

with TemporaryDirectory() as directory:
    root = Path(directory)
    project = (root / "demo-project").resolve()
    project.mkdir()
    stage, gate, role = "01-requirement-analysis", "G1", "product_owner"

    # The demo adapter owns the fixture credentials, artifact and review package.
    credentials = {"demo-token": VerifiedApprover("demo-po", frozenset({role}), True)}
    artifact_ref = "demo:requirements-v1"
    evidence_ref = "demo:g1-checklist-v1"
    artifact_digest = sha256(b"Example requirement: users can view their orders.").hexdigest()

    def context_digest():
        package = f"{artifact_ref}:{artifact_digest}\n{evidence_ref}"
        return sha256(package.encode("utf-8")).hexdigest()

    def can_approve(identity, requested_role, scope):
        return (identity.subject == "demo-po" and requested_role == role
                and scope.project == project and scope.gate == gate)

    engine = WorkflowEngine(project, state_dir=root / "state",
                            verify_identity=credentials.get, can_approve=can_approve)
    execution_id = engine.start()["execution_id"]
    review = engine.request_review(
        execution_id, gate, artifact_sha256=artifact_digest,
        review_context_sha256=context_digest(), author_ids=["demo-author"],
        actor="demo-requester", artifact_refs=[artifact_ref],
    )
    engine.approvals.approve(
        execution_id, gate, "demo-token", "approved", role=role,
        review_id=review["event_id"], artifact_sha256=artifact_digest,
        evidence_refs=[evidence_ref],
    )
    transition = engine.complete_stage(
        execution_id, stage, output_refs=[artifact_ref],
        review_id=review["event_id"], artifact_sha256=artifact_digest,
        review_context_sha256=context_digest(),
    )
    print(transition["next_stage"])
PY
```

Expected output: `02-system-design`. The adapter supplies verified identity, scoped roles, canonical authors, digests and inspectable references. The engine checks the active stage, review and digest bindings, eligible approver, self-approval restriction and gate decision. It does not fetch the artifact or evaluate the checklist.

## API usage

For action results at G4/G6, pass `verify_action_result=trusted_result_lookup` to `WorkflowEngine(...)`. For build provenance at G5, pass `verify_build_provenance=trusted_build_lookup`. Neither callback is needed for G1–G3 or a standalone G7 incident workflow.

1. `start()` starts at `01-requirement-analysis`. `complete_stage(execution_id, active_stage, ...)` advances one stage; missing, out-of-order and already completed stages are refused. Development handoff does not require a gate.
2. Call `request_review(execution_id, gate, artifact_sha256=..., review_context_sha256=..., author_ids=[...], actor=..., artifact_refs=[...])`. The adapter must derive the digest of the immutable artifact and a separate digest of the **review package**, including material plan/config/evidence changes. Changing either digest opens a new review and invalidates prior decisions; repeating an identical request returns the existing review. Use immutable references that let reviewers inspect the package. For an action gate, also supply `target`: G4 uses `repository`, `pull_request`, and `base_ref`; G6 uses a canonical `environment`; G7 uses `incident_ref` matching the incident execution. Use stable IDs where labels alone are ambiguous.
3. Record a decision through `engine.approvals.approve(...)` using the review's `event_id` as `review_id` and its artifact digest. The configured [scoped role check](../approval-engine/README.md) must allow that decision. To complete G1–G3 or G5, pass `review_id`, the current `artifact_sha256` and a freshly derived `review_context_sha256`; if the package changed, open a new review instead. See the [G5 policy](../../framework/governance/human-review-gates/G5-qa-approval.md) for its two required decisions.
4. **Before** merge, deploy or a critical incident action, call `authorize_action(execution_id, gate, artifact_sha256=..., review_id=..., review_context_sha256=..., target=...)`. Immediately before dispatch, call `check_action_start(execution_id, gate, authorization_id=..., artifact_sha256=..., review_context_sha256=..., target=...)` using the current request. It checks `expires_at` for an exception and records a single-use start claim. Do not enqueue actions after claiming them; if execution is deferred elsewhere, the trusted adapter must enforce the deadline at the actual action boundary. The engine never calls providers.
5. After a G4 or G6 action, call `complete_stage(..., artifact_sha256=..., action_result_ref=...)`. `verify_action_result(gate, ref)` must retrieve trusted evidence for the exact authorization, start claim (`start_event_id`), artifact and target. Success advances the stage; G4 also records the resulting `merge_commit`. A terminal `failed_no_changes` or verified G6 `rolled_back` produces `action_failed`, leaves the stage unchanged and requires a new review before a retry. Only provide a terminal failure once the provider can no longer perform the old action and the target is safe to retry. For an unclaimed authorization, only `failed_no_changes` with no start claim can close it. Missing, mismatched or inconclusive results remain blocking. Rollback itself remains external to the engine.
6. For a G5 review, supply `provenance_ref`. `verify_build_provenance(ref)` must return trusted `VerifiedBuildProvenance` linking the candidate's digest to the recorded repository and merge commit at G4. G6 must use the same candidate cleared by the current G5. From Deployment, use `return_to_qa(execution_id, reason=..., actor=...)` for a rebuild from the same source. From QA or Deployment, use `return_to_development(...)` for a source fix requiring a new G4 merge. Both transitions record the reason, invalidate the affected reviews and require fresh approvals. Neither is available while a production authorization has no terminal result.
7. Monitoring handoff has no gate. Start a separate critical incident execution with `start_critical_incident(incident_ref=...)` and use G7 for review, authorization and a single start claim on the response plan. If an exception-backed G7 authorization expires before it is claimed, `request_review` records `action_expired` and opens a fresh review in the same incident, even for the same plan. When both digests are unchanged, the review metadata must still match the previous request. Previous decisions do not carry over. A claimed action is not reset on expiry. The expiry event uses the existing schema-v3 `reset_gates` marker, so v3 readers also see the old attempt as closed. G7 does not advance any SDLC execution.

## Regression tests

Run from the repository root:

```bash
PYTHONPATH=platform/src python3 -B -m unittest discover -s platform/tests -v
```
