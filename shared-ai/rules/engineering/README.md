# Rules: engineering

- Prefer small, compatible changes; do not edit outside the scope. Check the current standards at [Standards](../../../framework/standards/README.md).
- Validate data at the boundary, enforce permissions on the server, keep errors from leaking data, and plan rollback for state-changing work.
- Add tests for changed behavior, including error cases; run the project's commands and record exactly which tests were skipped.

- [git-workflow.md](git-workflow.md): branching (Gitflow), commit message format, and git limits for AI-assisted work.
