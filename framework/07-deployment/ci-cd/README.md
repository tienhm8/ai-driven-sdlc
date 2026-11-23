# CI/CD – Deployment

## Kiến trúc
Thư mục gồm hai tài liệu tiêu chuẩn, tách theo hai câu hỏi: **pipeline được xây dựng thế nào** và **release được đưa ra môi trường theo chiến lược nào**.

```
ci-cd/
├── pipeline-guidelines.md   → "Làm sao" – pipeline: stages, trigger, artifact, secrets, độ tin cậy
└── deployment-strategy.md   → "Đưa ra thế nào" – chiến lược: Recreate, Rolling, Blue-Green, Canary, Feature flags
```

Luồng đọc gợi ý: `pipeline-guidelines.md` (build và promote artifact) → `deployment-strategy.md` (chọn cách rollout) → `templates/deployment-plan.md` (áp dụng vào kế hoạch cụ thể).

## Vai trò từng file
| File | Vai trò | Người dùng chính |
|---|---|---|
| `pipeline-guidelines.md` | Quy định 10 stage chuẩn, nguyên tắc build once/promote artifact, kiểm soát trigger và branch, quản lý secrets và anti-pattern cần tránh | DevOps, Developer/Release Engineer |
| `deployment-strategy.md` | So sánh các chiến lược triển khai, hướng dẫn xử lý database theo expand-and-contract, định nghĩa kiểm soát progressive rollout và quyết định rollback | DevOps, Release Manager, SRE |

Lưu ý: hai file này là tiêu chuẩn chung; cần đối chiếu với nền tảng CI/CD thực tế trước khi áp dụng.
