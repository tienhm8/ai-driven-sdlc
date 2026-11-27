# Backend pipeline — aisoft-backend

Open this for GitLab CI work on the NestJS base. Observations refer to revision `5ebe06c7`; recheck the target checkout and effective GitLab configuration before applying them.

## Current pipeline

- `.gitlab-ci.yml` declares `build`, `test`, and `release`. There is **no test or lint job** in the file. A stage declaration, a release, or an image build does not establish that tests ran.
- Push jobs for `develop`, `integration/*`, and `release/*` build and push images; tag jobs publish images and prepare a GitLab release. None is an MR-only validation job. A GitLab release is not evidence of a runtime deployment.
- The Dockerfile uses Node 24, `npm ci` with a BuildKit secret for the private npm dependency, and `npm run build-bundle`. `npm run build` runs `nest build`; passing it does not validate the bundle or the image. Do not reuse the publishing job as an MR build check.

## When a ticket authorizes validation jobs

1. Select an approved Node 24 runner/image and install with `npm ci` from the committed `package-lock.json`. Verify access to the approved package registry from the intended pipeline context. Do not give untrusted MR code access to protected credentials, host Docker, or a deploy runner. If registry access is unavailable, report the block instead of bypassing access controls.
2. Define an MR validation path with no registry push or release action. Use `npm run build` for the application compile check. If the bundle is required, separately validate `npm run build-bundle` or the actual builder target without publishing, on an approved runner that supports its prerequisites.
3. Use Jest for the relevant tests (`npm test -- --ci --runInBand`, optionally with the affected spec path). Use `npm run start:di-check` for provider/module changes, in a suitable environment. It checks wiring with stubs, not live dependency behavior. Run `npm run test:e2e` only with approved, isolated test services and fixtures; never reuse a production environment. See the [NestJS testing reference](../../../backend/nestjs/references/testing.md) for coverage and smoke checks.
4. `npm run lint` has `--fix`; do not use it as the validation command. Verify a non-fixing invocation with the checked-in ESLint version and config (for example, the repo's target globs without `--fix`). Keep formatter checks non-writing as well.
5. Capture the real exit status, job link and report. If an approved Jest reporter is configured, publish its generated XML; do not declare a JUnit path before a reporter exists. When prerequisites are missing, say what could not run; do not report a required check as passed. See [G4 evidence](g4-evidence.md).
