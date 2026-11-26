# Architecture and control boundaries

| Component | Responsibility |
|---|---|
| Skill Loader | Resolve shared and project-local skills |
| Rule Loader | Resolve effective engineering and project rules |
| Model Router | Select model profile by task and effort |
| Tool Adapters | Discover configured tools; integrations remain isolated |
| Validators | Check the project manifest, workspace structure, resource paths and approval policy. Artifact-content and traceability checks are not implemented. |
| Approval Engine | Record verified human decisions against a specific review and artifact digest |
| Workflow Engine | Persist stage progress and authorize gated actions before execution |

The [Framework gate policy](../../framework/governance/human-review-gates/gate-policy.md) is the reference for G1–G7 conditions, approver roles and exceptions. This page covers the platform trust boundary and the responsibilities of the caller and engine.

## State and audit

The local runtime records review requests, decisions, transitions and other governance events as they occur in a transactional SQLite store **outside the project workspace**. Transactions serialize writes by local callers sharing the store; the log is not immutable or tamper-evident. Run the engine as trusted application code under a service identity and protect the state directory from repository users and AI/tool processes. Keep the directory stable across restarts. State is isolated by resolved project path; the database and its SQLite sidecar paths must not redirect through symlinks. Keep older SQLite executions and JSONL records for audit, not as approval evidence for current schema-v3 executions.

## Adapter responsibilities

An external integration must authenticate callers, resolve roles, and derive canonical targets, authors and artifact/review-context digests from trusted metadata. The engine does not merge PRs, deploy, or run incident actions. A CI/CD or repository adapter must enforce authorization for the exact artifact, review package and target, and claim it at the action boundary so exception expiry is checked at the actual start. It must verify results and correlate them to that specific claim. A terminal failure means the provider can no longer act on the old request and either made no changes or has verified rollback. The adapter also verifies the provenance connecting the G4 merge result to the G5 candidate before G6. Never treat raw caller inputs as verified evidence, or a historical authorization event as a reusable credential. The local core alone is not a production integration.

See [workflow usage](../workflow-engine/README.md) and [approval rules](../approval-engine/README.md).
