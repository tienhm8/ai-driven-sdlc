# Backend module map

Use this index when a task touches an existing capability outside the everyday REST/CRUD path. Module names refer to the base, not modules that every new project must enable. Check imports/providers in `src/app.module.ts`, `src/config/module/config.ts`, and the owning module before assuming a capability is active. Except where noted, find the modules below in `src/modules/`.

| Task or capability | Start with | Read or verify next |
|---|---|---|
| Feature wiring, ORM adapter, transaction | `user`, `repository`, `common-provider`, `core` | [Repository pattern](controller-service-repository.md) and [module design](module-design.md). Use PostgreSQL/MongoDB or migration guidance only for the adapter/schema being changed. |
| JWT, SSO, roles, partition membership | `auth`, `sso`, `user`, `data-partition` | [Authentication and partition](authentication.md), then the affected guard, service, and query. |
| Cross-service call | `microservice`, `internal-http` | [Transport guidance](microservice-transports.md); check both endpoints. |
| Audit, push, subscriptions, queues, schedules | `audit-log`, `notification`, `one-signal`, `topic`, `redis`, `cron-manager`; check which cron module is registered | Inspect the relevant processor, schedule, or leader check. Bull uses Redis; a queue is not a cache. Verify retry/idempotency, concurrency, and audit or notification behavior only where relevant. |
| Upload, object storage, imports | `file`, `minio`, `import-session`; import flows in `user`/`setting` | Check allowed file types, access policy, storage and import state, and the failure/retry contract. |
| System settings, sequences, code generation, batch changes | `setting`, `increment`, `quy-tac-ma`, `data-process` | Check ownership, data scope, uniqueness/concurrency and the failure path before changing writes. |
| Health, logging, tracing | `health`, `base-logger`, telemetry in `microservice` | Check what is wired. The reference base has a `BaseLoggerModule` source file but its registration is commented out. For HTTP/TCP tracing, inspect `docs/http-trace.md` or `docs/tcp-context.md` as applicable; keep sensitive data out of telemetry. |

This is an index into the actual source and existing skills. Do not load unrelated module guides or create a skill per module; add a focused reference only when real tasks need more than the source and this index.
