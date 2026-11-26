# Frontend review checklist (Umi Max, `base-web`)

Use for a diff in the frontend. Check only the items the diff touches. Detail for each is in the Umi Max skill.

## Reuse of the base
- The change follows the existing path `config/routes.ts` → page → model → `useInitModel`/`useInitService` → shared Axios. It does not add a second HTTP client, interceptor, or store. ([data fetching](../../../frontend/umi-max/references/data-fetching.md))
- List screens use `TableBase`; every column has `width`; filters, sort, and pagination stay in the model. A tree or load-once table sets `rowKey`. ([forms and tables](../../../frontend/umi-max/references/forms-tables.md))
- A model for another service passes that service's address from `ip.ts`; no URL, port, or credential is written in code.
- Sub-routes of an API are called with a dedicated function, not through `postService` or `putService`, which only call the base path.

## Routes and access
- A new route has its locale key in both `vi-VN/menu.ts` and `en-US/menu.ts`. A new model was registered with `npx max setup`.
- Hiding a button or menu is not authorization; the API must enforce it. Loading state is handled so permissions-in-flight do not flash a forbidden screen. ([routing and access](../../../frontend/umi-max/references/routing-access.md))
- `currentRole`, Keycloak settings, and the "do not touch" block in `ip.ts` are unchanged unless that is the task.

## Untrusted data
- HTML from users or an editor passes `sanitizeObject` before it reaches `dangerouslySetInnerHTML`. Links and colors from data pass through `src/utils/security.ts` before `href`, `window.open`, or a tag color. ([UI utilities](../../../frontend/umi-max/references/ui-utilities.md))
- `src/utils/socket.ts` is not imported: it connects to a hard-coded external host with the stored token on import.
- No token, personal data, or secret in console output, error reports, or committed files.

## Component behavior
- State lives where it is used; derived values are computed in render; effects only synchronize with external systems and clean up; a stale response cannot overwrite a newer one. Keys are stable. Icon-only controls have an accessible name, and focus is handled for modals and drawers. (`react` skill)

## Evidence
- The author reports `yarn build` and a manual smoke test of the changed flow, with steps, and says that no automated tests exist. No claim of a passing test suite or of the e2e scaffold running. The aggregate `yarn lint` was not used as a read-only check. ([testing](../../testing/references/frontend-umi-max.md))
