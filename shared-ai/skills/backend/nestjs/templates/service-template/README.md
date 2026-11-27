# Use-case service template

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

Register the provider token with the real adapter. Take `tenantId` from verified permissions; do not trust a tenant the request claims for itself. If the use case needs other permission conditions (owner, role, or action), check them before returning data. Test with two fake tenants.
