---
name: authorization
description: "Design or review defensive authorization: deny by default, per-resource checks on the server, tenant and owner scope, and cross-tenant tests. Use when a change touches roles, permissions, ownership, or data scope."
---

# Authorization

1. Deny by default. A route, action, or query is allowed only by an explicit rule; a missing declaration must not mean allowed. Confirm what the framework does when no rule is declared.
2. Enforce on the server, per resource. Check the action, the owner, and the tenant or partition for each resource the request names; hiding a control in the UI is not a check.
3. Apply scope inside the query as well as in a guard: list, count, lookup, update, and delete must all be limited to what the caller may access. Do not trust an identifier or partition selector supplied by the client without verifying the caller's membership.
4. Grant the least privilege needed. Separate identity from permission, and keep role and permission definitions in one place.
5. Test with at least two tenants or owners: an allowed caller succeeds, and each cross-scope or under-privileged caller is denied, including for lists and counts. Confirm that a denied write changed nothing.
6. Choose the response for inaccessible resources deliberately (forbidden or not found) and keep it consistent with the existing contract.

## This stack

Roles, `SystemRoleGuard`, `DataPartitionGuard`, and per-entity partition behavior in `aisoft-backend` are in the NestJS skill's [authentication and partition reference](../../backend/nestjs/references/authentication.md); the frontend only hides controls and is described in the Umi Max skill's [routing and access reference](../../frontend/umi-max/references/routing-access.md). Use those instead of restating them here.
