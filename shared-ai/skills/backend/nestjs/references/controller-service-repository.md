# Controller, service, and repository

Open this when adding a repository, changing a query or transaction, or debugging a persistence binding. Paths below are relative to the backend checkout.

| Layer | Owns | Keep out |
|---|---|---|
| Controller / transport handler | Input binding, validation, guard metadata, response contract, `@Operation` on state-changing handlers | ORM calls, business rules, transaction orchestration |
| Service | Use case, invariants, resource authorization, transaction boundary, business and diagnostic records via `@Observer` | Driver-specific query operators and raw database errors |
| Repository adapter | Queries, persistence mapping, application of supported query scope | HTTP status/serialization and business decisions |

1. Find the contract in the feature's `repository/` directory and check whether it extends the base contract in `src/modules/repository/common/`. Prefer changing the existing interface and active adapter over duplicating a driver API in the service.
2. In the owning module, read `RepositoryProvider(Entity.X, Implementation)`. In the service, pair the same entity key with `@InjectRepository(Entity.X)` and type the parameter with the feature's interface. Read `RepositoryConfig` for adapter setup and entity-specific `dpConfig` when configured. Do not add a second token, copy another entity's `dpConfig`, or register an inactive adapter just because its file exists.
3. Check the active adapter and query filters before changing persistence. Scope reads **and writes** according to the resource and partition policy, including counts and pagination where applicable. A request guard is not a substitute for a scoped query. If both adapters are active in supported deployments, preserve contract behavior across them or report the verified support boundary.
4. Where atomicity is needed, inspect the module's `TransactionProvider` binding and inject the matching transaction abstraction with `@InjectTransaction()`. Follow the base's transaction contract: start once at the use-case boundary, pass the same transaction to participating repository operations, and commit or abort as appropriate. Verify that the selected adapters actually support sharing that transaction; do not imply a single Mongo transaction covers SQL, Redis, or remote calls. Do not introduce transactions into read-only examples unnecessarily.
5. Mock at the entity token for service tests. Use an adapter/integration test when correctness depends on query scope, persistence mapping, or rollback. Run the DI smoke when registrations change and check what the smoke actually covers.

For a real binding example, see `src/modules/user/user.module.ts` and `src/modules/user/service/user.service.ts`: `Entity.USER` binds `UserMongoRepository`, `RepositoryConfig` sets a User-specific partition option, and `MongoTransaction` is the transaction provider. That wiring illustrates the pattern, not a default adapter or partition policy. Do not copy bootstrap logic or special internal scope exceptions into new features. See the [wiring example](../examples/module-example.md) and [auth/partition checks](authentication.md) if relevant. For what each layer logs, see [logging with Observer](logging-observer.md).
