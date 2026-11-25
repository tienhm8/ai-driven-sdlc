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

Dùng [input manifest](inputs/README.md) làm điểm tham chiếu chuẩn, gồm đường dẫn tới đúng phiên bản RTM đã duyệt. Giữ mọi yêu cầu thuộc baseline G1, kể cả hiệu năng và bảo mật; chỉ tài liệu tham khảo bổ sung là tùy bối cảnh. Nếu thiếu yêu cầu ảnh hưởng thiết kế, ghi open question hoặc assumption và yêu cầu BA/PO xác nhận; không tự suy diễn thành yêu cầu chính thức.

## Bộ outputs
1. System Architecture.
2. ADR(s) cho quyết định kiến trúc trọng yếu.
3. API Specification.
4. Database Design.
5. Data Model.
6. Sequence Diagrams / Key Flows.
7. Security Design.
8. Review evidence và G2 approval record.
9. [Bảng truy vết thiết kế trong Design Package Index](outputs/design-package-index.md#4-truy-vết-yêu-cầu), không sửa RTM đã duyệt ở G1 để thêm liên kết thiết kế.

Artifact không áp dụng phải ghi `N/A` và lý do trong package index.

## Document control
Mỗi artifact cần ID, version, status, owner, date, requirement references. Trạng thái gợi ý: `Draft → In Review → Approved → Superseded`; baseline là vai trò của phiên bản gói đã chốt, không phải trạng thái artifact riêng. Không sửa âm thầm bản đã duyệt; tăng version, ghi change reason và đánh giá tác động.

## G2 — Human Review Gate
Solution Architect được ủy quyền ra quyết định G2; Tech Lead và chuyên gia ghi kết luận theo phạm vi. Xem [điều kiện quyết định và chốt baseline](human-review.md#6-điều-kiện-quyết-định-g2) và [quy định G2](../governance/human-review-gates/G2-design-approval.md).

## Handoff sang 03 — Task Planning
Chuyển đúng phiên bản design package đã chốt làm baseline cùng bằng chứng G2 hợp lệ, bảng truy vết thiết kế, component boundaries, API/schema/flow, hạng mục migration/integration và bảo mật/NFR, dependencies, risks và spikes/PoC. Stage 03 xác minh đầu vào, phân rã và phân công task, rồi nối task về requirement và mục thiết kế. G3 phê duyệt readiness trước khi coding tại Stage 04. Luồng: **G2 → Stage 03 Task Planning → G3 → coding**. Khi dùng workflow engine, áp dụng điều kiện hoàn thành Stage 02 tại mục 2.11 của `workflow.md` trước khi bàn giao.

Áp dụng `framework/standards/architecture/`, `security/`, `documentation/` và governance policies. Policy/standard được phê duyệt có hiệu lực cao hơn template.
