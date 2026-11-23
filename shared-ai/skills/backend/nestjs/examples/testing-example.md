# Ví dụ Jest cho StatusModule

```ts
import { Test } from '@nestjs/testing';
import { StatusController, StatusModule, StatusService } from './status.module';

afterEach(() => jest.restoreAllMocks());

it('registers the controller and delegates to the service', async () => {
  const moduleRef = await Test.createTestingModule({ imports: [StatusModule] }).compile();
  try {
    const spy = jest.spyOn(moduleRef.get(StatusService), 'getStatus');
    expect(moduleRef.get(StatusController).getStatus()).toEqual({ status: 'ok' });
    expect(spy).toHaveBeenCalledTimes(1);
  } finally {
    await moduleRef.close();
  }
});
```

Đặt trong `status.module.spec.ts`; chạy theo script của dự án có `@nestjs/testing` và Jest. Đây là test DI/controller; thêm HTTP test `GET /status` (200 theo cấu hình route thực tế) để kiểm tra routing và serialization.
