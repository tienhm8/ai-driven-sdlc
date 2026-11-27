# Rules: sdlc

`sdlc/` is a mandatory rule group that the [rule loader protects by default](../../../platform/rule-loader/README.md), together with `core/`.

- Identify the stage from the [Framework](../../../framework/README.md). Read the stage's workflow, checklist, and human review; do not guess the gate mapping.
- Link requirement → change → test evidence → review decision; when a requirement changes, update the links.
- Under [Governance](../../../framework/governance/README.md), record the actual gate status and the approver; if approval is missing, mark the work as waiting instead of moving on.
