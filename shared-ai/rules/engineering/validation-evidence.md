# Rules: validation evidence

- Record the exact command, its result (passed, failed, skipped), and the environment for every check you report. Say which checks did not run and why.
- Do not report a check as passed when it was skipped or could not run, and do not weaken, disable, or delete a test to obtain a pass.
- A command that writes files (a formatter, `--fix`, a setup step) is not a read-only check. Use a read-only form, or report that the command changed files.
- Verify with disposable data and local services. Do not deploy, upload, or run destructive or bulk data operations against shared or real environments to verify a change.
- A green build or CI run, or an AI review, is evidence for what it exercised; it does not replace a required human approval.
