# AI-Driven-SDLC

## Giới thiệu

Mô hình **One Shared Framework + Multiple Project Instances + Shared AI Knowledge & Skills**.

### 4 nguyên tắc thiết kế quan trọng

1. **Framework chỉ được xây dựng và quản lý tại một nơi.**
2. **Các Project Instance nằm trong folder `projects/`**, ngang hàng với `framework/`.
3. **AI Rules, Skills, Model Routing và Tool Configuration được quản lý tập trung**, có thể tái sử dụng giữa nhiều dự án và nhiều AI Tool.
4. **Mỗi dự án có thể có nhiều repository code riêng**, nhưng dùng chung tài liệu SDLC, project context và governance.

### Quan hệ giữa các thành phần

| Thành phần | Nội dung |
|---|---|
| **Framework** (`framework/`) | Quy trình SDLC, Governance, Standards, Templates, Human Review Gates |
| **Shared AI** (`shared-ai/`) | Rules, Skills, Agents, Model Routing, Knowledge, Tool Configurations |
| **Project Instances** (`projects/`) | CRM, ERP, Booking... Mỗi dự án có cấu hình và tài liệu riêng, tái sử dụng và tham chiếu Framework và Shared AI |
| **Platform** (`platform/`) | Công cụ tự động hoá: khởi tạo dự án, đồng bộ Framework, kiểm tra cấu trúc (và các module loader/router/engine đang được phát triển) |

**Lợi ích:**

- Đổi quy trình SDLC: chỉ cập nhật Framework.
- Cập nhật quy tắc AI hoặc thêm Skill (ví dụ NestJS, PostgreSQL): mọi dự án dùng chung.
- Không phải copy Framework vào từng dự án.
- Quản lý phiên bản Framework và Shared AI độc lập.

> **Lưu ý:** Cây thư mục bên dưới là cấu trúc logic, không bắt buộc là một Git repository duy nhất. Khi cần phân quyền, versioning và phát hành độc lập, có thể tách `framework`, `shared-ai` và từng project thành các repository riêng.

## Bắt đầu sử dụng

Không cần đọc hết tài liệu. Bắt đầu bằng hai câu hỏi: **"Tôi đang làm vai trò gì?"** và **"Việc tiếp theo của tôi là gì?"**

