# Outputs – Monitoring & Maintenance

## 1. Kiến trúc

```
outputs/
├── README.md                          # Quy ước tổ chức và lưu trữ
├── monitoring-report-example.md       # Ví dụ (giả lập)
├── incident-report-example.md         # Ví dụ (giả lập)
└── postmortem-example.md              # Ví dụ (giả lập)

Sản phẩm thực tế (tạo khi vận hành), theo quy ước:
outputs/<service>/<period>/            # ví dụ: outputs/payments/2026-Q4/
outputs/<service>/<incident-id>/       # ví dụ: outputs/payments/INC-2026-0042/
```

Các file `*-example.md` chỉ minh họa cách điền template, không phải bằng chứng production. Sản phẩm thật được tổ chức theo service và kỳ báo cáo hoặc theo incident ID.

## 2. Vai trò từng file

| File | Vai trò |
|---|---|
| `README.md` | Liệt kê loại sản phẩm cần tạo (báo cáo, hồ sơ sự cố, postmortem, maintenance, backlog, evidence); quy định cách đặt thư mục và nguyên tắc không ghi đè lịch sử |
| `monitoring-report-example.md` | Minh họa báo cáo giám sát theo kỳ từ template `monitoring-report.md`, kèm caveat rằng số liệu là giả lập |
| `incident-report-example.md` | Minh họa hồ sơ sự cố (timeline, rollback, phê duyệt placeholder) từ template `incident-report.md` |
| `postmortem-example.md` | Minh họa postmortem: tách giả thuyết khỏi kết luận, action items có owner và cách xác minh |

## Quy ước
- Tổ chức theo service/environment/period hoặc incident ID, ví dụ:
  `outputs/payments/2026-Q4/monitoring-report.md`
  `outputs/payments/INC-2026-0042/incident-report.md`
- Không ghi đè lịch sử; tạo version mới và giữ evidence nguồn.
- Bảo vệ dữ liệu theo access/retention policy.
- File `*-example.md` chỉ minh họa, không phải bằng chứng production.
