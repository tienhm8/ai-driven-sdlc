# Checklists – Code Review

`checklists/` chứa các danh sách kiểm tra theo từng khía cạnh của code review. Checklist hỗ trợ reviewer không bỏ sót hạng mục; không thay thế đánh giá theo ngữ cảnh.

## Kiến trúc
```text
checklists/
├── code-quality-checklist.md     # Chất lượng code tổng quát
├── security-checklist.md         # Bảo mật
├── performance-checklist.md      # Hiệu năng
└── merge-approval-checklist.md   # Điều kiện phê duyệt G4 trước khi merge
```

Quan hệ với các thành phần khác:
- Checklist chi tiết hơn được dùng kèm `templates/code-review-checklist.md` (tổng hợp) và `templates/security-review.md` (chuyên sâu bảo mật).
- Kết quả đánh giá từng mục ghi vào `templates/review-report.md` (mục *Checks*) và `outputs/`.
- `merge-approval-checklist.md` là điều kiện đầu vào của Human Review Gate G4 (xem `human-review.md`).

## Vai trò từng file
| File | Vai trò | Khi nào dùng |
|---|---|---|
| `code-quality-checklist.md` | Kiểm tra scope, logic nghiệp vụ, error handling, naming, coupling, log, test và tài liệu | Mọi PR |
| `security-checklist.md` | Kiểm tra authentication/authorization, validation, injection, secret, dữ liệu nhạy cảm, error disclosure, dependency | PR chạm input, quyền truy cập, dữ liệu nhạy cảm hoặc dependency mới |
| `performance-checklist.md` | Kiểm tra N+1 query, pagination, index, blocking I/O, cache, resource leak, timeout/retry | PR chạm truy vấn dữ liệu, critical path hoặc được tuyên bố là tối ưu |
| `merge-approval-checklist.md` | Xác nhận điều kiện G4: đúng PR/commit, finding đáp ứng quy tắc chặn merge, CI đạt, approver là người | Trước khi merge; AI không tự đánh dấu hoàn tất G4 |

## Nguyên tắc sử dụng
- Đánh dấu Pass / Fail / N/A và ghi bằng chứng (vị trí file, kết quả CI, test).
- Checklist chỉ là điểm xuất phát; reviewer vẫn phải đánh giá ngữ cảnh thay đổi.
- Khi head SHA thay đổi đáng kể, đánh giá lại các mục đã đánh dấu.