| Bạn muốn | Mở |
|---|---|
| Chọn vai trò hoặc giai đoạn để xem việc cụ thể | [Guide tương tác](framework/guide/index.html) (mở trực tiếp bằng trình duyệt) |
| Xem dự án đang ở giai đoạn nào, cần làm gì tiếp | Chạy `python platform/scripts/guide-server.py`, rồi chọn tab **Dự án** |
| Tra cứu theo vai trò (PO, BA, Developer, QA...) | [Bảng vai trò](framework/README.md#bắt-đầu-theo-vai-trò) |
| Bắt đầu từ giai đoạn đầu tiên | [01 — Requirement Analysis](framework/01-requirement-analysis/README.md) |
| Biết cách dùng AI cho mọi vai trò | [Quy trình dùng AI](shared-ai/rules/core/ai-usage-flow.md) |
| Tạo dự án mới | `python platform/scripts/init-project.py --name "<Tên>" --slug <slug>` |

Guide chỉ tóm tắt và dẫn link. Quy định chính thức nằm ở `workflow.md`, `human-review.md` của từng giai đoạn và `framework/governance/`.

## Kiến trúc

Ký hiệu: thư mục không có chú thích là đã có trong repo; `(planned)` là thư mục đã được định nghĩa trong thiết kế nhưng chưa có nội dung.

```
ai-driven-sdlc/
│
├── README.md
│
├── framework/                                # FRAMEWORK CHUNG (một nơi duy nhất)
│   │
│   ├── README.md
│   │
│   ├── 01-requirement-analysis/              # 8 giai đoạn SDLC, mỗi giai đoạn có cấu trúc giống nhau:
│   ├── 02-system-design/                     #   README.md, workflow.md, ai-instructions.md, human-review.md
│   ├── 03-task-planning/                     #   templates/, checklists/, inputs/ (nếu có), outputs/
│   ├── 04-development/                       #   (04 có thêm coding-guidelines/)
│   ├── 05-code-review/
│   ├── 06-testing-qa/
│   ├── 07-deployment/
│   ├── 08-monitoring-maintenance/            #   (có thêm operations/: monitoring, alerting, incident, RCA)
│   │
│   ├── governance/
│   │   ├── ai-governance/                    # AI usage/security/responsible AI policy, autonomy level
│   │   ├── autonomy-levels/
│   │   ├── human-review-gates/               # G1–G7 + gate-policy.md
│   │   └── audit-policy/                     # audit trail, retention & access
│   │
│   ├── standards/
│   │   ├── architecture/                     # api-standards, database-standards
│   │   ├── coding/                           # coding-standards, testing-standards
│   │   ├── documentation/
│   │   ├── metadata/                         # id, naming, status, versioning conventions
│   │   └── security/
│   │
│   ├── templates/                            # Template dùng chung cho nhiều giai đoạn
│   │   ├── requirement/                      # (trống)
│   │   ├── design/
│   │   ├── planning/
│   │   ├── development/                      # (trống)
│   │   ├── review/
│   │   ├── testing/                          # (trống)
│   │   └── deployment/                       # (trống)
│   │
│   ├── project-management/                   # charter, status, risk/issue/decision/change log, approval register...
│   └── assets/                               # Hình minh hoạ
│
├── shared-ai/                                # AI RESOURCES CHUNG
│   │
│   ├── rules/                                # core/, sdlc/, engineering/
│   │
│   ├── skills/
│   │   ├── core/                             # code-generation, code-review, documentation,
│   │   │                                     # requirement-analysis, system-design, testing
│   │   ├── architecture/                     # clean-architecture, domain-driven-design, microservices, monolith
│   │   ├── backend/                          # dotnet, laravel, nestjs, nodejs, spring-boot
│   │   ├── frontend/                         # angular, nextjs, react, vue
│   │   ├── database/                         # database-design, database-migration, mongodb, mysql, postgresql, redis
│   │   ├── devops/                           # docker, github-actions, kubernetes, terraform
│   │   └── security/                         # authentication, authorization, owasp
│   │
│   ├── agents/                               # Hướng dẫn agent theo vai trò
│   │   ├── business-analyst/
│   │   ├── solution-architect/
│   │   ├── developer/
│   │   ├── code-reviewer/
│   │   ├── qa-engineer/
│   │   └── devops-engineer/
│   │
│   ├── model-routing/
│   │   ├── task-model-mapping.yaml
│   │   ├── model-profiles.yaml
│   │   ├── effort-policy.yaml
│   │   └── fallback-policy.yaml
│   │
│   ├── knowledge/
│   │   ├── architecture/
│   │   ├── database/
│   │   ├── security/
│   │   └── devops/
│   │
│   └── tool-configs/
│       ├── claude-code/
│       ├── cursor/
│       ├── github-copilot/
│       ├── codex/
│       └── generic/
│
├── projects/                                 # PROJECT INSTANCES (hiện đang trống)
│   │
│   ├── Project-CRM/                          # Cấu trúc dự kiến cho mỗi dự án
│   │   ├── .ai-sdlc/
│   │   │   └── project.yaml                  #   manifest: project, stack, AI resources, autonomy
│   │   ├── .claude/                          #   ví dụ: rules/ và skills/ cho công cụ đã chọn
│   │   ├── docs/                             #   tài liệu SDLC theo 01–08 + project-management/
│   │   ├── crm-backend/                      # Git Repository riêng
│   │   ├── crm-frontend/                     # Git Repository riêng
│   │   └── crm-mobile/                       # Git Repository riêng
│   │
│   ├── Project-ERP/
│   └── Project-Booking/
│
└── platform/                                 # AUTOMATION & INTEGRATION
    │
    ├── README.md
    ├── scripts/                              # Đã có
    │   ├── init-project.py                   #   Tạo Project Instance mới
    │   ├── validate-project.py               #   Kiểm tra cấu trúc & cấu hình dự án
    │   └── sync-framework.py                 #   Đồng bộ template/tài nguyên theo phiên bản Framework
    │
    ├── tool-adapters/                        # (planned)
    ├── skill-loader/                         # Shared and project-local skills
    ├── rule-loader/                          # Shared and project-local rules
    ├── model-router/                         # Static v1 routing policy
    ├── workflow-engine/                      # Local stage state and action gates
    ├── approval-engine/                      # Local approval enforcement API
    └── validators/                           # (planned)
```

## Thành phần chính

| Thư mục | Vai trò | Trạng thái |
|---|---|---|
| `framework/` | Framework chung: 8 giai đoạn SDLC, governance (gồm G1–G7 review gates), standards, templates, project management | Đã có nội dung |
| [shared-ai/](shared-ai/README.md) | Rules, skills, agents, chính sách model routing, knowledge và hướng dẫn tích hợp công cụ | Platform có loader và định tuyến tĩnh; tích hợp với công cụ/provider vẫn cần cấu hình riêng |
| `projects/` | Các project cụ thể, mỗi project có `.ai-sdlc/`, `docs/` và các Git repository riêng | Chưa có project nào |
| [platform/](platform/README.md) | Scripts khởi tạo/kiểm tra/đồng bộ, loader/router và workflow/approval engine | Có API governance chạy local; chưa tích hợp xác thực, repository hoặc CI/CD production |
