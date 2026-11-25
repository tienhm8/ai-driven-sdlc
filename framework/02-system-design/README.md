# 02 — System Design

## Mục đích
Chuyển Requirement Baseline đã được PO phê duyệt ở giai đoạn 01 thành bộ thiết kế kỹ thuật đủ rõ để lập kế hoạch, phát triển, kiểm thử, triển khai và vận hành.

- **AI:** đề xuất kiến trúc, API, database, data model, luồng xử lý và security design; tạo bản nháp và kiểm tra tính nhất quán.
- **Con người:** Solution Architect / Architect / Tech Lead đánh giá, điều chỉnh và phê duyệt các quyết định quan trọng.
- **Gate:** G2 — chỉ bàn giao cho Stage 03 phiên bản design package đã được chốt làm baseline và có bằng chứng G2 hợp lệ cho đúng phiên bản đó.

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
| `outputs/` | Tài liệu thiết kế thực tế của project | Baseline bàn giao phải có G2 hợp lệ cho đúng phiên bản gói |

## Inputs
Nguồn chính là các deliverable đã duyệt trong `01-requirement-analysis/outputs/` theo danh mục và cấu trúc tại `01-requirement-analysis/outputs/README.md`: BRD, Scope Definition, FRS, NFR, User Stories/Use Cases, Acceptance Criteria, Business Rules, RTM và register assumptions/constraints/dependencies/risks. Dùng manifest/link kèm ID, version và G1 approval reference. Có thể bổ sung kiến trúc hiện trạng và technology constraints cho dự án đang vận hành.

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
Mỗi artifact cần ID, version, status, owner, date, requirement references. Trạng thái gợi ý: `Draft → In Review → Approved → Superseded`; baseline là vai trò của phiên bản gói đã chốt, không phải trạng thái artifact riêng. Không sửa âm thầm bản đã duyệt; tăng version, ghi change reason và đánh giá tác động.

## G2 — Human Review Gate
Solution Architect được ủy quyền là approver G2; Tech Lead và các chuyên gia ghi kết luận theo phạm vi, với phê duyệt chuyên môn bắt buộc khi policy hoặc phạm vi yêu cầu. G2 xác nhận architecture, API, data, key flows, security/privacy, NFR, risks và traceability. Critical/High findings phải được xử lý hoặc có waiver đúng thẩm quyền. G2 chỉ được `Approved` sau khi đáp ứng điều kiện gate và có đủ phê duyệt chuyên môn bắt buộc. Nếu còn điều kiện cần đóng, ghi `Changes Requested`; nếu thiếu bằng chứng hoặc phê duyệt bắt buộc, ghi `Blocked`. Không bàn giao chính thức cho đến khi G2 được `Approved`. Khi G2 Approved, Solution Architect chốt đúng phiên bản gói đã được phê duyệt làm baseline và ghi phiên bản, quyết định, waiver hợp lệ (nếu có), người duyệt và thời điểm trong approval record G2; package index chỉ tham chiếu hồ sơ đó. AI không được tự phê duyệt G2.

## Handoff sang 03 — Task Planning
Chuyển đúng phiên bản design package đã chốt làm baseline cùng bằng chứng G2 hợp lệ cho phiên bản đó, component boundaries, API/schema/flow, migration/integration tasks, security/NFR tasks, dependencies, risks và spikes/PoC. Stage 03 xác minh đầu vào và lập kế hoạch; G3 phê duyệt readiness của kế hoạch/task trước khi coding tại Stage 04. Luồng: **G2 → Stage 03 Task Planning → G3 → coding**. Khi dùng workflow engine, áp dụng điều kiện hoàn thành Stage 02 tại mục 2.11 của `workflow.md` trước khi bàn giao.

Áp dụng `framework/standards/architecture/`, `security/`, `documentation/` và governance policies. Policy/standard được phê duyệt có hiệu lực cao hơn template.
