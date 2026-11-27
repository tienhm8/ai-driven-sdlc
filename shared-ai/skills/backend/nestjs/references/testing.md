# Testing

Select the smallest check that can verify the change. Run commands from the backend checkout with the project's Node.js version and locked dependencies.

| Change | Check |
|---|---|
| Use-case behavior or repository delegation | `npm test -- --runInBand <spec-path>`; mock the repository at its entity token. For transactional behavior, verify the failure/abort path as well as commit. |
| Module imports, exports, or providers | `npm run start:di-check` plus a focused binding test if needed. The smoke uses stubs and does not prove production connections work. |
| Database behavior | Targeted integration tests for the active adapter: scope, count/pagination, mutation, transaction/rollback as applicable. Do not treat an ORM mock as query evidence. |
| HTTP behavior | `npm run test:e2e` when the required test services and configuration are available. Initialize the same relevant pipes, guards, interceptors, and filters as the app. Check validation errors and denied access as applicable; close the app after the test. |
| RPC/context or compatibility | Use the focused tests and environment-appropriate smoke from [microservice transports](microservice-transports.md). |
| Build wiring | `npm run build`; a build is not a substitute for behavior tests. |

The base's `npm run lint` runs `--fix`; do not use it for read-only evidence. Record what passed, what failed, and what was skipped because prerequisites were unavailable.
