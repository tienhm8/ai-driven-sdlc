# Model Router

`ModelRouter(shared_ai).route(task_type, effort=None, risk=None)` reads the four [v1 policy files](../../shared-ai/model-routing/README.md). It returns the profile ID, required capabilities, effective effort, and fallback profile candidates. For example, `code-review` selects `critical-review/high`; `documentation` selects `routine/low` unless a higher effort or risk floor applies. Unknown task or supplied risk and unsupported effort raise `RoutingError`; there is no implicit default route. An omitted risk applies no additional floor, so callers working under a risk-classification policy must supply the classified risk.

This is static routing only. A trusted adapter must bind profiles to approved models, validate provider capabilities and data/budget policy, and enforce retry/fallback rules. The returned `fallback` list is not approval to call a provider. Credentials never belong in routing configuration. See the [task mapping example](routing-contract.example.yaml).
