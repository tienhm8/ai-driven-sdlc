# Routing and access

Open when adding or changing a route, menu entry, locale key, access rule, or session behavior. Paths are relative to the `base-web` checkout.

## Add a page

1. Write the page under `src/pages/...`.
2. Add the route to `config/routes.ts` with `name`, `path`, `icon`, and `component` (for example `./DanhMuc/ChucVu`). A parent menu has `routes: [...]` and no `component`.
3. `name` is also the locale key: add `menu.<Parent>.<Child>` to `src/locales/vi-VN/menu.ts` and `src/locales/en-US/menu.ts`. A missing key shows the raw key in the menu.
4. If you added a model, run `npx max setup`.

## Access control

- The `ChucVu` route has no `access`, so it is visible to any signed-in user of the app. Follow the nearest route, and do not assume access is enforced because a route exists.
- To restrict a route, set `access: 'accessFilter'` with `maChucNang: '<code>'`, or `access: 'manyAccessFilter'` with `listChucNang: [...]`. The functions live in `src/access.ts` and check the codes against `initialState.authorizedPermissions[].scopes`. They **allow** the route while permissions are still loading (`permissionLoading` and no scopes yet) so a user is not shown 403 during load; then they enforce. Verify behavior on refresh and on a deep link.
- To hide UI by permission, use `usePermissionCheck()` (`hasPermission`, `hasAnyPermission`, `hasAllPermissions`; every check returns `false` until `isReady`) or `useCheckAccess(code)` (returns `true/false` and has no ready state, so it returns `false` while permissions load). Pick the one that fits the loading behavior you need, and avoid flashing a "forbidden" state while loading.
- UI checks only hide controls. The backend must enforce the same permission; confirm that before relying on a hidden button.

## Runtime and layout

`src/app.tsx` defines `getInitialState` (starts with `permissionLoading: true` and restores `authorizedPermissions` from `sessionStorage` when present), the layout, and `onPageChange`. `onPageChange` redirects users who have permissions but no resource matching `currentRole` (from `src/utils/ip.ts`) to the forbidden page, skipping `unCheckPermissionPaths`. Do not change `currentRole`, the Keycloak settings in `ip.ts`, or the "DO NOT TOUCH" block for a feature task; those depend on Keycloak configuration owned elsewhere.

## Check

Exercise: direct load of the route, refresh, a user without the permission, and the menu entry. Report which of these ran.
