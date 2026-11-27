---
name: testing
description: "Plan and report verification for a change: choose the test level, set up isolated fixtures, and record exactly what ran. Use for any task that changes behavior; stack-specific commands are in the references."
---

# Testing

1. Map each acceptance criterion or changed behavior to a check. Choose the lowest level that can show it fails: a unit test for an invariant or a mocked dependency, an integration test when correctness depends on a real query, transaction, or serialization, and an end-to-end or manual flow only for what lower levels cannot show.
2. Cover failure as well as success: invalid input, a denied request, an empty result, a downstream error. A change that touches access control needs at least one denial test.
3. Use isolated fixtures and synthetic data. Never read or write real user data, production services, or shared environments to verify a change.
4. Run the targeted checks first, then the related suite. Record the exact command, the result (passed, failed, skipped), and the environment.
5. Report only what you ran. If a check could not run (missing dependencies, services, or a runner), say so and say what remains unverified. Never describe a check as passed when it was skipped, and never delete, disable, or weaken a test to make a result pass.
6. A passing build, a green CI run, or a passing smoke check shows only what it exercises; it does not replace review or an approval gate.

## Load a reference for the repository you are changing

| Repository | Open |
|---|---|
| Backend (`aisoft-backend`, NestJS) | [Backend (NestJS)](references/backend-nestjs.md) |
| Frontend (`base-web`, Umi Max) | [Frontend (Umi Max)](references/frontend-umi-max.md) |
