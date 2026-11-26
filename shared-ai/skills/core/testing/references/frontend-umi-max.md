# Testing the frontend (Umi Max)

Commands run from the `base-web` checkout with Node 22 and Yarn Classic.

## What exists

There is **no automated test suite** at the reference revision: no `*.spec.*` or `*.test.*` files, and no test runner or test script in `package.json`. `src/e2e/baseLayout.e2e.js` is browser scaffolding that nothing runs, and CI does not run it. Do not report it as a gate, and do not say a test passed.

The evidence available for a frontend change is therefore:

| Check | How | What it shows |
|---|---|---|
| Build | `yarn build` (`max build`) | The app compiles. It does not show the behavior is correct. |
| Targeted lint | `eslint <files>`, `stylelint <files>`, `prettier -c <files>` on the files you changed | Style and some errors. Avoid the aggregate `yarn lint` and `lint:fix`, which write files. |
| Manual smoke test | Run the app locally and exercise the changed flow | Behavior, only for the steps you actually performed. |

See the Umi Max skill's [verification reference](../../../frontend/umi-max/references/verification.md) for the full table and cautions.

## How to run a useful manual check

Record the steps so a reviewer can repeat them. For a list screen: load it, filter, sort, change page, create, edit, delete, and open it with an empty result and with a failing request. For a route or access change: load the URL directly, refresh, and sign in as a user without the permission. Report each step as done or not done.

## Reporting

Say plainly: "No automated tests exist for this repository; verification was `yarn build` and a manual smoke test of <flow>," and list what you did not exercise. If you add a test runner to a feature branch, that is a separate, approved change and not part of verifying an unrelated task.
