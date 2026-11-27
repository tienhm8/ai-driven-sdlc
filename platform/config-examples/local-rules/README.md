# Opt-in BE/FE rules

These examples are not loaded from this directory, copied by init, or included in the shared mandatory rule set. Adopt only the file that fits the project:

| Example | Intended use |
|---|---|
| [Backend module and HTTP boundaries](backend-module-http.md) | NestJS project derived from `aisoft-backend` |
| [Frontend route, access, and request boundaries](frontend-route-access-request.md) | Umi Max project derived from `base-web` |

1. Review the boundaries against the actual project. Copy **only the chosen rule files**, not this README, into the directory named by `ai.local_resources.rules_path` in the Project Instance. Keep them outside the reserved `core/` and `sdlc/` namespaces.
2. Change `scope.repos` to the exact aliases in `technology_stack.repositories` if they are not `be`/`fe`. Adjust `scope.paths` to the actual checkout layout. Scope is evaluated by `resolve-context.py` against the supplied repo, path and task, not by a legacy loader or IDE-native glob setting. Include both a directory and its `/**` pattern when the team resolves both forms.
3. At rollout, run [context explain](../../docs/context-resolution.md#3-explain-a-task) for representative `code-generation` and `code-review` tasks. Check that an affected path selects its own rule, while the other alias, unrelated paths and tasks such as `documentation` do not. Inspect the mandatory rule list to confirm it is unchanged.

The examples state local constraints, not implementation steps. For techniques, use [NestJS](../../../shared-ai/skills/backend/nestjs/SKILL.md) or [Umi Max](../../../shared-ai/skills/frontend/umi-max/SKILL.md). General input validation, server-side authorization and evidence requirements still come from the [shared engineering rules](../../../shared-ai/rules/engineering/README.md); these examples do not add another general rule for those topics.
