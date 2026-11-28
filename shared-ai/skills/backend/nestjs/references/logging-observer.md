# Logging with Observer

Open when a controller, service, job, or consumer writes a log, or when reviewing one. New code logs through `@aisoft/backend-observer`; do not add the Nest `Logger`, `console.*`, or a second Pino instance. Existing `Logger` calls stay until the owning code is changed. Requires a package version that exports `@Observer` and `TelemetryFacade`; check the lockfile and report a mismatch instead of upgrading as part of the task.

`TelemetryModule` is registered once by the application (see [health, logging, and tracing](health-and-observability.md)). Feature code does not register it, read `OBSERVER_*` variables, or configure OTLP.

## Pick the record type

| Need | API | Where |
|---|---|---|
| Who started a state-changing action and whether it succeeded | `@Operation({ action })` | HTTP controller handler |
| Same, outside an HTTP controller | `observer.operation.run({ action, actor?, data? }, fn)` | Start of a job, processor, cron, gRPC/TCP handler |
| A business fact operators need to search (state change, created record) | `observer.business.emit({ data })` or `business.builder` | Service |
| Technical detail: retry, degraded dependency, cache decision, handled error | `observer.diagnostic.emit({ severity, message?, error?, data? })` or `diagnostic.builder` | Service, adapter |
| Latency or failure of one named step | `observer.trace.run({ name, attributes? }, fn)` | Service, around a repository or remote call |

An operation record summarizes one initiated action; do not open an operation for internal steps. Do not add a diagnostic for a step a business record already describes.

## Controller

Every handler that changes state carries `@Operation`: HTTP `POST`, `PUT`, `PATCH`, and `DELETE` handlers that write data. Read-only endpoints do not. Authentication must run first so `request.user` is set; Observer resolves the actor from it and otherwise records `anonymous`.

```ts
@Post(":id/activate")
@Authorization()
@Operation({ action: "customer.activate" })
activate(@Param("id") customerId: string) {
  return this.customers.activate(customerId);
}
```

Observer records success or failure when the handler returns or its `Promise`/`Observable` settles, and preserves the original result or error. `data` holds a few short, non-personal facts (for example `{ channel: "support" }`); never the request body.

## Service

Inject the facade with the module and service names so every record carries `moduleName` and `serviceName`:

```ts
@Injectable()
export class CustomerService {
  constructor(
    @Observer({ module: "customer", service: "customer" })
    private readonly observer: TelemetryFacade,
    @InjectRepository(Entity.CUSTOMER) private readonly repository: ICustomerRepository
  ) {}

  async activate(customerId: string) {
    await this.observer.trace.run(
      { name: "customer.activation.persist", attributes: { "customer.id": customerId } },
      () => this.repository.activate(customerId)
    );
    this.observer.business.emit({
      data: { event: "customer.activated", customerId, previousState: "pending", state: "active" }
    });
  }
}
```

- Set both `module` and `service`; a missing one logs a warning per class. Override them on a single emit only when that record belongs to another module.
- Log while the operation context is active. Do not pass operation or trace IDs through method parameters; Observer attaches them.
- Do not `catch` only to log and rethrow: the exception filter already records unhandled errors, and the operation records the failure. Emit a diagnostic where the error is handled (retry, fallback, swallowed) or where it adds context the filter cannot see.
- Create a builder inside the flow that owns the data. Never keep one in a provider field or other state shared between requests.

## Jobs, processors, cron, and non-HTTP handlers

`@Operation` is documented for HTTP controllers. For a Bull processor, scheduled job, or gRPC/TCP handler that writes data, open the context with `operation.run` at the entry point and give a stable technical actor when no user exists:

```ts
@Process("send-reminder")
handle(job: Job<{ invoiceId: string }>) {
  const { invoiceId } = job.data;
  return this.observer.operation.run(
    { action: "invoice.reminder.send", actor: { id: "billing-scheduler" }, data: { invoiceId } },
    () => this.sendReminder(invoiceId)
  );
}
```

`operation.run` does not read context from Bull, TCP, or HTTP metadata; cross-service linking relies on the transport propagation described in the tracing docs. Without an actor, Observer records `system`. Nested operations get their own ID and a `parentOperationId`.

## Naming

- Operation `action`: `<domain>[.<sub>].<verb>`, lowercase, verb last, present tense. Examples: `customer.activate`, `invoice.reminder.send`. Keep the set small and stable; never put IDs or user input in the name.
- Business event (`data.event`): same shape in the past tense. Examples: `customer.activated`, `invoice.created`.
- Span `name`: `<domain>.<step>`, for example `customer.activation.persist`.
- `module` / `service` in `@Observer`: the owning Nest module and service, lowercase.

## Data safety

- The actor carries only `id`. The application configures `actorResolver` to return `{ id: user.sub }`; the library default also copies `username`, `fullName`, and `email` into every operation record, so do not rely on it:

  ```ts
  actorResolver: ({ request }) => {
    const user = (request as { user?: { sub?: string } } | undefined)?.user;
    return user?.sub ? { id: user.sub } : undefined;
  }
  ```

- Never add tokens, passwords, keys, connection strings, or personal data (name, email, phone, national ID, address) to `data`, `message`, `actor`, or span attributes. Use IDs.
- Prefer structured `data` over free text; redaction works on paths, not inside `message` or stack text.
- For a sensitive field specific to one call, add `redaction: { paths: ["data.<field>"], remove: true }`. Paths are static strings in code; never build them from request input.
- Observer does not redact what you write directly on a span (`span.setAttribute`, `span.addEvent`); clean it first.
- Keep `strict: true` for tests. In deployed environments a logging fault must not change the business result.
- `@Operation` is operational telemetry; it does not replace the audit trail (`AuditLogInterceptor` and the audit queue). Keep both where audit applies.

## Severity

`trace` and `debug` for detailed investigation, `info` for normal meaningful activity (default), `warn` for a recoverable anomaly, `error` for a failed operation that needs investigation, `fatal` when the service cannot continue. Do not log an expected business outcome (validation failure, not found) as `error`.

## Testing

How to provide or mock `TelemetryFacade` and assert emitted records is defined in the package's own docs (`output-and-testing.md` and `api.md` of `@aisoft/backend-observer`); follow them when writing the spec. Until checked there, treat this as unverified:

- A service with `@Observer` fails DI in `Test.createTestingModule` unless the test registers Observer or provides the facade. Fix the spec setup; do not drop the injection.
- Assert the business outcome first. Assert a telemetry record only when it is the behavior under change (a new business event, a removed personal field).
- Run `npm run start:di-check` after adding `@Observer` to a provider.

## Check

Before handing off, confirm: every state-changing handler has `@Operation` or `operation.run`; names follow the convention; no personal data or secrets in `data`, `message`, `actor`, or span attributes; no new `Logger` or `console` call; DI check and focused tests ran. State which checks ran.
