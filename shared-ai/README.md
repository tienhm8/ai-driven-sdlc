# Shared AI

Tài nguyên AI dùng chung cho các dự án áp dụng [SDLC Framework](../framework/README.md).

| Nhóm | Dùng khi |
|---|---|
| [Rules](rules/core/README.md) | Áp dụng ràng buộc chung, [SDLC](rules/sdlc/README.md) và [engineering](rules/engineering/README.md). |
| [Skills](skills/) | Nạp `SKILL.md` theo công việc và stack thực tế; không nạp toàn bộ thư viện. |
| [Agents](agents/) | Chọn `AGENT.md` theo vai trò; đây là hướng dẫn, không phải quyền thực thi. |
| [Model routing](model-routing/README.md) | Chọn profile và effort; ánh xạ runtime phải được cấu hình riêng. |
| [Knowledge](knowledge/) | Tra cứu quyết định kiến trúc, dữ liệu, bảo mật và vận hành. |
| [Tool configs](tool-configs/generic/README.md) | Tích hợp thủ công theo công cụ khi loader chưa có. |

## Kiến trúc

```
shared-ai/
├── rules/                  # Ràng buộc chung: core/, sdlc/, engineering/
├── skills/                 # SKILL.md theo nhóm
│   ├── core/               # code-generation, code-review, documentation, requirement-analysis, system-design, testing
│   ├── architecture/       # clean-architecture, domain-driven-design, microservices, monolith
│   ├── backend/            # nestjs, nodejs
│   ├── frontend/           # react, umi-max
│   ├── database/           # database-design, database-migration, mongodb, postgresql, redis
│   ├── devops/             # docker, gitlab-ci, kubernetes, terraform
│   └── security/           # authentication, authorization, owasp
├── agents/                 # AGENT.md theo vai trò: business-analyst, solution-architect, developer,
│                           #   code-reviewer, qa-engineer, devops-engineer
├── model-routing/          # task-model-mapping, model-profiles, effort-policy, fallback-policy (YAML)
├── knowledge/              # Tài liệu tra cứu: architecture, database, security, devops
└── tool-configs/           # Hướng dẫn tích hợp theo công cụ: claude-code, codex, cursor, github-copilot, generic
```

Danh mục skill kỹ thuật hiện tập trung vào hai codebase NestJS và Umi Max/React. Chỉ thêm công nghệ khi có nhu cầu thực tế; phạm vi danh mục skill không giới hạn quy trình, tiêu chuẩn hay governance của Framework.

Ranh giới: `rules/` và `agents/` là hướng dẫn, không cấp quyền thực thi. Loader và ánh xạ model/tool chạy ở `platform/`; khi chưa có loader, dùng `tool-configs/` để tích hợp thủ công.

## Bắt đầu

1. Đọc project context, stack, phạm vi và phiên bản framework/shared resources được dự án chọn.
2. Áp dụng governance của framework, rules chung, rồi rules dự án tương thích. Khi xung đột về quyền, chọn giới hạn nghiêm hơn; nếu không xác định được, dừng hành động liên quan và báo người phụ trách.
3. Chọn vai trò và skill theo task. Ví dụ: thay endpoint NestJS → Developer + NestJS + Testing; đọc quy trình Development và yêu cầu review tương ứng.
4. Ghi lại kết quả, lệnh kiểm tra đã chạy, việc chưa xác minh và gate cần con người quyết định.

### Chọn hướng dẫn theo task

Tên vai trò dưới đây giúp chọn ngữ cảnh làm việc; không cấp quyền thực thi hoặc phê duyệt. Khi chưa có agent riêng, dùng vai trò của stage và đọc tài liệu framework được dẫn thay vì chọn agent gần giống rồi mở rộng quyền.

| Task | Vai trò AI hỗ trợ | Skill hoặc tài liệu làm việc |
|---|---|---|
| Stage 03 — chia task, rà phụ thuộc, chuẩn bị gói G3 | Technical Project Planner / Scrum Assistant (chưa có agent riêng) | [Hướng dẫn AI](../framework/03-task-planning/ai-instructions.md) và [hợp đồng đầu ra](../framework/03-task-planning/outputs/planning-output-contract.md). |
| Stage 07 — chuẩn bị release, rollback và bàn giao | [DevOps Engineer](agents/devops-engineer/AGENT.md) | [Hướng dẫn AI](../framework/07-deployment/ai-instructions.md) và [đầu ra triển khai](../framework/07-deployment/outputs/README.md). |
| Stage 08 — rà monitoring, phân tích incident và chuẩn bị postmortem | SRE / Operations Engineer (vai trò Stage 08; chưa có agent riêng) | [Hướng dẫn AI](../framework/08-monitoring-maintenance/ai-instructions.md), [quy trình incident](../framework/08-monitoring-maintenance/operations/incident-management.md) và [đầu ra vận hành](../framework/08-monitoring-maintenance/outputs/README.md). |

Không tự cài adapter, cấp quyền, gửi dữ liệu ra ngoài hay gọi provider chỉ vì tài nguyên này được nạp. Khi cập nhật, giữ ID ổn định, kiểm tra liên kết và ghi rõ thay đổi không tương thích trước khi dự án nâng phiên bản.
