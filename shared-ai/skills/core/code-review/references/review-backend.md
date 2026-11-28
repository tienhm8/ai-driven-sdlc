# Backend review checklist (NestJS, `aisoft-backend`)

Use for a diff in the backend. Check only the items the diff touches. Detail for each is in the NestJS skill.

## Wiring and layering
- The new or changed repository is bound with `RepositoryProvider(Entity.X, Impl)` and injected with `@InjectRepository(Entity.X)`, and the bound class is the adapter that is actually active. A SQL or Mongo file that is not bound does nothing. ([repository pattern](../../../backend/nestjs/references/controller-service-repository.md))
- The controller holds no business rules or ORM calls; the service owns the use case and transaction boundary; providers are exported only if another module needs them.
- A provider change comes with a DI check (`npm run start:di-check`) or a focused binding test.

## Access and data scope
- Every new endpoint declares its guards (`@Authorization()` or the intended alternative). A route with no guard is public; confirm that is intended. `SystemRoleGuard` allows a route that declares no roles, so a role restriction must be declared explicitly.
- Queries and writes respect the resource's owner, role, and data-partition scope, including counts, lists, updates, and deletes. A guard alone does not scope a query. ([authentication and partition](../../../backend/nestjs/references/authentication.md))
- Internal endpoints (`@InternalController`) are service-to-service and must not be reachable as a user-facing path.

## Input, output, errors
- Input is validated by a DTO with the project's pipe settings; unknown fields are handled by policy. Raw entities, credentials, and storage keys are not returned.
- Known failures map to the project's error codes; unexpected failures do not leak stack traces or database errors. ([DTO validation](../../../backend/nestjs/references/dto-validation.md), [exceptions](../../../backend/nestjs/references/exception-handling.md))
- Logs and queue payloads contain no tokens, passwords, or personal data.

## Logging (Observer)
- Every state-changing handler has `@Operation({ action })`; a job, processor, cron, or gRPC/TCP handler that writes data opens `operation.run`. Read-only endpoints have none, and internal steps do not open extra operations. ([logging with Observer](../../../backend/nestjs/references/logging-observer.md))
- New code adds no Nest `Logger`, `console.*`, or separate Pino instance. Services inject `TelemetryFacade` with `@Observer({ module, service })`, both names set.
- Action, business event, and span names follow the convention (`customer.activate`, `customer.activated`) and contain no IDs or user input.
- `data`, `message`, `actor`, and span attributes carry IDs, not personal data or secrets; `actorResolver` returns only `{ id }`. Redaction paths are static.
- No `catch` that only logs and rethrows; operation or trace IDs are not passed as method parameters; builders are not stored in shared state.
- A provider that gained `@Observer` has a passing DI check and its spec still builds.

## Persistence, jobs, and files
- A multi-step write uses the module's transaction at the use-case boundary and aborts on failure; a transaction is not assumed to span Redis or remote calls.
- A queue job is safe to run twice; the producer and processor use the same job name; retry settings are intentional. Scheduled jobs use the cron-leader guard. ([jobs](../../../backend/nestjs/references/jobs-and-notifications.md))
- Uploads: type checks, size bounds, and `scope` handling are preserved; a delete also considers the stored object. ([files](../../../backend/nestjs/references/files-and-imports.md))
- Bulk or destructive data changes have a stated scope, a backup, and a rollback; they were not run against real data. ([batch data](../../../backend/nestjs/references/settings-and-batch-data.md))

## Evidence
- The tests cover the changed behavior and a failure path, not only "should be defined". The reported commands match what ran. ([testing](../../testing/references/backend-nestjs.md))
