# Checklists – Deployment

## Kiến trúc
Thư mục tách kiểm tra readiness, quyền thực thi Production và xác minh sau triển khai, cùng các kiểm tra chuyên biệt về bảo mật và vận hành:

```
checklists/
├── pre-deployment-checklist.md          → readiness trước khi xin G6
├── production-authorization-checklist.md → sau G6, ngay trước khi chạy Production
├── security-deployment-checklist.md     → xuyên suốt, tập trung bảo mật
├── post-deployment-checklist.md         → sau khi deploy
└── production-readiness-checklist.md    → trước khi nhận Production
```

Với **Production**, thứ tự là **readiness → Release Manager phê duyệt G6 → kiểm tra quyền ngay trước khi chạy**. Checklist readiness là bằng chứng đầu vào, không thay thế G6 hay kiểm tra quyền. Với **non-production**, dùng các mục readiness phù hợp và kiểm tra quyền theo policy của môi trường; G6 không áp dụng.

## Vai trò từng file
| File | Vai trò | Thời điểm dùng | Người thường dùng |
|---|---|---|---|
| [Kiểm tra readiness](pre-deployment-checklist.md) | Xác nhận candidate, artifact, môi trường, dữ liệu và vận hành đã sẵn sàng | Sau G5; trước G6 nếu đích là Production | DevOps, Release Engineer |
| [Kiểm tra quyền thực thi Production](production-authorization-checklist.md) | Đối chiếu phê duyệt, authorization và lượt bắt đầu với yêu cầu hiện tại | Sau G6, ngay trước khi thực thi Production | DevOps, Release Engineer |
| `security-deployment-checklist.md` | Kiểm tra identity, secrets, provenance, network, TLS và audit logging theo policy bảo mật | Trước và trong deploy Production | Security, DevOps |
| `post-deployment-checklist.md` | Xác minh phiên bản đang chạy, health, smoke test, metrics và bàn giao | Ngay sau deploy | QA, DevOps, SRE |
| `production-readiness-checklist.md` | Đảm bảo service có owner, SLO, dashboard, runbook, backup và đội vận hành chấp nhận | Trước lần đưa lên Production đầu tiên hoặc khi thay đổi lớn | SRE/Operations, Service owner |
