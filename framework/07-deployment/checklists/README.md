# Checklists – Deployment

## Kiến trúc
Thư mục gồm 4 checklist độc lập, bao phủ 3 mốc của vòng đời triển khai và một góc nhìn bảo mật:

```
checklists/
├── pre-deployment-checklist.md          → trước khi deploy
├── security-deployment-checklist.md     → xuyên suốt, tập trung bảo mật
├── post-deployment-checklist.md         → sau khi deploy
└── production-readiness-checklist.md    → trước khi nhận Production
```

Mỗi file dùng định dạng Markdown checkbox (`- [ ]`) để tick trực tiếp. Checklist không thay thế G6: G6 do Release Manager phê duyệt, còn checklist là bằng chứng đầu vào.

## Vai trò từng file
| File | Vai trò | Thời điểm dùng | Người thường dùng |
|---|---|---|---|
| `pre-deployment-checklist.md` | Xác nhận release candidate, artifact, môi trường, dữ liệu và vận hành đã sẵn sàng trước khi thực thi | Sau G5, trước G6 | DevOps, Release Engineer |
| `security-deployment-checklist.md` | Kiểm tra identity, secrets, provenance, network, TLS và audit logging theo policy bảo mật | Trước và trong deploy Production | Security, DevOps |
| `post-deployment-checklist.md` | Xác minh phiên bản đang chạy, health, smoke test, metrics và bàn giao | Ngay sau deploy | QA, DevOps, SRE |
| `production-readiness-checklist.md` | Đảm bảo service có owner, SLO, dashboard, runbook, backup và đội vận hành chấp nhận | Trước lần đưa lên Production đầu tiên hoặc khi thay đổi lớn | SRE/Operations, Service owner |
