# Backend module map

Use this index when a task touches an existing capability outside the everyday REST/CRUD path. Module names refer to the base, not modules that every new project must enable. Check imports/providers in `src/app.module.ts`, `src/config/module/config.ts`, and the owning module before assuming a capability is active. Except where noted, find the modules below in `src/modules/`.

| Task or capability | Start with | Read next |
|---|---|---|
| Feature wiring, ORM adapter, transaction | `user`, `repository`, `common-provider`, `core` | [Repository pattern](controller-service-repository.md) and [module design](module-design.md). Use PostgreSQL/MongoDB or migration guidance only for the adapter/schema being changed. |
| JWT, SSO, roles, partition membership | `auth`, `sso`, `user`, `data-partition` | [Authentication and partition](authentication.md) |
| Cross-service call | `microservice`, `internal-http` | [Transport guidance](microservice-transports.md); check both endpoints. |
| Audit, push, subscriptions, queues, schedules | `audit-log`, `notification`, `one-signal`, `topic`, `redis`, `cron-manager` (note: two cron-manager modules exist, one under `src/cron-manager/` and one under `src/modules/cron-manager/`; `DefaultModules` registers the former) | [Jobs, notifications, and scheduling](jobs-and-notifications.md) |
| Upload, object storage, imports | `file`, `minio`, `import-session`; import flows in `user`/`setting` | [Files and imports](files-and-imports.md) |
| System settings, sequences, generated codes, batch changes | `setting`, `increment`, `quy-tac-ma`, `data-process` | [Settings, sequences, and batch data](settings-and-batch-data.md) |
| Health, logging, tracing | `health`, `base-logger`, telemetry in `microservice` | [Health, logging, and tracing](health-and-observability.md) |

This is an index into the actual source and the references above. Do not load unrelated references or create a skill per module; add a focused reference only when real tasks need more than the source and the existing reference.
