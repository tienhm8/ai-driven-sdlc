# Settings, sequences, generated codes, and batch data changes

Open when changing system settings, counters, code generation, or a bulk data operation. Paths are relative to the backend checkout under `src/modules/`.

## Settings (`setting`)

- Settings are key/value records. `SettingService.getSettingValue(key)` returns the stored value or `{}`; `setSettingValue(key, value)` looks up a class in `MAP_SETTING_ENTITY[key]`, validates the value with class-validator (`whitelist`, stop at first error), and upserts. A new key needs an entry in `SettingKey`, a value class, and the map; without the map entry the call fails with a bad-request error.
- Other modules read settings at bootstrap and initialize defaults when missing (`FileService`, `UserService`). Because a missing setting reads as `{}`, code must handle absent fields. Changing a default or a value class changes behavior for existing deployments; account for already-stored values.
- Pass the active `transaction` option when a setting read or write belongs to a larger unit of work, as `FileService.updateFileData` does.

## Sequences (`increment`)

`IncrementService.getIncreaseCount(name)` calls a repository method that runs `findOneAndUpdate` with `$inc` and `upsert` in MongoDB, which is atomic per document, so two concurrent callers receive different values. This guarantee comes from the Mongo implementation; do not reimplement it with read-then-write, and do not claim it for another adapter without checking. A gap in numbers after a failed operation is normal; do not use it where gaplessness is required.

## Generated codes (`quy-tac-ma`)

`QuyTacMaService.getMa` loads the rule for a source, then builds the code from ordered parts: a data attribute, a lookup in a linked entity, or a generator function in `HamSinhMaService`, and joins them. Observed risk at the reference revision: the linked-entity branch reads from `mapRepository`, which is initialized empty, so a rule using it would fail unless the map is populated. Verify that before relying on it. Uniqueness of a generated code is not enforced by this service; if it must be unique, enforce it in the store and handle the conflict.

## Batch data changes (`data-process`)

`DataProcessService` rewrites a domain string across **every** MongoDB collection and every SQL table, except those named in `skipTables`. It writes in bulk, logs each document, and has no dry-run. Treat any change here as a destructive operation:

1. Confirm the scope with the owner (old and new value, tables to skip) and that a verified backup exists.
2. Check who can call it. At the reference revision the controller only has `@Authorization()` (JWT, system-role, and partition guards) and no `@AllowSystemRoles(...)`, while the README says only the admin role may use it. `SystemRoleGuard` returns `true` when no roles are declared, so at this revision any authenticated user who passes the JWT and partition guards can call these endpoints. Treat that as an access gap to report to the owner; do not rely on the README statement. Before exposing or extending the endpoint, add an explicit role restriction and test it with a non-admin user.
3. Prefer adding a dry-run or counting mode before extending it; test on disposable data only; never run it against a shared or production database to verify a change.
4. Keep logs free of document contents beyond identifiers.

## Check

Unit-test validation and default handling with a mocked repository. For anything that changes stored data, describe the rollback and state plainly that the change was not run against real data.
