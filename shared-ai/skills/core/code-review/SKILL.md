---
name: code-review
description: "Review a diff before merge for behavior, data, and access-control defects, with evidence. Use for any pull request or change set; stack checklists for the backend and frontend are in the references."
---

# Code review

**Wrong behavior: do not recommend approval. Ugly code: comment, do not block.**

## Entry check: stop and return to the author if missing

Read the PR description first. Do not review the code and state what is missing if any of these is absent:

- Task, acceptance criteria, and what problem the change solves.
- Whether it changes behavior or only refactors, and what is out of scope.
- What it affects: data or schema, API contract, jobs or events, cache, configuration, access control.
- How it was tested: command, result, or CI link, on the current head SHA.
- For data, API, or job changes: deploy order and rollback.
- Size within the project threshold; if over, ask to split unless the description gives a reason (generated code, mass rename).

The expected description is the [PR template](../../../../framework/05-code-review/templates/pull-request-template.md). A failed required check or CI is a reason not to recommend approval.

## Procedure

1. From the description, form a hypothesis of what the code must do. Then read the requirement, the diff, **and the call sites, schema, config, and existing tests outside the diff**. Review against intent, not only the lines. Do not conclude on concurrency, performance, or architecture from the diff alone.
2. Compare the Task with the diff. List changed files and modules; flag files outside the stated scope, tests deleted or weakened, columns or tables dropped, and dependencies added without a reason. A change described as "refactor only" that changes conditions, return values, or side-effect order is a finding.
3. Review in this order and load only the checklist for the group you reach: [correctness, tests, placement](references/correctness.md); [concurrency, performance, operability](references/runtime.md); [security](references/security.md); then maintainability. Do not spend the review on style a formatter or linter handles. A group that does not apply gets a stated reason.
4. Report each finding with its location (`file:line`), the concrete input or state that triggers it, the wrong result, the severity, and a fix direction. Mark it verified (reproduced or traced through code) or a question. If you cannot build a failure scenario, report a question, not a defect. Merge findings with one cause; cap Low findings so important ones are not buried. Address the code, not the author, and name specific good points.
5. Check that the change has tests or other evidence for the behavior it alters, including the failure path, and that the reported checks match what ran. See the `testing` skill. Passing tests do not prove the code is correct.
6. State what you did not review (files, behaviors, environments).
7. A reviewer does not edit the code under review unless asked. Review by AI or a green CI run does not replace the approval of the authorized human reviewer (gate G4); the AI proposes findings and a recommendation, not approval.

Severity uses the shared scale (Critical, High, Medium, Low, Info) in the [code review stage](../../../../framework/05-code-review/human-review.md). Common cases and recommendation rules are in [severity and report](references/severity-and-report.md). Illustrations of common bug patterns are in [examples](references/examples.md).

## Load a checklist for the repository under review

| Diff touches | Open |
|---|---|
| Backend (`aisoft-backend`, NestJS) | [Backend checklist](references/review-backend.md) |
| Frontend (`base-web`, Umi Max) | [Frontend checklist](references/review-frontend.md) |
| Authentication or authorization changes | Also the `authentication` or `authorization` skill |
| Untrusted input, files, or a security-sensitive feature | Also the `owasp` skill; do not duplicate a security review inside this skill |
