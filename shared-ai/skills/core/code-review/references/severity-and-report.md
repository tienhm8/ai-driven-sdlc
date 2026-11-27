# Severity and report

## Common severity cases

| Severity | Common cases |
|---|---|
| Critical | Data loss or corruption; exploitable security vulnerability |
| High | Logic wrong against the acceptance criteria; race condition corrupting data; acceptance criterion with no test; migration that cannot be rolled back |
| Medium | Wrong layer; N+1 or missing index on still-small data; missing error handling in a secondary branch; missing log or alert |
| Low | Naming, minor structure |
| Info | Suggestion or point to watch, not a defect |

Questions and suggestions carry no severity.

## Recommendation (the AI proposes; the human decides G4)

- **Request Changes**: a Critical or High finding remains.
- **Comment**: Medium findings remain; state the condition (fix in this change, or a Task with an owner and date).
- **Approve** (proposal only): only Low or Info findings remain, and required checks passed on the current head SHA.
- **Blocked**: the entry check failed or a required input is missing.

## Report contents

- The change as the reviewer understands it: problem, behavior change or refactor, impact, risk level.
- Missing items in the PR description.
- Findings by severity, then questions and suggestions.
- Test assessment: acceptance criteria with and without evidence; source of gate results (CI or local run).
- Groups not applicable, with reasons; whether a security review was triggered.
- What was not reviewed.
- Good points, the recommendation, and the pending gate G4.
