# Dependency injection

Dùng constructor injection. Nếu contract là TypeScript interface, dùng token runtime (ví dụ `Symbol`) với `@Inject()` và `useClass`/`useValue`; interface không còn ở runtime. Ưu tiên singleton không chứa trạng thái theo request; dùng `overrideProvider(token)` trong test.
