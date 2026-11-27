# Rules: git workflow

1. One Task maps to one branch or one independent change unit. Work on a dedicated branch; never commit directly to long-lived branches (`master`, `develop`) or `release/*` branches.
2. Branching follows Gitflow (nvie). Working branches are named `<type>/<TASK-ID>-<short-description>`, where type is `feature`, `fix`, `refactor`, `docs`, or `chore`. They branch from `develop` and merge back into `develop`. Exception: a `fix` for a bug in an open release branches from `release/*` and merges back into it. Example: `fix/PRJ-12-login-timeout`.
   - `release/<X.Y.0>`: branches from `develop` at sprint close, is deployed to Staging, accepts only bug fixes, and closes by merging into `master` (tagged `vX.Y.0`) and back into `develop`.
   - `hotfix/<X.Y.Z>`: branches from `master` to fix a critical Production bug, merges into `master` (tagged `vX.Y.Z`) and into `develop` (or the open `release/*`).
   Merge these branches with `--no-ff`. Tags use `vMAJOR.MINOR.PATCH`: a release bumps MINOR, a hotfix bumps PATCH, a breaking change bumps MAJOR.
3. Commit messages **must** follow the Angular convention. The first line is `type(scope?): subject`, where `type` is one of `build`, `ci`, `chore`, `docs`, `feat`, `fix`, `perf`, `refactor`, `revert`, `style`, `test`. The body states the `TASK-ID`. Each commit contains only files within the Task scope. Do not add a `Co-Authored-By` line or any AI attribution line to commit messages.
4. After committing, report to the reviewer: the branch, the short hash, the **full message** (first line and body) of each commit just created, and each commit's file list (`git show --stat --format=full`). Do not report only "committed".
5. `master`, `develop`, and open `release/*` branches are protected: they accept changes only through a PR with review and passing checks. AI does not merge into these branches and does not create release tags. A human merges and tags after approval and passing checks (or a time-limited waiver).
6. No force-push and no rewriting of shared branch history.
7. Do not use `--no-verify` or equivalent flags to bypass hooks or check gates.
8. Do not commit secrets, `.env*` files, or production data.
9. Changes to rules, skills, workflows, and permission or CI configuration go in a separate Task and PR, not bundled into a feature Task.
10. The PR states the `TASK-ID` and links or includes the handoff report. The PR does not copy sections already in the handoff report.
