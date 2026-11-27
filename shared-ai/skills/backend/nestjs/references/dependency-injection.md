# Dependency injection

Use constructor injection. A TypeScript interface has no runtime identity: for feature repositories, reuse `RepositoryProvider` and `@InjectRepository` with the same entity rather than creating a second token. `RepositoryProviderName(Entity.X)` is the runtime token to use with `overrideProvider()` or `{ provide: token, useValue: mock }` in tests. For a transaction provider, use the existing `TransactionProvider` and `@InjectTransaction()` pair. Verify registration and exports in the owning module.

Do not store request state on a singleton. Use the base's context facility where applicable and verify that its scope is initialized on the affected HTTP or RPC path.

Run `npm run start:di-check` for registration changes. The repository's `test/di-check.ts` stubs selected dependencies; passing it does not test real database or transport behavior. Add a focused test for the binding or replacement you changed. See the [Jest example](../examples/testing-example.md).
