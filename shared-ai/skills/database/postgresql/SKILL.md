---
name: postgresql
description: "Design or tune PostgreSQL."
---

# postgresql

## How to proceed

1. Read the task, stack, conventions, and approved scope before starting.
2. Put invariants in constraints; evaluate indexes against queries, vacuum debt, and DDL locks; keep concurrent index builds outside a transaction when needed.
3. Compare query plans on staging; check contention and migration compatibility.

## Handover

Report the decision, the evidence checked, and anything not verified; pass items that need approval to the responsible person.
