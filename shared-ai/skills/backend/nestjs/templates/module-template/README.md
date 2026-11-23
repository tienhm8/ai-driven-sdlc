# Mẫu module theo feature

```ts
import { Module } from '@nestjs/common';
import { FeatureController } from './feature.controller';
import { FeatureService } from './feature.service';

@Module({
  controllers: [FeatureController],
  providers: [FeatureService],
})
export class FeatureModule {}
```

Đổi `Feature` bằng tên nghiệp vụ và tạo controller/service theo convention. Thêm `imports` cho module sở hữu dependency; chỉ thêm `exports` nếu có consumer. Dùng [ví dụ đầy đủ](../../examples/module-example.md) để kiểm tra cách wiring.
