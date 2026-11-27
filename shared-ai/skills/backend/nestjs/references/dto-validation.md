# DTO validation

- Use input DTOs for request bodies or queries where needed. A simple path param can use an appropriate pipe. Keep the external input and response contracts independent of persistence fields; never return raw entities or expose new fields merely because a persistence model changed.
- Check the existing `ValidationPipe`, `class-validator`, and `class-transformer` setup before adding a pipe. Respect the app's policy for transforming inputs and stripping or rejecting unknown fields (`whitelist` / `forbidNonWhitelisted`). Do not rely on implicit coercion without checking the result.
- Specify the type, format, length, and allowed values as applicable. For nested objects or arrays, check for `@ValidateNested` and the corresponding `@Type` metadata when using class-validator and class-transformer.
- Input validation checks shape; the service still owns business invariants and resource-level authorization. Preserve the standard [error contract](exception-handling.md).
- Test missing, invalid, extra, and boundary values as relevant. For a behavior change, see [testing](testing.md).
