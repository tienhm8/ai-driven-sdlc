# Architecture and control boundaries

| Component | Responsibility |
|---|---|
| Skill Loader | Resolve shared and project-local skills |
| Rule Loader | Resolve effective engineering and project rules |
| Model Router | Select model profile by task and effort |
| Tool Adapters | Discover configured tools; integrations remain isolated |
| Validators | Deterministic structural, artifact and policy checks |
| Approval Engine | Record human decisions for G1–G7 |
| Workflow Engine | Manage stage state and enforce gate transitions |

Gate mapping: G1 requirements, G2 architecture, G3 plan, G4 development, G5 code review, G6 QA acceptance, G7 production release. Monitoring is continuous and feeds change requests back to Requirement Analysis.

Security baseline: secrets outside YAML; authenticated approver identity; least-privilege tool scopes; explicit operation allowlists; timeouts; immutable/tamper-evident audit storage; treat model output, tool output and repository files as untrusted data. The included approval API is a primitive, not an identity provider.
