# Review checklist: concurrency, performance, operability

## Load and concurrency

- Two simultaneous requests on the same data: is there a read, decide, write-back pattern without a lock, optimistic locking, or conditional update?
- Is uniqueness guaranteed by the storage layer, or only checked in code ("already exists?")?
- Reruns (retry, message delivered twice, double click): is the operation idempotent? Is there an idempotency key for create and payment operations?
- Background tasks: timeout, retry limit, backoff, handling of final failure, overlap prevention where needed.
- Events and background tasks are emitted **after** the transaction commits.
- Shared in-process state (globals, stateful singletons) is safe with many requests and many instances.
- External calls have timeouts; their failure does not take down the main flow.

## Performance, data, cache

- Queries or network calls inside loops (N+1), including lazy-load properties.
- How many records the query touches today and as data grows; is there a limit, pagination, batching, or streaming, or is everything loaded into memory?
- Only needed columns and data are fetched.
- New or changed queries: filter, join, and sort conditions have suitable indexes (including composite column order); no condition makes an index unusable.
- Indexes after the change: an old index still serves an access pattern; a new index is not a duplicate or covered by an existing prefix. Adding or dropping an index needs evidence and an update to the DB design doc in the same PR.
- Migrations on large tables: long locks, need for batching or steps, backward compatibility with running code, a way back.
- Cache (only if justified): placed in one layer, keys deleted after commit on every write path, keys separated by user, tenant, and permission, no sensitive data in keys, behavior when many requests miss together.
- On a hot path, check against the performance requirement.

## Operability

- Important errors are logged with context and a correlation ID, without sensitive data.
- When a background task fails, someone knows (log, alert, dead-letter queue).
- New config has a value for every environment; new metrics or alerts are added where needed.
- The change can be rolled back; a feature flag has a removal plan.
