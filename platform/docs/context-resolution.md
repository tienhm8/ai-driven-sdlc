# Context resolution

`resolve-context.py` previews the **Context** step for one work item, repository and revision. For a Story spanning backend and frontend, run it twice with the same `work_item_id` and separate aliases, revisions and paths. The result is not permission to edit, merge, deploy or call a model.

## 1. Configure the Project Instance

Use the [versioned manifest example](../config-examples/project.yaml) for `.ai-sdlc/project.yaml`. New instances start with `schema_version: 1`, an empty `technology_stack.repositories` map, and the default context and routing policies. Add each repo alias and its expected stack versions. Claude Code (`claude`) is the default for init without `--tools`; otherwise the first selected tool is the default. Keep `ai.local_resources` relative to the instance.

Older manifests continue to validate and use the existing loaders. To opt in, add `schema_version: 1`, declare the per-repo stack map, and run `validate-project.py`. Keep any other conventions used by the instance. Init and sync do not migrate or overwrite an existing project manifest. Move local mandatory overrides to non-conflicting, additive rules before opting in; the resolver blocks `governance.allow_project_override_mandatory_rules: true` without changing how the legacy loader handles it.

`ai.context_policy` and `ai.routing_policy` support only `default` in this resolver. An optional `ai.tool_bindings.<tool>.<profile>` entry declares `model` and optionally `effort` (`low`, `medium`, `high` keys pointing to native strings). Explain shows unverified declarations by default. `--adapters-dir` checks them against an [operator-approved registry](../tool-adapters/README.md) and emits a `bound-preview` or a blocker. It does not verify a live invocation. `ai.budget_policy` selects a trusted quote policy for the [optional budget ledger](ai-budget.md); a managed run that declares it requires the ledger adapter. The declaration is not approval or a hard cap. The shared task mapping remains authoritative; unknown tasks do not fall back to `ai.default_profile`.

## 2. Register the checkout and work item

Use an operator-managed YAML file **outside the instance and registered checkouts**. The operator or trusted integration supplies the values from the actual workspace, versioned backlog and handoff. Do not populate it from a model response, untrusted branch, or Story text claiming approval. This local adapter does not query a tracker. Absolute checkout paths belong only in this operator file, never in the committed project manifest.

```yaml
repositories:
  be: {repository: demo/catalog-api, checkout: /workspace/catalog-api}
  fe: {repository: demo/catalog-web, checkout: /workspace/catalog-web}
work_items:
  US-001:
    backlog_ref: backlog.md#US-001
    version: v1
    ac_ref: story.md#acceptance-criteria
    dod_ref: definition-of-done.md#v1
    repositories:
      be: {paths: [src/modules/catalog]}
      fe: {paths: [src/pages/Catalog, src/models/catalog.ts]}
```

Paths are normalized and scoped per alias. Supply a full commit ID from the registered checkout, not `HEAD` or a branch name. The resolver reads committed manifests/lockfiles, not the working tree. The pilot checks `@nestjs/core` in npm and `@umijs/max`, React and Ant Design via direct dependency selectors in Yarn Classic. Other stack entries are declarations only. When the expected lockfile entry or skill baseline does not match, the affected version-specific skill is not selected. This is not an install or a package upgrade.

## 3. Explain a task

```bash
python3 platform/scripts/resolve-context.py \
  --project projects/Project-CRM --workspace-config "$HOME/.ai-sdlc/workspace.yaml" \
  --work-item-id US-001 --repo be --revision "$BE_COMMIT" \
  --role developer --stage 04-development --task code-generation --risk medium \
  --path src/modules/catalog --focus dto --focus query --format json
```

- **`--action prepare`** (default) lets you inspect the context while preparing a task. A resolved preview still has `authority: none`. The role is a context label, not proof of identity or permission.
- **`--action coding` / `--action merge`** check G3 / G4 respectively. The trusted work-item repo entry must provide a `G3` or `G4` mapping with `revision`, `execution_id`, `review_id`, `artifact_sha256`, and `review_context_sha256`; G4 also needs the canonical `target` (`repository`, `pull_request`, `base_ref`). This link must be derived by the operator/integration for the exact work item, revision and review package. The resolver checks the matching record in the existing governance store (`--state-dir` when not at its default). It does not turn a YAML field into an approval, claim G4, or check permission to execute. The workflow engine still owns the action boundary.
- **Exit codes:** `0` means the preview resolved, `1` means it reports blockers, and `2` means invalid CLI input or an unreadable/invalid workspace config. No mode calls an AI provider, changes gate state, reserves budget, or sends context outside the workspace.

## Rule and skill selection

The resolver always selects shared mandatory `core`/`sdlc` rules and the framework's workflow, human-review and AI instructions for the chosen stage before applicable engineering and local rules. Local rules can declare a canonical `id`, `scope`, and known `conflicts` in YAML frontmatter. Scope fields are optional (`repos`, `paths`, `tasks`, `stages`); configured fields are combined with AND and each field accepts any listed value. Path patterns use case-sensitive shell-style matching against the paths actually supplied, not against an expanded directory listing. Existing `.mdc` rules with tool-native `globs` or `alwaysApply` need an explicit resolver `scope`. A rule without scope is unscoped. Mandatory IDs/namespaces cannot be claimed by local rules. Duplicate IDs (including `.md` vs `.mdc`) and active declared conflicts block the preview. Textual contradictions still need human review; a renamed document or skill never becomes a governance override.

For NestJS and Umi Max projects, start with the [opt-in BE/FE rule examples](../config-examples/local-rules/README.md). Copy only the rules that fit the project into its configured local rules directory and adjust the aliases and paths. The examples are not loaded by default.

Skill selection reads `SKILL.md` frontmatter first and uses the pilot stack/task/focus triggers, not descriptions as instructions. Use `--focus` for the actual surface: for example `dto`, `query`, `di`, `table`, `request`, `route`, `component`, `auth`, `authorization`, `migration` or `ci`. Project-local skills may opt in with the same `scope` fields; a duplicate shared skill ID blocks rather than shadowing the shared skill. Explain lists resource paths without reading bodies or expanding references. A local consumer can use `load_selected_context` to read just the selected bodies and references in order. It never follows links recursively or grants execution authority. See the [existing loader contracts](../rule-loader/README.md) for the legacy APIs.
