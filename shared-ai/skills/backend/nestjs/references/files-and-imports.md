# Files and imports

Open when changing file upload or download, object storage, or bulk import. Paths are relative to the backend checkout under `src/`. Statements marked *(inferred)* come from reading the code and were not exercised.

## Wiring

`FileModule` registers three controllers: `FileController` (authenticated), `FilePublicController` (no controller-level guard), and `FileInternalController` (`@InternalController`). It binds `Entity.FILE` to `FileMongoRepository` and a `MongoTransaction`. Do not move a route between controllers without reviewing its access.

## Upload validation

- `@UploadFile()` applies `FileInterceptor("file")` and `FileTypeInterceptor`. `MulterConfigService` filters by `ALLOW_MIME_TYPES` using the **client-declared** MIME type and uses memory storage, so each upload is fully buffered in RAM. No `limits` (such as `fileSize`) are set in the Multer options or elsewhere in the module, so verify where size is bounded (gateway, proxy, or code) before accepting large files.
- `FileTypeInterceptor` then detects the real type from the bytes (`file-type`) and rejects types not in the allow-list (an `.cfb` container is allowed through). It also runs `compressFile`, which re-encodes PNG and JPEG to JPEG, and WebP to WebP, with a quality calculated so the result trends toward 512 KiB, with a floor of quality 16. **Uploaded images are lossy-recompressed, and PNGs become JPEGs**, but `req.file.mimetype` is updated to the detected type. Account for this when a feature needs the original bytes.
- The allow-list contains images, common Office documents, text/PDF, and MP3. `image/svg+xml` and HTML are not on it. Changing the list is a security decision; the same list drives both checks.

## Where the bytes go

`FileService.create` reads the `FILE_UPLOAD` setting first:

- `INTERNAL`: forwards the file with the caller's `authorization` header to another service (`internal/file`) via `InternalHttpService`.
- `LOCAL` (default, also used for any unknown value): reads the `FILE_STORAGE` setting. `DATABASE` stores base64 in the record's `data`; `S3` writes an object to the configured MinIO bucket under `<timestamp>_<uuid><ext>` and stores that key in `data`. Any other value throws `NotImplementedException`.

Both settings are initialized at bootstrap if missing (`FILE_STORAGE` from `server.defaultFileStorage`, `FILE_UPLOAD` to `LOCAL`). The filename is decoded from `latin1` to UTF-8 and URL-encoded in object metadata; never use the client filename as a storage path. Responses clear `data` so bytes and storage keys are not returned.

Other operations to know when touching storage: `updateFileData` replaces bytes per storage type (for S3 it overwrites the same key); `getFileBuffer` returns bytes (it forces `LOCAL` when the record exists locally); `deleteById` deletes only the database record, scoped to the author (a `TODO` notes missing permission and logging), and **no code in `src/` removes a MinIO object**, so an S3 object stays after its record is deleted; `migrateDbToS3` and `compressFiles` are bulk maintenance operations over every file (run with concurrency 8 and 16) and `compressFiles` takes no parameters.

## Large uploads (multipart)

`initiateMultipartUpload` computes `totalPart = ceil(size / multipartPartSize)`, starts an S3 multipart upload, generates one presigned `PUT` URL per part (valid 3600 seconds), and creates the file record with `uploadId` inside a transaction. `clientCompleteMultipartUpload` loads the record by `fileId` and completes the upload with the parts sent by the client. Points to verify when changing it: the complete call checks only that the record exists (it does not check that the caller is the author or that the part list is complete) *(inferred)*, and an upload that is started but never completed leaves an open multipart upload and a record. The file-type and MIME checks above **do not run on this path**, because the bytes go straight to MinIO through presigned URLs.

## Download and access

`accessFile` loads the record and applies its `scope`: `INTERNAL` requires a valid SSO token; `PRIVATE` requires a valid token and the caller to be the author, and answers *not found* instead of *forbidden*; `PUBLIC` works without a token. The code has a `TODO` about read authorization, so treat access control as incomplete and test the denial paths when changing it. `getFileData` streams from the database or MinIO with the stored `mimetype` as `Content-Type`; it sets no `Content-Disposition` or `X-Content-Type-Options`, so confirm how browsers will treat user-uploaded content before serving more types inline.

Internal endpoints (under `internal/file`: `GET :id/data`, `PUT :id/data`, `POST migrate/db/s3`, `PUT :id/upsert`) are for service-to-service use. `@InternalController` applies `GwGuard` (gateway API-key security) at class level; only `POST` create adds `@Authorization()` for a user. Read `common/guard/gw.guard.ts` to see exactly what it enforces, and never route a user-facing path through these endpoints. `migrate/db/s3` and `:id/upsert` are bulk or destructive maintenance operations; do not call them against real data to verify a change.

## MinIO

`MinioClientProviders` builds the client from the `minio` configuration (endpoint, port, SSL flag, access/secret key, region); never inline these values. `MinioService.onModuleInit` creates the bucket if it does not exist and only **logs a warning** on failure, so a missing or unreachable bucket shows up later as upload errors. There is no lifecycle policy in code.

## Imports

`BaseImportService<E, R>` (`config/service/base-import.service.ts`) is the shared engine. A feature subclass (for example `UserImportService`) passes a repository and a transaction, and can override hooks. Behavior to rely on:

- **Row validation** runs class-validator on the row class (`whitelist`, `forbidUnknownValues: false`) plus the override `validateAndTransformRowData`. A row with errors is **reported, not inserted**, and does not stop other rows; the result has `error` and a per-row `rowErrors` list.
- **Modes**: `ImportMode.CREATE` (default) calls `repository.create`; `UPDATE` and `UPSERT` call `updateOne` filtered by the entity fields that the import definition marks as keys. `dto.keys` is declared but marked `TODO` and the service computes keys from the definition, so request-supplied keys do not drive the filter.
- **Transactions**: with the default `useTransactionInsert: true`, each row is inserted in its own transaction and committed or aborted individually, so a batch is **not atomic**: earlier rows stay committed if a later row fails. Rows run one at a time in that mode; `concurentInsert` only applies when `useTransactionInsert` is false.
- **Dry run** (`dryRun: true`) validates and inserts inside a transaction and aborts at the end (using a savepoint per row only when `useSavepoint` is set), so validation reflects real constraints without persisting. Use it for the "validate" step of the UI flow.
- **Hooks**: `preprocessImport`, `validateAndTransformRowData`, `insertRowData`, and `afterInsertImport` are the override points. `afterInsertImport` runs once after all rows, in a separate transaction.
- Errors are converted with the injected `transformErrorMessage` using `showInternalMessage: true`, which can expose internal messages to the user; check what that returns before reusing it for sensitive entities.
- Import and export endpoints are generated by the base import controller factory in `config/controller/`. Prefer adding an entity to that mechanism over writing a new upload endpoint.
- `ImportSessionModule` is an **empty module**: there is no session state or resumable import at this revision.

## Check

Test: allowed and disallowed MIME types, a file whose bytes do not match its declared type, an empty file, a large file, each `scope` (anonymous, other user, author), and each storage and upload-target branch you touched. For imports, test a mix of valid and invalid rows in dry-run and real mode, and a repeated import in each mode. Use a mocked MinIO client in unit tests and a disposable bucket for integration checks; never use real user files.
