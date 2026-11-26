# Frontend pipeline — base-web

Open this for GitLab CI work on the Umi Max base. Observations refer to `basev4` revision `d3d0e0b1`; recheck the target checkout and effective GitLab configuration before applying them.

## Current pipeline

- `.gitlab-ci.yml` has a `docker-build` job that runs when the branch matches `/production/` and `Dockerfile` exists. It builds **and pushes** an image. It is not an MR-only validation job. There is no dedicated MR build, lint, or test job in the file.
- The Dockerfile uses Node 22 and runs `yarn build`, but copies only `package.json` before `yarn install`. Image dependency resolution can therefore differ from `yarn.lock` until a separate Dockerfile change fixes it.
- There is no Vitest or Playwright script or runner in the base at this revision. The existing browser scaffold is not proof of automated coverage.

## When a ticket authorizes validation jobs

1. Use Node 22 and Yarn Classic. Install with `yarn install --frozen-lockfile`, and use `yarn build` for the Umi Max compile check. Supply only the configuration the build needs, using approved non-production values. Do not use the existing publish job, rsync, or sourcemap uploads to check an MR.
2. Verify non-fixing lint and format commands with the checked-in tool versions and configuration before making either required. The aggregate `yarn lint` runs `max setup` and writing steps, and `lint:fix` writes. If generated Umi files are necessary, make setup explicit and separate from the non-fixing check.
3. **After a separate ticket provisions the runners**, use `yarn test` for Vitest unit/component tests and `yarn e2e` for Playwright browser tests. Verify that Vitest resolves the aliases and generated Umi modules the tests actually need; for Playwright, verify browser dependencies, app startup, and isolated test data. Do not copy Next.js config, environment variables, or Amplify settings from the sample repository. See the [FE testing reference](../../../core/testing/references/frontend-umi-max.md).
4. Until the runners and tests exist, record automated tests as not run. Capture build or manual smoke evidence only for what was exercised; it cannot silently replace a required automated check. When a runner generates JUnit, use its actual output path and preserve its exit status. See [G4 evidence](g4-evidence.md).
