# UI utilities

Open when adding a form rule, showing a date, rendering HTML from data, or opening a link. Paths are relative to the `base-web` checkout.

## Form rules (`@/utils/rules`)

Spread rules into `rules`: `rules={[...rules.required, ...rules.text, ...rules.length(250)]}`. Available groups include:

- Text: `required`, `text` (rejects whitespace-only), `length(n)`, `ten` (letters only, at most 50 characters; not for long names), `dacbiet`.
- Numbers: `number(max?, min?, hasDecimal?)`, `float`, `floatnumber`, `diem`, `diemToeic`, `sotaikhoan`.
- Contact: `email`, `soDienThoai`, `httpLink`.
- Dates: `ngaySinh`, `sauHomNay`, `truocHomNay`, and related before/after rules.
- Files: `fileRequired`, `fileName`, `fileType(types)`, `fileLimit(n)`. HTML editor: `requiredHtml` (read the file for the value shape it expects).
- Other: `json`, `arrNumber(max, min)`.

Messages come from the `global.validation.*` locale keys. Read `src/utils/rules.ts` for exact signatures before using an unfamiliar rule. Rules improve input quality but do not replace backend validation.

## Dates

- `src/utils/dayjs.ts` loads the `vi` locale and plugins once. Do not configure dayjs plugins again; import dayjs after the app has run this file.
- Display with `formatDate`, `formatDateTime`, `formatTime`, and the range variants in `src/utils/formatDate.ts`; they take their formats from the app's configuration. `ChucVu` shows `formatDateTime`.
- For values sent to the API, follow that field's contract (full timestamp or a date-only string). Confirm the contract rather than assuming.

## Untrusted HTML, links, and colors

- HTML from users or an editor: apply `sanitizeObject` (`src/utils/utils.ts`, DOMPurify) before `dangerouslySetInnerHTML`.
- Links and colors from data: use `isSafeUrl`, `getSafeHref`, `openSafeUrl`, and `getSafeTagColor` from `src/utils/security.ts`. Do not assign untrusted values directly to `href`, `window.open`, or a tag `color`. The helpers block `javascript:`, `data:`, `vbscript:`, `file:`, and `blob:` URLs.
- Do not log tokens or personal data in the browser console or error reporting.
