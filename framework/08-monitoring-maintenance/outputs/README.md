# Outputs – Monitoring & Maintenance

## 1. Kiến trúc

```
outputs/
├── README.md                          # Quy ước tổ chức và lưu trữ
├── monitoring-report-example.md       # Ví dụ (giả lập)
├── incident-report-example.md         # Ví dụ (giả lập)
└── postmortem-example.md              # Ví dụ (giả lập)
```

Framework chỉ giữ hướng dẫn và ví dụ giả lập. Hồ sơ vận hành thực tế lưu trong `docs/08-monitoring-maintenance/outputs/` của project instance.

## 2. Vai trò từng file

| File | Vai trò |
|---|---|
| `README.md` | Liệt kê loại sản phẩm cần tạo (báo cáo, hồ sơ sự cố, postmortem, maintenance, backlog, evidence); quy định cách đặt thư mục và nguyên tắc không ghi đè lịch sử |
| `monitoring-report-example.md` | Minh họa báo cáo giám sát theo kỳ từ template `monitoring-report.md`, kèm caveat rằng số liệu là giả lập |
| `incident-report-example.md` | Minh họa hồ sơ sự cố (timeline, rollback, phê duyệt placeholder) từ template `incident-report.md` |
| `postmortem-example.md` | Minh họa postmortem: tách giả thuyết khỏi kết luận, action items có owner và cách xác minh |

## Quy ước
- Trong project instance, dùng `outputs/<service>/<env>/<period-or-incident-id>/`. Ví dụ:
  - `outputs/payments/production/2026-Q4/monitoring-report.md`
  - `outputs/payments/staging/INC-2026-0042/incident-report.md`
- Không ghi đè lịch sử; tạo version mới và giữ evidence nguồn.
- Dẫn link tới bằng chứng nhạy cảm trong kho có kiểm soát truy cập và retention theo policy; không sao chép secret, PII thô, raw logs nhạy cảm hoặc production dump vào repo.
- File `*-example.md` chỉ minh họa, không phải bằng chứng production.
