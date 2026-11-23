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
Maintenance plan ─────────────┐
Monitoring report ──► Incident report ──► Postmortem ──► Improvement backlog
(định kỳ)             (từng sự cố)        (RCA/actions)   (theo dõi đến khi verify)
```

Template là khung trống; sản phẩm thực tế được lưu trong `outputs/` (xem `outputs/README.md`).

## 2. Vai trò từng file

| File | Vai trò | Đầu ra/nơi lưu |
|---|---|---|
| `monitoring-report.md` | Tổng hợp trạng thái sức khỏe, SLI/SLO, alert quality, capacity và khuyến nghị theo kỳ | `outputs/<service>/<period>/monitoring-report.md` |
| `incident-report.md` | Ghi metadata, tác động, timeline, mitigation, phê duyệt và tiêu chí đóng sự cố | `outputs/<service>/<incident-id>/incident-report.md` |
| `postmortem.md` | Phân tích nguyên nhân gốc và yếu tố góp phần, tách sự kiện đã xác minh khỏi giả thuyết, đưa ra action items | `outputs/<service>/<incident-id>/postmortem.md` |
| `maintenance-plan.md` | Mô tả phạm vi, hoạt động, kiểm tra trước/trong/sau, rollback và phê duyệt của một đợt bảo trì | `outputs/<service>/<period>/maintenance-plan.md` |
| `improvement-backlog.md` | Theo dõi vấn đề/cơ hội cải tiến, ưu tiên, owner và bằng chứng xác minh trước khi đóng | `outputs/<service>/<period>/improvement-backlog.md` |

## Quy ước
- Không ghi secret, credential, PII thô vào template; dùng dữ liệu đã redact.
- Mọi dòng thời gian ghi rõ timezone; mọi quyết định ghi người phê duyệt và timestamp.
- Postmortem phải không quy kết cá nhân.
- Ô để trống là dữ liệu chưa có, không được điền giả định thay thế.
