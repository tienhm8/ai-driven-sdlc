# Mẫu service theo use case

```ts
import { Inject, Injectable } from '@nestjs/common';

export const FEATURE_REPOSITORY = Symbol('FEATURE_REPOSITORY');

export interface FeatureRepository {
  findVisibleById(tenantId: string, id: string): Promise<{ id: string } | null>;
}

@Injectable()
export class FeatureService {
  constructor(@Inject(FEATURE_REPOSITORY) private readonly repository: FeatureRepository) {}

  async find(tenantId: string, id: string): Promise<{ id: string } | null> {
    return this.repository.findVisibleById(tenantId, id);
  }
}
```

Đăng ký provider token bằng adapter thật; lấy `tenantId` từ quyền đã xác minh, không tin tenant tự khai từ request. Nếu use case cần điều kiện quyền khác (owner, role hoặc action), kiểm tra trước khi trả dữ liệu. Kiểm thử với hai tenant giả.
