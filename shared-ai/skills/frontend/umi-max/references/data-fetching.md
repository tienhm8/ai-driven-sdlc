# Data fetching

Open when changing an API call, model, request lifecycle, or the Axios client. Paths are relative to the `base-web` checkout.

## Model and service chain

- `src/models/<group>/<name>.ts` default-exports a hook that returns `useInitModel<T>('<api-path>')`. The model namespace is `<group>.<name>` (for example `danhmuc.chucvu`), used by `useModel('<namespace>')` and `TableBase modelName`. After adding a model file, run `npx max setup` so Umi picks it up; a missing namespace usually means this was skipped.
- `useInitModel(url, fieldNameCondition?, initCondition?, ipService?, initSort?, initFilter?)` owns the list, `page`, `limit`, `filters`, `condition`, `sort`, form flags, and actions (`getModel`, `getAllModel`, `postModel`, `putModel`, `deleteModel`, `handleEdit`, `handleView`, and the many variants). It builds on `useInitService`, which calls `<ip>/<url>/...`.
- The default backend address is `ip3` from `src/utils/ip.ts`. A model that talks to another service must pass that address as the fourth argument; omitting it silently targets the default service. Take addresses from `ip.ts`; never inline a URL or a port.
- `postService` and `putService` only call `<ip>/<url>` and `<ip>/<url>/:id`. For a sub-route (for example `:id/approve`), write a dedicated function with the shared `axios` instance; calling `postService` would hit the create route.
- Put record types in the feature's `typing.d.ts` namespace and enums/labels in a `constant.ts`; keep enum values aligned with the backend contract. A `services/<Group>/<Name>/index.ts` file is only needed for custom calls; it may be empty and need not be created to match a diagram.

## Request behavior to preserve

- `getModel` sends `page`, `limit`, `sort`, the condition (`condition` or `cond`, per the model argument), `filters` (inactive filters removed), and an optional `select`. A page past the end resets to the last page and rejects with `Invalid page`; a failure clears the list and resets to page 1. Handle rejection where you call it.
- Axios (`src/utils/axios.ts`) is shared. Its request interceptor sets `Accept-Language` and adds `x-data-partition-code` from `localStorage.partitionCode` unless the header is set explicitly (a null or undefined value removes it) or the path is excluded. Its response interceptor shows errors unless the request body includes `silent: true`. Do not add a second interceptor or client; extend this one only when the change affects every request.
- Rapid filter changes can resolve out of order. When a screen issues its own overlapping requests, make sure a stale response cannot overwrite a newer one.
- Authentication tokens come from the OIDC flow, not from code you add. Do not read tokens from storage or write credentials into a request.

## Do not import `src/utils/socket.ts`

Importing it opens a Socket.IO connection at module load to a hard-coded external URL, with the token read from `localStorage`. Importing it from any screen sends the token to that host. Treat it as unvetted; build any real-time need on an approved, configured endpoint instead.
