# Review checklist: correctness, tests, placement

## Does the code do the right thing?

- Where in the code each acceptance criterion is met; which criterion has no place meeting it.
- Edge cases, empty and duplicate data.
- State transitions: are invalid transitions blocked?
- Errors are not swallowed, are classified per the project's error handling, and do not leak internal details.
- Money and precise numbers do not use floating point; time zones, formats, and rounding follow the business rule.
- Writes that must succeed or fail together are in one atomic unit.
- Business rules come from the requirement, not invented by the code; if unclear, record an open question.

## Are there tests proving it?

- Each acceptance criterion has a test and real output, including the failure path.
- Tests check behavior, not implementation details; no empty assertions or assertions that only check "does not throw".
- No test was deleted, skipped, or weakened to get a pass.

## Is the code in the right place?

Take the layer map from the project's architecture docs; do not impose your own. Check these responsibilities:

| Responsibility | Question |
|---|---|
| Request boundary (handler, controller, UI component) | Does it only orchestrate, or does it hold business rules or direct data access? |
| Input validation and authorization | Done at the boundary by the shared mechanism, accepting only allowed fields? |
| Business logic (service, use case) | Is each rule here, and in one place only? |
| Data access (repository, query) | Does upper-layer code bypass it, or reach another module's data outside its public interface? |
| Async and side effects (job, event, notification, external call) | Are slow or irreversible effects separated from the main flow and from the transaction? |
| Output | Does it return the defined shape, not a raw internal object? |

Signals to examine, not laws: a unit over the project's size threshold, one function doing many things, deep nesting, too many dependencies, circular dependencies, duplicated logic.
