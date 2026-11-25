# Requirement Analysis — Đầu ra (Outputs)

## 1. Mục đích

Thư mục này định nghĩa deliverables chuẩn của Requirement Analysis và vị trí lưu trong project. Danh mục phải nhất quán với mục **1.8 Output — Đầu ra** trong `../workflow.md` và template tương ứng trong `../templates/README.md`.

## 2. Cấu trúc đầu ra chuẩn

```text
outputs/
├── README.md
├── requirement-analysis-report.md                    # Báo cáo tổng hợp bổ sung
├── 01-business-requirements/
│   └── BRD.md
├── 02-scope-definition/
│   └── scope-definition.md
├── 03-functional-requirements/
│   └── functional-requirements.md
├── 04-non-functional-requirements/
│   └── non-functional-requirements.md
├── 05-user-stories-use-cases/
│   ├── user-stories.md
│   └── use-cases.md
├── 06-acceptance-criteria/
│   └── acceptance-criteria.md
├── 07-business-rules/
│   └── business-rules.md
├── 08-business-process-model/
│   └── business-process-model.md                    # Tùy chọn
├── 09-glossary/
│   └── glossary.md                                  # Tùy chọn
├── 10-assumptions-constraints-risks/
│   ├── assumptions-constraints-dependencies-risks.md
│   └── open-questions.md
├── 11-requirement-traceability/
│   └── requirement-traceability-matrix.md
└── 12-requirement-review/
    ├── requirement-review-record.md
    └── G1-approval.md
```

Business Process Model và Glossary là đầu ra tùy chọn, nhưng template và thư mục chuẩn được giữ trong framework/project. Nếu không áp dụng, ghi `N/A` và lý do trong review package. Các deliverables khác là bắt buộc.

`requirement-analysis-report.md` là báo cáo tổng hợp bổ sung để review dễ hơn; không thay thế artifact nguồn và không phải một trong 12 deliverable chuẩn.

## 3. Deliverables và nội dung

| # | Deliverable | Artifact chuẩn | Nội dung cốt lõi |
|---:|---|---|---|
| 1 | Business Requirements Document (BRD) | `01-business-requirements/BRD.md` | Mục tiêu, nhu cầu nghiệp vụ, yêu cầu stakeholder và BRQ có ID; tham chiếu BR bằng ID. |
| 2 | Scope Definition | `02-scope-definition/scope-definition.md` | Project/System Scope, in-scope, out-of-scope, ranh giới hệ thống và external dependencies. Đây là nguồn chuẩn duy nhất cho phạm vi. |
| 3 | Functional Requirements Specification (FRS) | `03-functional-requirements/functional-requirements.md` | FR có ID, mô tả, mức ưu tiên, nguồn, owner, trạng thái và tiêu chí xác minh. |
| 4 | Non-functional Requirements (NFR) | `04-non-functional-requirements/non-functional-requirements.md` | NFR có ID, hạng mục, mô tả, mức ưu tiên, nguồn, owner, trạng thái và cách đo/kiểm chứng khi phù hợp. |
| 5 | User Stories & Use Cases | `05-user-stories-use-cases/user-stories.md`; `05-user-stories-use-cases/use-cases.md` | Nhu cầu, actor, mục tiêu và kịch bản; liên kết yêu cầu liên quan. |
| 6 | Acceptance Criteria | `06-acceptance-criteria/acceptance-criteria.md` | Tiêu chí kiểm chứng qua US/UC hoặc trực tiếp từ FR/NFR, với điều kiện Pass/Fail. Test Case và kết quả thực thi thuộc Stage 06. |
| 7 | Business Rules Catalogue | `07-business-rules/business-rules.md` | Nguồn chuẩn duy nhất cho BR: ID, mô tả, điều kiện, kết quả mong đợi và BRQ/FR liên quan. BRD chỉ tham chiếu BR ID. |
| 8 | Business Process Model (tùy chọn) | `08-business-process-model/business-process-model.md` | Quy trình, sơ đồ/mô tả, actor, hoạt động, quyết định và sự kiện nghiệp vụ khi phù hợp. |
| 9 | Business Glossary (tùy chọn) | `09-glossary/glossary.md` | Thuật ngữ, định nghĩa và từ viết tắt khi phù hợp. |
| 10 | Assumptions, Constraints, Dependencies, Risks & Open Questions | `10-assumptions-constraints-risks/assumptions-constraints-dependencies-risks.md`; `10-assumptions-constraints-risks/open-questions.md` | Các giả định, ràng buộc, phụ thuộc, rủi ro và câu hỏi mở cùng owner/trạng thái xử lý. |
| 11 | Requirement Traceability Matrix (RTM) | `11-requirement-traceability/requirement-traceability-matrix.md` | Nguồn/Mục tiêu → BRQ → FR/NFR đến AC; liên kết BR và US/UC khi áp dụng. Đánh giá từng chiều trước G1. |
| 12 | Requirement Review Record & G1 Approval Package | `12-requirement-review/requirement-review-record.md`; `12-requirement-review/G1-approval.md` | File review ghi findings/resolution; file G1 dẫn chiếu quyết định PO trên platform và đúng phiên bản baseline/package (gồm OQ, giả định, ràng buộc). |

## 4. Quy tắc đầu ra

1. Tạo các deliverables bắt buộc theo đúng cấu trúc và template trong `../templates/`.
2. Tạo Business Process Model và Glossary khi phù hợp; nếu không áp dụng, ghi N/A cùng lý do.
3. Gán và giữ ID theo `../../standards/metadata/id-conventions.md`; không bịa rằng ID đã được cấp phát chính thức.
4. Tham chiếu nguồn cho yêu cầu; không biến suy luận/giả định thành dữ kiện đã xác nhận.
5. Cập nhật artifact nguồn thay vì sao chép nội dung khiến các bản trùng lặp có thể lệch nhau.
6. Duy trì trạng thái, phiên bản, owner và lịch sử thay đổi theo chuẩn framework.
7. Phân biệt rõ bản nháp do AI tạo với nội dung đã được người có thẩm quyền xác nhận.
8. G1 Approval chỉ ghi nhận quyết định của Product Owner được ủy quyền; AI không được tự phê duyệt.
9. Quyết định G1 chỉ áp dụng cho đúng phiên bản artifact và review package được ghi trong hồ sơ.

## 5. Trạng thái

Artifact status dùng các giá trị chuẩn tại `../../standards/metadata/status-conventions.md` (Draft, In Review, Changes Requested, Approved, Rejected, Deprecated). Trạng thái câu hỏi, finding và quyết định gate là các lifecycle riêng, không thay thế Artifact Status.

## 6. Bàn giao và điều kiện G1

Checklist 06 xác nhận điều kiện sẵn sàng và dẫn chiếu kết quả kiểm tra; hồ sơ `12-requirement-review/G1-approval.md` dẫn chiếu quyết định chính thức trên platform và liệt kê phiên bản được duyệt. `12-requirement-review/requirement-review-record.md` lưu quá trình review, findings và resolution.

- Requirement baseline được chuyển sang System Design qua các artifact đã duyệt và tham chiếu phiên bản/approval cụ thể.
- RTM Stage 01 được khởi tạo từ `templates/requirement-traceability.md` của framework; các stage sau bổ sung liên kết downstream theo ID, không dùng chúng làm điều kiện G1.
- Không còn câu hỏi critical ngăn cản thiết kế; vấn đề còn lại có owner, hạn và được PO chấp nhận rõ ràng.
- Chuyển tiếp chỉ sau khi có quyết định G1 hợp lệ là Approved.
