# Testing the frontend (Umi Max)

Commands run from the `base-web` checkout with Node 22 and Yarn Classic.

## What exists

At the `basev4` reference revision (`d3d0e0b1`), there are no unit specs or test runner scripts in `package.json`. `src/e2e/baseLayout.e2e.js` is browser scaffolding without a configured runner; the checked-in GitLab pipeline does not run it. Do not report it as an automated check or a gate.

The evidence available for a frontend change is therefore:

| Check | How | What it shows |
|---|---|---|
| Build | `yarn build` (`max build`) | The app compiles. It does not show the behavior is correct. |
| Targeted lint | `eslint <files>`, `stylelint <files>`, `prettier -c <files>` on the files you changed | Style and some errors. Avoid the aggregate `yarn lint` and `lint:fix`, which write files. |
| Manual smoke test | Run the app locally and exercise the changed flow | Behavior, only for the steps you actually performed. |

See the Umi Max skill's [verification reference](../../../frontend/umi-max/references/verification.md) for the full table and cautions.

## How to run a useful manual check

Record the steps so a reviewer can repeat them. For a list screen: load it, filter, sort, change page, create, edit, delete, and open it with an empty result and with a failing request. For a route or access change: load the URL directly, refresh, and sign in as a user without the permission. Report each step as done or not done.

## Approved direction, not yet installed

- **Vitest** for unit and component tests (`yarn test`, wrapping `vitest run`, once provisioned). Start with pure logic, then configure jsdom and the actual Umi alias and generated module dependencies required by component tests. Use mocks for external services, and verify missing browser APIs only where the components need them.
- **Playwright** for browser E2E (`yarn e2e`, wrapping `playwright test`, once provisioned). Verify browser setup, app startup, URL, isolated fixtures, and at least one real checked-in test before requiring the job. Do not assume the legacy scaffold will run unchanged.
- `1group-fe` (`b2f6a017`) provides a Vitest config and setup (`jsdom`, cleanup, browser API mocks), a Playwright dependency and script, and checked-in specs under `e2e/`. No `playwright.config.*` is checked in at that revision, and its GitLab pipeline does not run the suite. Use these as references, not a working E2E configuration for Umi: reuse neither Next.js-specific setup nor unverified alias assumptions. The runner/config/script installation in `base-web` is a separate ticket. See [frontend CI](../../../devops/gitlab-ci/references/frontend-pipeline.md) for adding jobs after it lands.

## Reporting

Report the commands and manual steps you actually ran. For a checkout without the runners, mark automated checks `skipped/not available` and state which behavior is still unverified, even if the build passes. Do not mark a required check as passed or substitute a smoke check for it without the applicable approval process.
