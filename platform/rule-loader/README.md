# Rule Loader

Call `load_rules(shared_root, project_root)` with the shared rules directory (normally `shared-ai/rules`). Project-local rules come from `ai.local_resources.rules_path` in `.ai-sdlc/project.yaml`, relative to the project root; the default is `.ai-sdlc/local-rules`. Shared rules use `.md`; local rules support `.md` and `.mdc`.

- **Mandatory:** Shared rules under `core/` and `sdlc/` are protected by default. When `governance.allow_project_override_mandatory_rules` is absent or `false`, the loader ignores local files in the reserved `core/` and `sdlc/` namespaces, including `.mdc` variants. Project validation reports `RESERVED_RULE_IGNORED` for each ignored local rule. Move project-specific rules outside these namespaces.
- **Customizable:** Outside the reserved namespaces (for example, under `engineering/`), local rules override shared rules with the same relative filename (including the extension). An explicit boolean `true` applies that same rule to both reserved namespaces. Invalid policy types cause validation and loading to fail.

**Upgrade note (incompatible change):** Earlier versions let a local rule with the same path replace a shared rule in any directory. Local rules under `core/` and `sdlc/` are now ignored unless the override flag is `true`. Before upgrading, run project validation and resolve each `RESERVED_RULE_IGNORED` warning: move project-specific rules outside these directories, or set the flag to `true` only if the project has approved replacing mandatory rules.

Passing `None` loads only eligible local rules; it does not load or verify the shared baseline. Pass the selected shared rules directory when the baseline is required. This API resolves instruction data only: it cannot detect conflicting prose in differently named files, grant privileges, or override mandatory gates.
