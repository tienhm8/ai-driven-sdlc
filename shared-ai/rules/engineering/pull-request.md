# Rules: pull request

Use with [git-workflow.md](git-workflow.md). The template is [pull-request-template.md](../../../framework/05-code-review/templates/pull-request-template.md).

1. Open a PR only from a dedicated branch for one Task. The title is `<TASK-ID>: <short summary>`. Fill every required section of the template. A section that does not apply says "No" with a short reason; do not delete it.
2. Open the PR as `Draft` until the author has re-read the diff and the checks listed in the template are run. Do not request review on a Draft.
3. State the problem and the Task, the acceptance criteria it meets, whether it changes behavior or only refactors, and what is intentionally out of scope.
4. Fill the impact table: data or schema, API contract, jobs or events, cache, configuration, access control or sensitive data, new dependencies. A "Yes" row says what changes and how it stays compatible with the code that is running.
5. For a change to data, an API, or a job, state the deploy order (code or migration first), any feature flag, and how to roll back.
6. Report validation evidence under [validation-evidence.md](validation-evidence.md): exact command, result, environment, and what did not run. Do not write "tested" without a command or a CI link.
7. Keep the PR small enough to review. If it is large, split it, or state why it cannot be split (generated code, mass rename).
8. Changes to rules, skills, workflows, and permission or CI configuration are a separate PR ([git-workflow.md](git-workflow.md) rule 9).
9. If AI wrote or helped write the PR, fill the AI assistance section. AI does not mark the PR Ready, approve it, or merge it; a human does after the checks pass.
10. Do not put secrets, personal data, or production data in the description, screenshots, or logs.
11. A reviewer returns a PR that is missing a required section without reviewing the code. After a fix, report which finding each new commit addresses; do not rewrite shared history.
