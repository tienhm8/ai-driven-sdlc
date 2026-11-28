---
name: nestjs
description: "Implement, test, or review NestJS 11.2.7 changes on aisoft-backend or a project derived from it. Covers modules, REST, DTOs, DI, repositories, and on-demand guidance for auth, data partition, gRPC, and TCP."
metadata:
  nestjs-version: "11.2.7"
---

# NestJS 11.2.7

## Everyday backend changes

1. Check the approved task, the NestJS version in the lockfile, and the nearest working module. If the version differs, report the mismatch and verify compatibility before using version-specific guidance; do not upgrade dependencies as part of the task.
2. Follow **controller → service → repository**. The controller owns the HTTP boundary, the service owns the use case and transaction boundary, and the repository owns persistence. Keep DTOs separate from persistence entities and preserve the existing response and error contract. Every state-changing handler carries `@Operation`; services log through an `@Observer`-injected `TelemetryFacade`, not the Nest `Logger` ([logging with Observer](references/logging-observer.md)).
3. Reuse `RepositoryProvider(Entity.X, Implementation)` and `@InjectRepository(Entity.X)` with the repository interface. Check the adapter actually bound by the module; a SQL or Mongo file alone is not evidence that it is active. Use the matching transaction provider only when the use case needs it. Export only providers used by other modules.
4. Validate input at the boundary. Preserve resource-level authorization and apply the existing data-partition policy where relevant; a guard alone does not scope a repository query. Do not expose raw entities, credentials, or database errors.
5. Run checks appropriate to the diff: `npm run build`, focused Jest via `npm test -- --runInBand <spec-path>`, `npm run start:di-check` for provider changes, and `npm run test:e2e` when HTTP behavior changes and the test environment is available. Report checks run, failures, and gaps. The base's `npm run lint` modifies files; do not use it as a read-only check.

## Load more only when the task needs it

For a small change following an existing feature, start here and in that feature. Use the table to open only the references that answer a question raised by the diff; do not read every linked file.

| Task | Open when needed |
|---|---|
| Add a module, change provider ownership, or wire DI | [Module design](references/module-design.md), [dependency injection](references/dependency-injection.md), [UserModule example](examples/module-example.md) |
| Add or change a repository, query, or transaction | [Controller, service, and repository](references/controller-service-repository.md); select the persistence skill only for adapter-specific work |
| Change request validation or error behavior | [DTO validation](references/dto-validation.md) or [exception handling](references/exception-handling.md), as applicable |
| Change JWT, Keycloak SSO, role checks, or data-partition scope | [Authentication and data partition](references/authentication.md); add `authentication` or `authorization` for changes to those mechanisms |
| Change gRPC, custom TCP, or internal HTTP | [Microservice transports](references/microservice-transports.md); add `microservices` if service boundaries, ownership, or a cross-service contract change |
| Write tests or need a DI mock | [Testing](references/testing.md) or [repository-token Jest example](examples/testing-example.md) |
| Change a Bull queue or processor, push notification, topic subscription, or scheduled job | [Jobs, notifications, and scheduling](references/jobs-and-notifications.md) |
| Change file upload/download, object storage, or bulk import | [Files and imports](references/files-and-imports.md) |
| Change settings, sequences, generated codes, or a bulk data operation | [Settings, sequences, and batch data](references/settings-and-batch-data.md) |
| Add or change a log, business event, operation record, or span in feature code | [Logging with Observer](references/logging-observer.md) |
| Change health checks, application logging setup, or tracing | [Health, logging, and tracing](references/health-and-observability.md) |
| Unsure which module owns a capability | [Backend module map](references/backend-module-map.md) |
