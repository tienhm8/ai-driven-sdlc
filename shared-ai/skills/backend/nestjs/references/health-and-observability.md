# Health, logging, and tracing

Open when changing health endpoints, logging, or tracing. Paths are relative to the backend checkout.

## Health

- `HealthService.checkLiveness` runs no dependency checks: it only shows the process answers. `checkReadiness` assembles checks for the dependencies that are configured **and** injected: MongoDB (when `mongodb.uri` is set), SQL (when `sql.host` is set), and Redis via `ping` (when `redis.host` is set). With none configured it returns `status: "ok"`, so an empty configuration reports ready.
- The indicators are `@Optional()`, so a missing provider silently drops that check. When adding a dependency, add its readiness check and keep liveness cheap so orchestrators do not restart a healthy process because a downstream is slow.
- Keep error text from health checks free of connection strings and credentials.

## Logging

`BaseLoggerModule` exists in the source, but its registration in `DefaultModules` (`config/module/config.ts`) is commented out, and the `nestjs-pino` logger is commented out in `main.ts`. Do not describe it as active or add code that depends on it without enabling it deliberately. Use the Nest `Logger` as the existing services do, with levels matching severity, and keep tokens, credentials, and personal data out of log lines.

## Tracing

- `MicroserviceModule` imports `TelemetryModule.forRootAsync` from `@aisoft/backend-observer`, named with `server.name`. The repository's `config/traces.ts` owns the SDK, provider, propagator, and context manager. Do not add a second tracing setup or a duplicate span source.
- HTTP trace behavior is documented in `docs/http-trace.md`; TCP context propagation in `docs/tcp-context.md`. Read the relevant one before changing instrumentation, and run the matching smoke check described there (for TCP: `npm run build`, then `node test/tcp-context.smoke.cjs`). The package requires Node.js 24.
- Telemetry must not alter business results: a tracing fault should not fail or retry the business operation. Propagate only trace identifiers; never put credentials, actors, or personal data into trace context or attributes.

## Check

Exercise readiness with a dependency down and a dependency up, and confirm liveness is unaffected. For tracing changes, run the documented smoke in a local environment and confirm concurrent requests keep separate context. State which of these ran.
