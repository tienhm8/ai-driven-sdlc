# Jobs, notifications, and scheduling

Open when changing a Bull queue or processor, push notifications, topic subscriptions, Redis usage, or a scheduled job. Paths are relative to the backend checkout under `src/`. Statements marked *(inferred)* come from reading the code and were not exercised.

## Redis client

`modules/redis/redis-client.provider.ts` exposes one global `ioredis` client under the token `REDIS_CLIENT`; inject it with `@InjectRedisClient()`. It reads `redis.*` and `server.name` from configuration, uses the server name as `keyPrefix`, supports TLS, and connects lazily in dependency-check mode. Bull has its own connection configured in `BullModule.forRootAsync` (`config/module/config.ts`) with the same prefix. Consequences:

- Do not create another `Redis` instance; inject this one. Keys written through it get the prefix automatically, so do not add the prefix yourself, and note that Bull keys are prefixed separately.
- The base has no cache abstraction. `cron-manager` uses it for a lock; nothing else uses it as a cache. If you add caching, define key naming, TTL, and invalidation with the owner and never cache data that varies by user or data partition under a shared key.
- A queue is not a cache, and a cache entry is not a job.

## Queues (Bull)

- `QueueName` (`common/constant/constant.ts`) has `OneSignal` and `AuditLog`. A module registers a queue with `BullModule.registerQueue({ name, defaultJobOptions })`; the processor is a provider with `@Processor(QueueName.X)` and one `@Process("<job-name>")` method per job. The producer injects the queue with `@InjectQueue(...)` and adds a job under the same job name. Check that the names match and that the processor is in the module's `providers`.
- Both queues register with `attempts: 3`, `timeout: 60000`, `removeOnComplete: true`, and `removeOnFail: true`: a job that fails three times is **discarded**, leaving only the log line from `@OnQueueFailed`. Make processors safe to run twice (at-least-once).
- Producers can override options per job. `OneSignalService.sendBatch` adds `send-batch` jobs with `attempts: 5` and `delay: 100`, so its effective retry count differs from the module default.
- `AuditLogProcessor` (`emit-log`) calls `repository.create(log)`. A retry after a partial success could write a duplicate audit record *(inferred)*; check the repository for a unique key before changing retries.
- Keep job payloads and log lines free of tokens and personal data. `send-batch` jobs carry the whole notification object and a list of player IDs, so they are stored in Redis until processed.

## Notifications and push (OneSignal)

- `NotificationService.createNotification` fills sender fields from the authenticated user, persists the record, then calls `OneSignalService.sendNotification(dto)` **without awaiting it**. The request succeeds even if the push later fails, and an exception inside that call is not reported to the caller. Do not assume delivery.
- `sendNotification` branches on `receiverType`: `TOPIC` reads subscribed users in batches of 2000 and calls `sendBatch` for each batch; `USER` calls `sendBatch` once for the listed users. `sendBatch` is `async` but is called without `await` in both branches, so errors become unhandled rejections *(inferred)*; handle them if you change this path.
- `sendBatch` selects device records for those users where `inactiveAt >= sendAt`, in batches of 2000, and enqueues one `send-batch` job per batch. Devices past `inactiveAt` are skipped, and the code has a `TODO` that they never receive the message later. Do not describe push as reaching every subscriber.
- `OneSignalProcessor` (`send-batch`) maps the notification to the OneSignal payload and calls `OneSignalApiService.createNotification` (`POST https://onesignal.com/api/v1/notifications`, with `app_id` and the API key from configuration). The HTTP client has a 5-second timeout. The processor logs the response body, so check that it never contains user data. A retry after a timeout can notify a user twice, because the provider call is not made idempotent here.
- `OneSignalService.updateOneSignalUser`, which would register a device, is **entirely commented out** at this revision, and `existPlayerId` is unused. Do not treat device registration as working. Confirm how player IDs actually get into the store before changing registration or expiry rules.
- The OneSignal API key and app ID come from the `oneSignal` configuration; never commit them or print them.

## Topics

`TopicService.userSubscribeTopic` checks that the topic exists, rejects a duplicate subscription, enforces `MAX_TOPIC_SUBSCRIPTION`, then creates the subscription. These are separate calls, so concurrent requests can pass the checks together and exceed the limit or duplicate *(inferred)*. A repository `bulkUserSubscribeTopic` exists and uses Mongo bulk operations. If correctness under concurrency matters, enforce it in the store (a unique key or a conditional update), not only in the service.

## Scheduled jobs

- Cron methods use `@Cron(...)` from `@nestjs/schedule`. Guard multi-instance jobs with `CronManagerService.isCronLeader(ServiceClass, "methodName")`, as `AuditLogService.clearOldLog` does (every 12 hours).
- `isCronLeader` returns truthy only when `server.cron` is enabled (`SERVER_CRON=1`) and the instance wins a Redis lock (`SET key pid EX 32 NX`). When `server.cron` is off the function **returns `undefined`** (falsy), so an instance without the flag never runs the job. The lock lasts 32 seconds and is not released when the job ends, so a job longer than 32 seconds can overlap the next trigger, and a faster schedule is skipped until the lock expires. Keep scheduled work short and idempotent.
- Two `cron-manager` modules exist (`src/cron-manager/` and `src/modules/cron-manager/`); `DefaultModules` imports `src/cron-manager/cron-manager.module`. Import `CronManagerService` from the one that is registered, and check before consolidating them.
- `clearOldLog` deletes audit logs older than a fixed window computed in code (the variable is named `twoYearAgo` but subtracts four years). Treat a retention change as a data-deletion change: confirm the window with the owner and test only against disposable data.

## Check

Unit-test a processor with a mocked repository or API client, including a thrown error. `npm run start:di-check` verifies queue and processor registration with stubs, not a live Redis. Never run a scheduled or delete job, or send a real push, against real data to verify a change.
