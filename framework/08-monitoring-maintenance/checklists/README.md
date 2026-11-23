# Checklists – Monitoring & Maintenance

## 1. Kiến trúc

```
checklists/
├── monitoring-readiness-checklist.md   # Sẵn sàng giám sát trước/sau Production
├── incident-response-checklist.md      # Quy trình xử lý sự cố
├── maintenance-checklist.md            # Bảo trì có kế hoạch
├── recovery-readiness-checklist.md     # Sẵn sàng backup, restore, DR
└── security-operations-checklist.md    # Vận hành bảo mật
```

Mỗi checklist là danh sách `- [ ]` ngắn gọn, dùng để xác nhận từng điều kiện trước khi chuyển bước. Các checklist độc lập nhưng thường dùng cùng lúc: ví dụ sự cố bảo mật dùng `incident-response` và `security-operations`; bảo trì có rủi ro dùng `maintenance` và `recovery-readiness`.

Luồng sử dụng điển hình:

```
Trước Production  →  monitoring-readiness, recovery-readiness
Vận hành định kỳ  →  maintenance
Khi có sự cố      →  incident-response (+ security-operations nếu liên quan bảo mật)
```

## 2. Vai trò từng file

| File | Vai trò | Dùng khi |
|---|---|---|
| `monitoring-readiness-checklist.md` | Xác nhận dịch vụ đã có SLI/SLO, metrics, logs, traces, dashboard, alert, runbook và chính sách dữ liệu | Trước khi đưa dịch vụ lên Production, hoặc khi thêm dịch vụ/dependency mới |
| `incident-response-checklist.md` | Hướng dẫn các bước từ ghi nhận sự cố, phân công IC, mitigation, G7 approval đến xác minh khôi phục | Khi sự cố được khai báo và trong suốt quá trình xử lý |
| `maintenance-checklist.md` | Đảm bảo bảo trì có change approval, baseline, rollback/abort criteria và kiểm tra sau thay đổi | Trước, trong và sau mỗi maintenance window |
| `recovery-readiness-checklist.md` | Xác nhận RTO/RPO, backup, restore test, failover/DR runbook và tiêu chí quay lại primary | Định kỳ kiểm tra khả năng khôi phục và trước các thay đổi có rủi ro dữ liệu |
| `security-operations-checklist.md` | Kiểm soát cảnh báo bảo mật, quyền truy cập evidence, redaction, containment và phê duyệt rotation/đóng sự cố | Khi có cảnh báo hoặc sự cố bảo mật/dữ liệu nhạy cảm |

## Quy ước
- Checklist là công cụ xác nhận, không thay thế runbook hay quyết định của người có thẩm quyền.
- Đánh dấu `[x]` chỉ khi có evidence; ghi lý do nếu bỏ qua một mục.
- Mục không áp dụng: ghi rõ "N/A" kèm lý do, không xóa.
