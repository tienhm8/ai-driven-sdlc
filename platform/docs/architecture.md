# Architecture and control boundaries

| Component | Responsibility |
|---|---|
| Skill Loader | Resolve shared and project-local skills |
| Rule Loader | Resolve effective engineering and project rules |
| Model Router | Select model profile by task and effort |
| Tool Adapters | Discover configured tools; integrations remain isolated |
| Validators | Deterministic structural, artifact and policy checks |
| Approval Engine | Record verified human decisions against a specific review and artifact digest |
| Workflow Engine | Persist stage progress and authorize gated actions before execution |

The [framework gate policy](../../framework/governance/human-review-gates/gate-policy.md) defines G1 Requirements, G2 Design, G3 before coding, G4 before merge, G5 QA and business acceptance, G6 before production, and G7 critical incident response. Development handoff and routine Monitoring do not have gates. Critical incidents run separately from the SDLC state machine.

The local runtime records decisions and transitions in a transactional SQLite event store **outside the project workspace**. This prevents races between local callers sharing that store; it does not make the audit log immutable or tamper-evident. Run the engine as trusted application code under a service identity that protects the state directory from repository users and AI/tool processes. Do not reuse old JSONL entries as approval evidence: they lack the verified role and artifact binding now required.

An external integration must authenticate callers, resolve roles, and derive canonical targets, authors and artifact/review-context digests from trusted metadata. The engine does not merge PRs, deploy, or run incident actions. A CI/CD or repository adapter must enforce authorization for the exact artifact, review package and target, and claim it at the action boundary so exception expiry is checked at the actual start. It must verify results and correlate them to that specific claim. A terminal failure means the provider can no longer act on the old request and either made no changes or has verified rollback. The adapter also verifies the provenance connecting the G4 merge result to the G5 candidate before G6. Never treat raw caller inputs as verified evidence, or a historical authorization event as a reusable credential. The local core alone is not a production integration.

See [workflow usage](../workflow-engine/README.md) and [approval rules](../approval-engine/README.md).
