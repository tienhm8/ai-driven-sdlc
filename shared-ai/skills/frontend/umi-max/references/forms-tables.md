# Forms and tables

Open when adding or changing a list, form, modal, drawer, tree, filter, or pagination. Paths are relative to the `base-web` checkout.

## TableBase

- Use `@/components/Table` (`TableBase`) for list screens. It provides column filters, sorting, pagination, the create button, import/export buttons, and the form modal/drawer. Props to know: `modelName` (namespace), `columns`, `dependencies` (reload when they change, usually `[page, limit]`), `Form`, `formType` (`'Modal' | 'Drawer'`), `title`, `buttons`, `otherButtons`, `otherExtra`, `hideCard`, `pageable`, `hideTotal`, `addStt`, and `otherProps` (passed to the Ant Design table).
- Every column in `IColumn<T>` **requires `width`**. Declare quick filters on the column with `filterType`; a `'select'` filter needs `filterData`. Declare `sortable` on the column. Do not build a separate filter row when the column filters suffice.
- `buttons` toggles built-in buttons: `create` (default on), `import` and `export` (default off), `globalSearch`, `filter`, `reload`, `columnSetting` (default on). Disable create when the record state forbids it instead of hiding it with CSS.
- For server-side data, keep it in the model: `getModel(condition, filters, sort, ...)` is the default fetch; pass fixed conditions through the first argument or `getData`.
- For tree or load-once tables, set `pageable={false}`, `hideTotal`, `addStt={false}`, put the data in with the model's `setDanhSach`, and pass `otherProps={{ rowKey: '_id', expandable: ... }}`. Without a `rowKey`, expanding one row can expand the whole tree. Stable keys apply to any list or tree you render.
- `TableStaticData` is only for small in-memory data. Large or shared data must filter and paginate on the server.

## Forms

- Pass the form as `Form={Component}`. The component reads `record`, `edit`, `visibleForm`, `postModel`, `putModel`, and `formSubmiting` from `useModel`. Reset the form when it closes and set values from `record` when it opens, as the ChucVu form does.
- Use the shared rules (`import rules from '@/utils/rules'`, spread into `rules`): see [UI utilities](ui-utilities.md). Match length limits to the backend column.
- Keep the create and edit payloads consistent with the API contract. In particular, confirm whether a cleared optional field must be sent as an empty string, `null`, or omitted; do not assume.
- Ask for confirmation before destructive actions. A simple delete uses `Popconfirm`; when deleting can affect other records, check where it is used first and confirm with the user.

## Action buttons

The base provides `ButtonExtend` (`@/components/Table/ButtonExtend`): a `Button` with a built-in `Tooltip` (props: `tooltip`, `notHideText`, `otherTooltipProps`). Icon-only buttons need a tooltip. Existing screens such as `ChucVu` use a plain `Tooltip` + `Button`; follow the nearest screen when editing it. For new code prefer `ButtonExtend` **only if the team has adopted that convention**; do not rewrite existing screens for it. Wrap a `Popconfirm` around the button, not an extra `Tooltip`.

## Check

After a change, exercise create, edit, delete, filter, sort, page change, and an empty or failing response. When a filter changes, confirm the current page behaves as the contract requires. State what you exercised.
