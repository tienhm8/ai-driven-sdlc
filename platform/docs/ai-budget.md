# AI cost and budget by work item

The budget ledger is local and optional. It does not require a second AI tool, credentials, a provider transport, or changes to gates. An expense approval does not substitute for G3/G4. The CLI never calls a provider.

## Register and approve

Run under the trusted operator or adapter identity. Use a protected local state directory outside the Project Instance and registered checkouts. The database and its enclosing cost directory must be private to that identity. `--approver`, `--reviewer` and `--actor` are audit labels, not authentication: authorize the operator upstream and keep the state and CLI write access away from agents, untrusted worktrees, and other users. Run the operator workflow against the same state directory as the managed runner.

```bash
budget() { python3 platform/scripts/ai-budget.py --project projects/demo --state-dir "$HOME/.ai-sdlc/state" "$@"; }
budget register FEAT-0001
budget register US-0001 --parent FEAT-0001
budget approve FEAT-0001 --usd 10.00 --approver budget-owner --reason 'Synthetic example only'
budget report FEAT-0001 --format csv
```

Use IDs from the existing backlog. Track BE and FE against the same Story; `repo` is an attribution field, not a separate wallet. A Feature includes its own shared work plus the direct usage of its Stories. Do not register the same charge under both. A Story with no explicit limit inherits the applicable Feature limit; when both are set, both apply. A standalone Feature, Bug, or Enabler can use its own ID. There is no implicit USD amount. The initial limit and all changes record the old/new amount, approver, reason, and UTC time. Use `history` to inspect these events and `usage` for active accounting rows (including repo, stage, task, model, and parent attribution).

## Import and reconcile

`import-usage <file>` accepts a JSON array; use `-` for stdin. It accepts only documented metadata, not raw logs/transcripts, source, prompts, or secrets. Treat imports as operator-reviewed evidence. Do not embed internal work item IDs in provider requests; map them to events locally. Use sanitized account aliases and opaque source IDs. Representative synthetic record:

```json
[
  {
    "work_item_id": "US-0001", "repo": "be", "stage": "04-development", "task": "code-generation",
    "run_id": "local-run-1", "session_id": "provider-session-1", "request_id": "provider-request-1",
    "event_id": "expense-1", "provider": "fixture", "account": "fixture-account", "unit": "request",
    "model": "fixture-model", "effort": "medium", "observed_at": "2026-11-27T12:00:00Z", "status": "ok",
    "basis": "estimated", "charge": "metered",
    "usage": {"input": 2000, "output": 200, "cache_read": 500, "cache_write": 0},
    "pricing": {"input": "2", "output": "3", "cache_read": "0.10", "cache_write": "4", "fee": "0"},
    "price_source": "fixture-price:v1", "price_effective_on": "2026-11-01"
  }
]
```

- **`billed`** means reconciled and attributed actual expense; **`reported`** means a tool/adapter-reported amount. Both use an `amount` decimal string. **`estimated`** is calculated from token buckets at rates per million plus a flat `fee` if supplied. Use explicit zeros for known zero counts/prices. Include a versioned price source and effective date for estimates; no prices are bundled. **`unmeasured`** records missing telemetry/pricing and has no amount. Use optional `model`, `effort`, `request_id`, `tool` and `attempt` only when supported by evidence. Include planning, review, paid failures/retries, subagent usage, and tool fees once at their actual accounting granularity.
- USD is default. Non-USD amounts/rates require `currency`, `fx_to_usd` (USD per currency unit), and `fx_source`. Conversion and pricing use decimal arithmetic; individual totals round up to integer microdollars. USD caps and quotes must fit that precision. `charge: seat` is only `estimated` or `unmeasured`; it is never added to metered spend or used to claim a per-Story invoice.
- Replays deduplicate by provider, account, and original `event_id`. Reconciliation uses **the same event ID and attribution** with a stronger basis (`billed` > `reported` > `estimated` > `unmeasured`) and replaces rather than adds the active cost. `request_id`, if available, must be unique across that provider/account. Use a stable attribution for each request.
- A provider/account/session has **one work item, charge type, and accounting unit**. For a cumulative session use `unit: session` and increasing `sequence` (starting at 1), with a stable session ID and a distinct `event_id` per snapshot; omit `request_id`/`attempt`. Only the latest snapshot contributes. A stronger reconciled total may be lower than an estimate. Do not mix session totals with individual requests or create artificial session IDs to bypass deduplication. Session summaries are only suitable when the entire session maps to one work item. Imports are atomic; a conflicting record rolls back the batch.

## Review at 80% and after a cut-off

`budget_warn_pct` is 80: it means **80% already used**, measured against the currently approved metered limit, not that 80% remains. At the threshold, the next managed attempt pauses unless a recorded review covers its projected total. A transport budget cut-off or a charge above its reservation also forces review. Use `pending` to locate unresolved attempts and `settle <reservation> --usage <file>` to reconcile a confirmed per-request amount or stronger evidence. No timeout automatically frees a reservation; a confirmed zero is allowed, but do not use it to represent unknown cost.

```bash
budget review FEAT-0001 --reviewer budget-owner --completed 'Planning and API review' \
  --remaining 'Validation' --reason 'Reached 80 percent' --projected-usd 2.00
```

A review records completed/remaining work, reason, and the future projection. It allows resumption only within the reviewed amount and approved limit. If the projected cost exceeds the balance, the report contains `increase_needed`; the ledger remains `awaiting-approval` until the approver records a sufficient new cap with `approve`. It never allocates extra money itself. Reconcile pending/unmeasured metered usage first. `hold` records an operator-imposed review, for example after a cut-off outside the managed runner. Unmeasured metered usage or a pending outcome means `remaining` is unknown, not zero. JSON/CSV reports distinguish known metered totals, seat estimates, reservations and coverage; `outside_managed_runner: not-enforced` is always explicit.

## Integrate an approved managed runner

Reference an operator-defined quote policy ID from `ai.budget_policy` in the versioned manifest. Pass `LedgerAttemptBudget(ledger, workspaces=..., policies=...)` to `ManagedModelRunner(..., budget=...)`. The policy mapping is trusted operator code, not loaded from a project-supplied command; each callback returns a positive USD quote for the exact `Attempt` (or `None` if there is no quote). Existing `allow_budget` approval, scope/gate/data checks and audit stay in force. Declaring a budget policy without a ledger adapter blocks dispatch. The transport supplies optional `ToolReply.usage` from actual sanitized telemetry. The runner fills status/model/effort from the observed reply and the ledger fills local work item, repo, stage, task, tool, run and attempt. Managed settlement takes metered request records only. Do not pass a Story ID to a provider or reuse another attempt's charge.

A single SQLite write transaction checks `spent + reserved + projected_next` for Story and Feature and records the reservation before dispatch. Each retry/fallback obtains its own reservation. A turn that did not dispatch can release its quote internally; a dispatched turn with missing or invalid usage stays pending, and the managed run stops. A turn interrupted before settlement may appear `active`; inspect `pending` and reconcile it with evidence. The ledger is a **projected soft cap**, not a provider-enforced maximum. Quotes can be exceeded, in-flight/interrupt costs can be unknown, and IDE/subscription use is not intercepted. The implementation does not start any actual provider transport or promise hard USD enforcement.
