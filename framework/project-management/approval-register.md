# Approval Register

Chỉ mục phê duyệt của dự án. Mỗi mục dẫn đến hồ sơ quyết định gốc; bảng này không cấp quyền hoặc thay thế audit.

No entries

| Approval ID | Loại / Gate hoặc chủ đề | Artifact version / SHA | Trạng thái | Hồ sơ quyết định / audit |
|---|---|---|---|---|

- **Gate:** tra vai trò, tiêu chí và trạng thái hợp lệ ở [Gate Policy](README.md#nguồn-chuẩn). Link đến review/audit chính thức ghi danh tính, vai trò và quyết định của từng người duyệt, thời điểm, bằng chứng và đích được duyệt nếu áp dụng. `Conditional` không cho qua Gate; nếu còn điều kiện bắt buộc cần sửa, ghi `changes_requested` theo policy.
- **Quản trị dự án:** dùng mẫu phê duyệt quản trị để ghi quyết định về charter, baseline, change hoặc closeout theo thẩm quyền trong charter. Đây không phải quyết định Gate.
- Khi quyết định bị thay thế hoặc cần duyệt lại, giữ lịch sử và liên kết bản ghi mới; không sửa hoặc xóa quyết định gốc.
