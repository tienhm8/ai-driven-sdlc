# Verification

Open to choose checks or prepare evidence. Run from the `base-web` checkout with Node 22 and Yarn Classic using the locked dependencies (`yarn install --frozen-lockfile`).

| Change | Check |
|---|---|
| Any code change | `yarn build` (`max build`). A build proves the app compiles, not that behavior is correct. |
| Types | Targeted type check on the files you changed, if the project's TypeScript setup supports it; report errors separately when they come from unrelated template files. |
| Lint | Run the specific tool (`eslint <files>`, `stylelint <files>`, `prettier -c <files>`) so you control writes. The aggregate `yarn lint` runs `max setup` and its prettier/style steps write files; `lint:fix` also fixes. Do not call either a read-only check. |
| Behavior | A local smoke test of the changed flow in a browser: the happy path, an empty list, a failed request, and any permission case you touched. Record the steps. |
| Routes/menu/access | Exercise a direct load, refresh, and a user without the permission. |

Notes:

- `src/e2e/baseLayout.e2e.js` is browser scaffolding; the manifest has no test runner or script for it, and CI does not run it. Do not report it as an existing gate or as having run.
- Never run the deploy, rsync, or sourcemap-upload scripts to verify a change.
- Docker builds currently copy `package.json` without `yarn.lock` before installing, so an image can resolve different dependencies than the checkout. Mention this if the task depends on image behavior.
- Report which commands ran, which failed, and which were skipped and why. State plainly when a check was not exercised.
