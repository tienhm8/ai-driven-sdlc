---
name: umi-max
description: "Implement, test, or review frontend changes on base-web or a project derived from it: Umi Max 4.4.6 with React 19.2.3 and Ant Design 5.24.2. Covers routes, pages, models, the shared table/form wrappers, and the shared Axios client."
metadata:
  umi-max-version: "4.4.6"
  react-version: "19.2.3"
  antd-version: "5.24.2"
---

# Umi Max 4.4.6 (base-web)

Baseline: Umi Max 4.4.6, React/React DOM 19.2.3, Ant Design 5.24.2, Node 22, Yarn Classic. Confirm against `package.json` and `yarn.lock`. If the checkout differs, report it and verify before using version-specific guidance; do not upgrade dependencies as part of a task. This is not a Next.js project; do not apply Next.js guidance.

## Everyday frontend changes

1. Find the closest existing screen and follow it end to end: `config/routes.ts` → `src/pages/...` → `src/models/...` (`useModel('<namespace>')`) → `useInitModel`/`useInitService` → shared Axios (`src/utils/axios.ts`). Reuse that path instead of adding a parallel request stack, store, or table.
2. Check `src/components/` before writing a component. Use `TableBase` for list screens, with `columns` (each needs `width`), the model namespace, and `Form` for add/edit. Do not hand-roll an Ant Design `Table` for a standard list.
3. Server-side lists keep filter, sort, and pagination in the model; change them through `getModel` and `dependencies`, not by filtering fetched rows in the page. Handle loading, empty, and error states, and confirm what happens to the current page when the filters change.
4. Do not treat hiding a button or menu as authorization; the API must enforce it. Never hard-code endpoints, tokens, or credentials. Do not import `src/utils/socket.ts` (see [data fetching](references/data-fetching.md)).
5. HTML from users or an editor must pass `sanitizeObject` before `dangerouslySetInnerHTML`. URLs and colors from data must go through `src/utils/security.ts` before use in `href`, `window.open`, or tag colors. See [UI utilities](references/ui-utilities.md).
6. Verify with `yarn build` and a smoke check of the changed flow. Report what ran, what failed, and what was not run. Do not run the aggregate `yarn lint` as a read-only check (it runs `max setup` and writes files), and never run the deploy, rsync, or sourcemap-upload scripts to test.

## Load more only when the task needs it

For a small change that follows an existing screen, this file and that screen are enough. Open only the reference that answers a question raised by the diff.

| Task | Open when needed |
|---|---|
| Add or change a form, modal, drawer, table, tree, filter, or pagination | [Forms and tables](references/forms-tables.md) |
| Add or change a route, menu, locale key, access rule, or session behavior | [Routing and access](references/routing-access.md) |
| Change an API call, model, request lifecycle, or the Axios client | [Data fetching](references/data-fetching.md) |
| Add a form rule, show a date, render HTML, or open a link | [UI utilities](references/ui-utilities.md) |
| Choose checks or prepare evidence | [Verification](references/verification.md) |
| See the real flow of a standard CRUD screen | [ChucVu walkthrough](examples/chucvu-flow.md) |
| Change component state, effects, focus, or accessibility | The `react` skill |
