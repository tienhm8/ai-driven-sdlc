# Templates – Deployment

## Kiến trúc
Thư mục gồm các biểu mẫu chuẩn, được điền khi triển khai một release. Các biểu mẫu liên kết theo chuỗi: **release note → plan → checklist → rollback → G6 approval → deployment record**.

```
templates/
├── release-note.md            → thông báo nội dung release (cho người dùng và stakeholder)
├── deployment-plan.md         → kế hoạch thực thi chi tiết
├── deployment-checklist.md    → bảng kết quả và liên kết checklist chuyên biệt
├── rollback-plan.md           → kế hoạch khôi phục khi release lỗi
└── production-approval.md     → biểu mẫu phê duyệt G6 (chỉ quyết định, liên kết tới deployment record)

../../templates/deployment/deployment-record.md → deployment record dùng chung: thực thi, sai lệch, sự cố, bàn giao Stage 08
```

Canonical: plan, rollback plan, release note và G6 nằm ở thư mục này; các file cùng loại trong `framework/templates/deployment/` chỉ là liên kết (deployment record là canonical dùng chung ở đó).

Quy ước: sao chép file sang thư mục `outputs/<project>/<release-ID>/` rồi điền; không sửa trực tiếp file mẫu.

## Vai trò từng file
| File | Vai trò | Người điền chính | Thời điểm |
|---|---|---|---|
| `release-note.md` | Tổng hợp tính năng, cải tiến, bug fix, tác động API/DB/config và cách rollback cho release | Release Engineer, QA | Trước và sau deploy |
| `deployment-plan.md` | Mô tả phạm vi, điều kiện tiên quyết, chiến lược, các bước thực thi, verification và liên lạc | DevOps, Deployment owner | Trước G6 |
| [Deployment Checklist](deployment-checklist.md) | Tổng hợp Pass/Fail/N/A và dẫn tới checklist chuyên biệt đã điền | DevOps, QA | Trước và sau deploy |
| `rollback-plan.md` | Định nghĩa trigger, ràng buộc, các bước rollback, khôi phục database và tiêu chí thành công | DevOps, SRE, service owner | Trước deploy |
| `production-approval.md` | Biểu mẫu G6: ràng buộc artifact SHA-256, canonical target, review package SHA-256, evidence, rủi ro, quyết định Go/No-Go. Chỉ người có thẩm quyền ký; AI không được phê duyệt | Release Manager | Ngay trước Production |
| [Deployment Record](../../templates/deployment/deployment-record.md) (mẫu dùng chung) | Thực thi so với kế hoạch, xác minh và bàn giao; tách bàn giao sự cố khỏi bàn giao release sang Stage 08 | Deployment owner, SRE | Trong và sau deploy |
