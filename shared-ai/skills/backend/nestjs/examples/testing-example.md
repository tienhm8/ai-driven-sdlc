# Example: mock a repository at its entity token

This focused Jest test exercises the base's runtime token convention without a database. Use the pattern with the real service and stubs for its other dependencies when testing a feature. The example itself tests injection and delegation only, not guards, query scope, or transactions.

```ts
import { Injectable } from '@nestjs/common';
import { Test } from '@nestjs/testing';
import { Entity } from '@module/repository';
import {
  InjectRepository,
  RepositoryProviderName,
} from '@module/repository/common/repository';
import type { UserRepository } from '@module/user/repository/user-repository.interface';

@Injectable()
class UserReader {
  constructor(
    @InjectRepository(Entity.USER)
    private readonly repository: Pick<UserRepository, 'getById'>,
  ) {}

  read(id: string) {
    return this.repository.getById(id);
  }
}

it('injects the User repository under the same entity token', async () => {
  const getById = jest.fn().mockResolvedValue(null);
  const moduleRef = await Test.createTestingModule({
    providers: [
      UserReader,
      { provide: RepositoryProviderName(Entity.USER), useValue: { getById } },
    ],
  }).compile();
  try {
    await expect(moduleRef.get(UserReader).read('example-user')).resolves.toBeNull();
    expect(getById).toHaveBeenCalledWith('example-user');
  } finally {
    await moduleRef.close();
  }
});
```

When testing an imported feature module, use `overrideProvider(RepositoryProviderName(Entity.USER)).useValue(mock)` before compilation if the token is already registered. For a transactional service, supply its transaction dependency or stub the real use-case boundary, then test commit/abort behavior separately. Verify authorization and query scope with the appropriate integration or HTTP test; do not use this test-only reader as a feature implementation.
