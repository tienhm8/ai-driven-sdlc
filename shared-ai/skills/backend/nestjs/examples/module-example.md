# Ví dụ module Status

Ví dụ endpoint công khai, không đọc dữ liệu người dùng. Nếu dự án dùng guard mặc định, hãy tuân theo cơ chế khai báo public của dự án; không gỡ guard toàn cục.

```ts
import { Controller, Get, Injectable, Module } from '@nestjs/common';

@Injectable()
export class StatusService {
  getStatus(): { status: 'ok' } {
    return { status: 'ok' };
  }
}

@Controller('status')
export class StatusController {
  constructor(private readonly statusService: StatusService) {}

  @Get()
  getStatus(): { status: 'ok' } {
    return this.statusService.getStatus();
  }
}

@Module({ controllers: [StatusController], providers: [StatusService] })
export class StatusModule {}
```

Lưu ví dụ thành `status.module.ts` cùng thư mục với test minh họa. Thêm `StatusModule` vào `imports` của root module để đăng ký route. Endpoint này chỉ cho biết process có phản hồi; không dùng thay readiness kiểm tra phụ thuộc.
