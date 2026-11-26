# Example: read the UserModule wiring

This is an abridged example from `src/modules/user/user.module.ts` and `src/modules/user/service/user.service.ts`, not a complete module to paste. Reuse the wiring pattern, not the `User` entity, policy, or adapter for another feature.

```ts
// UserModule: relevant entries in @Module({ providers: [...] }).
UserService,
RepositoryProvider(Entity.USER, UserMongoRepository),
RepositoryConfig({ User: { dpConfig: { disable: true } } }),
TransactionProvider(MongoTransaction),
```

```ts
// UserService: relevant constructor parameters (other dependencies omitted).
@InjectRepository(Entity.USER)
private readonly userRepository: UserRepository,
@InjectTransaction()
private readonly userTransaction: BaseTransaction,
```

1. Start at the owning module and follow `Entity.USER` into `UserService`. The service calls `UserRepository`; the registered implementation is `UserMongoRepository`, not the SQL adapter with a similarly named file.
2. For a new feature, declare its entity token and repository contract using the base conventions, select the actual adapter, and decide whether the use case needs a transaction. The User-specific `dpConfig` above illustrates where configuration lives; it is **not** a safe default for another entity. Do not copy User bootstrap logic or special internal scope exceptions.
3. Keep the controller responsible for the route and validated DTO, and preserve the existing response/error handling. Register the module with its owner and export only what another module uses.
4. Use the [repository-token Jest example](testing-example.md) for DI and the [testing reference](../references/testing.md) to decide which behavior needs an integration or HTTP test.
