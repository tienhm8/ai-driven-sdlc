# Example: follow the ChucVu screen

A standard CRUD screen in `base-web`. Use it to learn the flow; do not copy its seed values (for example the `filterData` list on `ma`) into a new feature. Paths are relative to the checkout.

1. **Route**: `config/routes.ts` registers `ChucVu` under `DanhMuc` with `component: './DanhMuc/ChucVu'` and no `access`.
2. **Page**: `src/pages/DanhMuc/ChucVu/index.tsx` reads `getModel`, `page`, `limit`, `deleteModel`, and `handleEdit` from `useModel('danhmuc.chucvu')`, defines `IColumn<ChucVu.IRecord>[]` (each with `width`), and renders `TableBase` with `modelName="danhmuc.chucvu"`, `dependencies={[page, limit]}`, `Form`, and `buttons={{ import: true }}`. The action column uses `Tooltip` + `Button` + `Popconfirm`.
3. **Form**: `components/Form.tsx` reads `record`, `edit`, `postModel`, `putModel`, `formSubmiting`, and `visibleForm` from the same model, applies `rules.required`, `rules.text`, and `rules.length(...)`, and resets when closed.
4. **Model**: `src/models/danhmuc/chucvu.ts` returns `useInitModel<ChucVu.IRecord>('chuc-vu')`. No backend address argument is passed, so it uses the default `ip3`.
5. **Types**: `src/services/DanhMuc/ChucVu/typing.d.ts` declares `ChucVu.IRecord`. `services/DanhMuc/ChucVu/index.ts` is empty; no custom service is needed here.
6. **Request**: `useInitModel` → `useInitService` → the shared Axios client, which adds `Accept-Language` and `x-data-partition-code` and handles errors centrally.

To add a similar screen: add the route and locale keys, the page, the form, the model and the types; run `npx max setup`; build; then exercise create, edit, delete, filter, sort, and paging. Pass a different backend address to `useInitModel` only if the screen talks to another service.
