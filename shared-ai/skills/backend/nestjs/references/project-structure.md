# Project structure

Find the checkout root and the package manifest and lockfile before choosing paths or commands. In the base, start at `src/main.ts` for bootstrap, `src/app.module.ts` for app-owned modules, and `src/config/module/config.ts` for default modules and cross-cutting providers. Locate the owning feature under `src/modules/` and keep DTOs, adapters, and tests alongside the feature according to the nearest working example. If the derived project uses a monorepo or another app entry point, follow its actual composition root instead of imposing the base's directory layout.
