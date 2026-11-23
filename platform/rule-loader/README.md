# Rule Loader

Call `load_rules(shared_root, project_root)` with the shared rules directory (normally `shared-ai/rules`) or `None`. Project-local rules come from `ai.local_resources.rules_path` in the project's `.ai-sdlc/project.yaml`, relative to the project root. If omitted, the default is `.ai-sdlc/local-rules`. Local rules support `.md` and `.mdc`. A local rule with the same relative filename overrides the shared rule. This resolves instruction data only; it does not grant privileges or override required governance policy.
