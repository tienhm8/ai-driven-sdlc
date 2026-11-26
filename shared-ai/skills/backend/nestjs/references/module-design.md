# Module design

Start with a nearby module that is registered in `src/app.module.ts`, `src/config/module/config.ts`, or another owning module. Keep a feature's controllers, services, DTOs, and repository implementations together. Follow the base's imports and filenames rather than copying a generic scaffold.

- Register controllers in `controllers` and services and adapter bindings in `providers`. Export only the provider or contract that another module needs; the consumer imports the owner. Keep base-owned shared facilities in their owning modules instead of re-registering them globally in a new feature.
- Bind the active feature adapter and optional transaction provider using the [repository pattern](controller-service-repository.md). A global `RepositoryModule` does not by itself select a feature adapter.
- If imports become circular, identify who owns the use case and move shared orchestration or contracts before considering `forwardRef`.
- When registry or provider scope changes, run an appropriate DI test; see [dependency injection](dependency-injection.md) and the [UserModule wiring example](../examples/module-example.md). For an unfamiliar checkout, see [project structure](project-structure.md).
