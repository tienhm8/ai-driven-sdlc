# 02 — System Design

## Mục đích
Chuyển Requirement Baseline đã được PO phê duyệt ở giai đoạn 01 thành bộ thiết kế kỹ thuật đủ rõ để lập kế hoạch, phát triển, kiểm thử, triển khai và vận hành.

- **AI:** đề xuất kiến trúc, API, database, data model, luồng xử lý và security design; tạo bản nháp và kiểm tra tính nhất quán.
- **Con người:** Solution Architect / Architect / Tech Lead đánh giá, điều chỉnh và phê duyệt các quyết định quan trọng.
- **Gate:** G2 — không được coi thiết kế là baseline chính thức hoặc chuyển G3 nếu chưa có phê duyệt hợp lệ.

## Cấu trúc
```text
02-system-design/
├── README.md
├── workflow.md
├── ai-instructions.md
├── human-review.md
├── inputs/README.md
├── templates/
│   ├── system-architecture.md
│   ├── architecture-decision-record.md
│   ├── api-specification.md
│   ├── database-design.md
│   ├── data-model.md
│   ├── sequence-diagram.md
│   └── security-design.md
├── checklists/
│   ├── architecture-review-checklist.md
│   ├── api-review-checklist.md
│   ├── database-data-review-checklist.md
│   ├── security-review-checklist.md
│   └── g2-design-approval-checklist.md
└── outputs/
    ├── README.md
    └── design-package-index.md
```

## Tài liệu hướng dẫn ở thư mục gốc
| File | Vai trò |
|---|---|
| `workflow.md` | Các bước thực hiện giai đoạn 02 |
| `ai-instructions.md` | Hướng dẫn AI khi tạo thiết kế |
| `human-review.md` | Trách nhiệm review và phê duyệt của con người |

## Vai trò thư mục
| Folder | Vai trò | Quy tắc |
|---|---|---|
| `inputs/` | Đầu vào đã duyệt từ 01 và bối cảnh/ràng buộc liên quan | Tham chiếu đúng version của requirement baseline |
| `templates/` | Biểu mẫu tạo tài liệu thiết kế | Không phải output dự án |
| `checklists/` | Tiêu chí kiểm tra chất lượng và tính đầy đủ | Lưu kết quả, reviewer, bằng chứng, ngoại lệ |
| `outputs/` | Tài liệu thiết kế thực tế của project | Chỉ Approved/Baselined sau G2 |

## Inputs
Nguồn chính là `01-requirement-analysis/outputs` hoặc vị trí tài liệu dự án tương ứng: approved requirements, User Stories, Acceptance Criteria, FR/NFR, business rules, scope, assumptions, constraints, dependencies, integration/data requirements. Có thể bổ sung kiến trúc hiện trạng và technology constraints cho dự án đang vận hành.

Không cần sao chép toàn bộ tài liệu 01. Ưu tiên manifest/link + ID/version/approval reference. Nếu thiếu yêu cầu ảnh hưởng thiết kế, ghi open question hoặc assumption và yêu cầu BA/PO xác nhận; không tự suy diễn thành yêu cầu chính thức.

## Bộ outputs
1. System Architecture.
2. ADR(s) cho quyết định kiến trúc trọng yếu.
3. API Specification.
4. Database Design.
5. Data Model.
6. Sequence Diagrams / Key Flows.
7. Security Design.
8. Review evidence và G2 approval record.

Artifact không áp dụng phải ghi `N/A` và lý do trong package index.

## Document control
Mỗi artifact cần ID, version, status, owner, date, requirement references. Trạng thái gợi ý: `Draft → In Review → Approved → Baselined → Superseded`. Không sửa âm thầm bản đã duyệt; tăng version, ghi change reason và đánh giá tác động.

## G2 — Human Review Gate
Solution Architect là approver chính; phối hợp Tech Lead, Security/Data owner khi cần. G2 xác nhận architecture, API, data, key flows, security/privacy, NFR, risks và traceability. Critical/High findings phải được xử lý hoặc có waiver đúng thẩm quyền. AI không được tự phê duyệt G2.

## Handoff sang 03 — Task Planning
Chuyển design package version đã Approved, component boundaries, API/schema/flow, migration/integration tasks, security/NFR tasks, dependencies, risks, spikes/PoC và G2 approval reference.

Áp dụng `framework/standards/architecture/`, `security/`, `documentation/` và governance policies. Policy/standard được phê duyệt có hiệu lực cao hơn template.
