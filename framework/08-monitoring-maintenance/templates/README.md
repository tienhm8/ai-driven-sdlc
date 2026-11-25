# Templates – Monitoring & Maintenance

## 1. Kiến trúc

```
templates/
├── monitoring-report.md      # Báo cáo giám sát theo kỳ
├── incident-report.md        # Hồ sơ một sự cố
├── postmortem.md             # Phân tích sau sự cố (blameless)
├── maintenance-plan.md       # Kế hoạch và kết quả bảo trì
└── improvement-backlog.md    # Backlog cải tiến độ tin cậy
```

Quan hệ giữa các template:

```
Monitoring report (định kỳ) ───────────────────────┐
Incident report / Postmortem (nếu cần) ────────────┼─► Improvement backlog
Maintenance plan và kết quả ───────────────────────┘   (khi có follow-up)
```

Template là khung trống; hồ sơ thực tế nằm trong `outputs/` của project instance theo [quy ước đầu ra](../outputs/README.md).

## 2. Vai trò từng file

| File | Vai trò | Đầu ra/nơi lưu |
|---|---|---|
| `monitoring-report.md` | Tổng hợp trạng thái sức khỏe, SLI/SLO, alert quality, capacity và khuyến nghị theo kỳ | `outputs/<service>/<env>/<period>/monitoring-report.md` |
| `incident-report.md` | Ghi metadata, tác động, timeline, mitigation, phê duyệt và tiêu chí đóng sự cố | `outputs/<service>/<env>/<incident-id>/incident-report.md` |
| `postmortem.md` | Phân tích nguyên nhân gốc và yếu tố góp phần, tách sự kiện đã xác minh khỏi giả thuyết, đưa ra action items | `outputs/<service>/<env>/<incident-id>/postmortem.md` |
| `maintenance-plan.md` | Mô tả phạm vi, hoạt động, kiểm tra trước/trong/sau, rollback và phê duyệt của một đợt bảo trì | `outputs/<service>/<env>/<period>/maintenance-plan.md` |
| `improvement-backlog.md` | Theo dõi vấn đề/cơ hội cải tiến, ưu tiên, owner và bằng chứng xác minh trước khi đóng | `outputs/<service>/<env>/<period>/improvement-backlog.md` |

## Quy ước
- Không ghi secret, credential, PII thô vào template; dùng dữ liệu đã redact.
- Mọi dòng thời gian ghi rõ timezone; mọi quyết định ghi người phê duyệt và timestamp.
- Postmortem phải không quy kết cá nhân.
- Ô để trống là dữ liệu chưa có, không được điền giả định thay thế.
