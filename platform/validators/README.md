# Validators

`validate_project(project, framework=None)` and the [validator CLI](../scripts/README.md#kiểm-tra-và-đồng-bộ) check the manifest, workspace structure, local resource paths and approval policy. They do not validate stage artifact contents, traceability or security controls. A passing validation does not approve a human gate.

When mandatory rule overrides are disabled (the default), validation reports a non-blocking `RESERVED_RULE_IGNORED` warning for each project-local `.md` or `.mdc` rule under `core/` or `sdlc/` that the [rule loader](../rule-loader/README.md) ignores. Move project-specific rules outside those reserved directories.
