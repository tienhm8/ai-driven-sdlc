# Routing acceptance

Section 4.4 separates **offline routing acceptance** from **optional live compatibility smoke testing**. A Project Instance can use one approved tool; it is not required to install, configure, or run both Claude Code and Codex, or to provide a cross-tool fallback. Offline acceptance can pass with live testing deferred until rollout. Neither check approves a Story, authorizes a merge, or changes a gate.

## Offline: catalog filter and pagination

Run from the framework root, after provisioning the platform's local dependencies:

```bash
PYTHONPATH=platform/src python3 -B -m unittest discover -s platform/tests -v
```

The [resolver fixtures](../tests/test_context_resolver.py) create two temporary Git checkouts and one synthetic work item. They do not install, build, or modify either application base. Use the [context resolver instructions](context-resolution.md) for an optional read-only check on other pinned checkouts. Use the same fixture work-item ID for both aliases, and the appropriate full commit and paths per alias. Do not assume the backend sample module implements the frontend sample page's actual API.

| Case | Expected evidence |
|---|---|
| Backend DTO and query for catalog filtering/pagination | `nestjs`, DTO and controller/service/repository references; no FE stack docs. `implementation/medium`. |
| Frontend catalog table and request mapping | `umi-max`, forms/tables and data-fetching references; no BE or CI skill. `react` appears only when component behavior is in scope; `gitlab-ci` appears only for CI focus. |
| Validation and review for each checkout | `testing` or `code-review` plus the current stack skill and only the matching stack reference. Routes are `implementation/medium` and `critical-review/high`, respectively. |
| Auth or migration with caller risk `low` | Effective risk and effort are `high`. A registry that can only supply `medium` returns `EFFORT_UNSUPPORTED`; an approved high binding preserves the floor. |
| Missing G3, stale G4, wrong alias/scope, or policy/config collision | The relevant action/preview reports a blocker. Explain does not claim or update an approval. |
| Retry/fallback and denied scope, data or budget | The [managed-runner fixtures](../tests/test_managed_model.py) prove limits and repeated preflight, with no real provider calls. They do not attest to any tool's native settings. |

For the real Story, confirm the screen, API contract, scope, AC and DoD independently. A suggested fixture contract is an optional status filter applied before pagination, a stable result order, and a filtered `total`; when the filter changes, the UI returns to page 1. Include empty results and invalid page/filter inputs. These are fixture expectations, not approved product requirements or evidence that the feature was built.

## Optional live smoke at rollout

Claude Code and Codex are candidate tools for a framework-level compatibility check, not project dependencies. At rollout, verify the tool or tools the project actually enables. Use both only when checking cross-tool compatibility; mark any tool not exercised as `not run` and do not claim live compatibility for it.

**Start only after approval.** Record the tool or tools under test, approved destination/account, maximum spend or approved billing arrangement for this smoke, approver, and allowable synthetic payload. If this is also a project pilot, separately record the real work-item ID, AC/DoD and scope; a tool smoke does not need real Story content. Use a disposable workspace and do not pass private IDs, code, credentials, checkouts or real Story material to a provider.

1. Verify each exact tool version and document its native model/effort settings and which runtime observations are available. Register the approved configuration outside the checkouts. Run explain first, as described in the [binding guide](../tool-adapters/README.md), and retain its sanitized binding result. Registry entries are not proof of an actual invocation.
2. Include a negative case per tool: an unapproved model or unsupported required effort must be blocked before egress. Do not intentionally spend on a denied route or try to trigger a provider refusal. Prefer a local fixture for the unsupported configuration rather than changing the user's default settings.
3. After the budget decision, exercise each approved binding with one benign synthetic request in an isolated session. An operator-driven smoke checks the tool only; to verify the managed boundary end to end, use a separately reviewed transport with one provider invocation per attempt, no implicit retries/fallback/actions, and the existing preflight. There is no live transport bundled in the platform today.
4. Record tool/version, case, requested model and effort, observed model and native effort, observation source, outcome and approval reference. Use documented tool/runtime metadata, not the model's own description of its settings. If either field is not observable, record `unverified`; do not promote that route for a task requiring verified capability/effort. Keep evidence local and omit prompt/transcript, source, credentials and machine paths.

| Tool | Version | Case | Requested model / effort | Observed model / effort | Observation source | Outcome / approval reference |
|---|---|---|---|---|---|---|
| Claude Code | — | Approved route / blocked route | — | — | — | Not run |
| Codex | — | Approved route / blocked route | — | — | — | Not run |
