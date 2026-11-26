---
name: code-review
description: "Review a diff before merge for behavior, data, and access-control defects, with evidence. Use for any pull request or change set; stack checklists for the backend and frontend are in the references."
---

# Code review

1. Read the requirement, the diff, and the call sites of everything the diff changes. Review the change against the intent, not only the lines.
2. Prioritize, in order: behavior that is wrong; data loss or corruption; broken access control or exposed data; then maintainability. Do not spend the review on style that a formatter handles.
3. Report each finding with its location, the condition that triggers it, the impact, and a suggested fix. Mark whether it is verified (reproduced or traced through code) or a question. Do not report speculation as a defect.
4. Check that the change has tests or other evidence for the behavior it alters, including the failure path, and that the reported checks match what ran. See the `testing` skill.
5. State what you did not review (files, behaviors, environments) so the author does not assume coverage.
6. A reviewer does not edit the code under review unless asked. Review by AI or a green CI run does not replace the approval decision of the authorized human reviewer (gate G4); the AI proposes findings and a recommendation, not approval.

## Load a checklist for the repository under review

| Diff touches | Open |
|---|---|
| Backend (`aisoft-backend`, NestJS) | [Backend checklist](references/review-backend.md) |
| Frontend (`base-web`, Umi Max) | [Frontend checklist](references/review-frontend.md) |
| Authentication or authorization changes | Also the `authentication` or `authorization` skill |
| Untrusted input, files, or a security-sensitive feature | Also the `owasp` skill |
