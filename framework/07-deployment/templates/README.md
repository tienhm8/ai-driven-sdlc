# Templates – Deployment

## Kiến trúc
Thư mục gồm các biểu mẫu chuẩn, được điền khi triển khai một release. Các biểu mẫu liên kết theo chuỗi: **release note → plan → checklist → rollback → G6 approval**.

```
templates/
├── release-note.md            → thông báo nội dung release (cho người dùng và stakeholder)
├── deployment-plan.md         → kế hoạch thực thi chi tiết
├── deployment-checklist.md    → checklist tổng hợp theo giai đoạn A–E
├── rollback-plan.md           → kế hoạch khôi phục khi release lỗi
└── production-approval.md     → biểu mẫu phê duyệt G6 và bản ghi thực thi
```

Quy ước: sao chép file sang thư mục `outputs/<project>/<release-ID>/` rồi điền; không sửa trực tiếp file mẫu.

## Vai trò từng file
| File | Vai trò | Người điền chính | Thời điểm |
|---|---|---|---|
| `release-note.md` | Tổng hợp tính năng, cải tiến, bug fix, tác động API/DB/config và cách rollback cho release | Release Engineer, QA | Trước và sau deploy |
| `deployment-plan.md` | Mô tả phạm vi, điều kiện tiên quyết, chiến lược, các bước thực thi, verification và liên lạc | DevOps, Deployment owner | Trước G6 |
| `deployment-checklist.md` | Kiểm tra định kỳ theo 5 nhóm (định danh, nền tảng, dữ liệu, thực thi, đóng) kèm bảng Pass/Fail/N/A | DevOps, QA | Trước và sau deploy |
| `rollback-plan.md` | Định nghĩa trigger, ràng buộc, các bước rollback, khôi phục database và tiêu chí thành công | DevOps, SRE, service owner | Trước deploy |
| `production-approval.md` | Biểu mẫu G6: đánh giá evidence, rủi ro, quyết định Go/No-Go và bản ghi thực thi. Chỉ người có thẩm quyền ký; AI không được phê duyệt | Release Manager | Ngay trước Production |
