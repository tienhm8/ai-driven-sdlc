# Feature module template

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

Replace `Feature` with the business name and create the controller and service following the conventions. Add `imports` for the module that owns each dependency; add `exports` only if there is a consumer. Use the [full example](../../examples/module-example.md) to check the wiring.
