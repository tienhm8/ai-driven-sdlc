# Testing the backend (NestJS)

Commands run from the backend checkout. Details on what to run for each kind of change are in the NestJS skill's [testing reference](../../../backend/nestjs/references/testing.md); this page records how the repository's tests are actually set up so you can choose between them.

## What exists

| Check | Command | What it covers |
|---|---|---|
| Unit and service tests | `npm test` (Jest, `rootDir: src`, files `*.spec.ts`, path aliases `@common`, `@config`, `@module` mapped in the Jest config) | 33 spec files beside the code. At the reference revision, 27 of them contain a single `toBeDefined` test that proves only that the provider can be created. Do not count such a test as coverage of behavior. |
| End-to-end | `npm run test:e2e` (`test/jest-e2e.json`, files `*.e2e-spec.ts`) | One file that boots `AppModule` and calls `GET /`. It needs the same services the app needs (databases, Redis); do not assume it can run in a bare checkout. |
| DI check | `npm run start:di-check` | Boots `AppModule` with stubs for settings, MinIO, and both Bull queues and verifies registration. It does not touch real databases, Redis, or MinIO, so a pass says nothing about those connections. |
| Transport smoke | `npm run build`, then `node test/tcp-context.smoke.cjs` (and `test/http-trace.smoke.cjs` for HTTP tracing) | Real TCP and trace-context behavior as described in `docs/tcp-context.md` and `docs/http-trace.md`. Run only when you changed that area. |

`npm run lint` uses `--fix` and rewrites files; do not use it as a read-only check.

## How to write a test that proves something

- **Service with a repository:** replace the repository at its entity token (`RepositoryProviderName(Entity.X)`) with a mock and assert the service's behavior, including the not-found and error paths. See the [repository-token example](../../../backend/nestjs/examples/testing-example.md).
- **Query scope, partition, or transaction behavior:** a mock cannot show it. Use an integration test against a disposable database, and assert both returned data and that out-of-scope data was neither read nor changed.
- **Access control:** test an allowed caller and each denial (no identity, wrong role, wrong partition or owner). See the [authentication reference](../../../backend/nestjs/references/authentication.md).
- **Queues and processors:** call the processor directly with a mocked repository or API client, and include a thrown error. Retry behavior comes from Bull options, which a unit test does not exercise.
- **Boot-time checks:** a "should be defined" test is not a behavior test. Add an assertion about what the code does.

## Reporting

State which of the four checks you ran, the commands, and the results. If the dependencies are not installed or the services are unavailable, say that the checks did not run rather than reporting a build as verification.
