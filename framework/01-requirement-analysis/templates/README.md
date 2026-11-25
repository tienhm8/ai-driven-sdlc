# Templates — 01 Requirement Analysis

## 1. Mục đích

Thư mục này chứa các biểu mẫu chuẩn để tạo deliverables của Requirement Analysis trong `../outputs/`. Template là khuôn mẫu; không đưa dữ liệu dự án thật vào đây. Khi khởi tạo project, các template được sao chép vào project theo quy tắc khởi tạo framework.

## 2. Danh mục template và ánh xạ

Bộ template gồm 14 file nội dung (12 deliverable bắt buộc và 2 template tùy chọn) cùng README này.

| Template | Artifact đầu ra | Bắt buộc | Vai trò / thứ tự sử dụng |
|---|---|---:|---|
| `business-requirement.md` | `01-business-requirements/BRD.md` | Có | Nhu cầu, mục tiêu và BRQ; gốc để phân rã yêu cầu. BRD tham chiếu BR bằng ID. |
| `scope-definition.md` | `02-scope-definition/scope-definition.md` | Có | Nguồn chuẩn phạm vi, ranh giới hệ thống và nội/ngoài phạm vi. |
| `functional-requirements.md` | `03-functional-requirements/functional-requirements.md` | Có | FRS; FR có nguồn, owner, priority, status và tiêu chí xác minh. |
| `non-functional-requirements.md` | `04-non-functional-requirements/non-functional-requirements.md` | Có | NFR có category, nguồn, owner, priority, status và cách đo/kiểm chứng. |
| `user-story.md` | `05-user-stories-use-cases/user-stories.md` | Có | Nhu cầu người dùng liên kết với BRQ/FR/NFR. |
| `use-case.md` | `05-user-stories-use-cases/use-cases.md` | Có | Actor, mục tiêu, luồng chính, ngoại lệ và kết quả. |
| `acceptance-criteria.md` | `06-acceptance-criteria/acceptance-criteria.md` | Có | Tiêu chí kiểm chứng qua US/UC hoặc trực tiếp từ FR/NFR; Test Case bổ sung ở Stage 06. |
| `business-rules.md` | `07-business-rules/business-rules.md` | Có | Nguồn chuẩn duy nhất cho BR; BRD chỉ tham chiếu bằng ID. |
| `business-process-model.md` | `08-business-process-model/business-process-model.md` | Tùy chọn | Mô hình quy trình, actor, activity, decision và event khi phù hợp. Giữ template để project cần thì dùng. |
| `glossary.md` | `09-glossary/glossary.md` | Tùy chọn | Thuật ngữ và định nghĩa nghiệp vụ khi phù hợp. Giữ template để project cần thì dùng. |
| `assumptions-constraints-dependencies-risks.md` | `10-assumptions-constraints-risks/assumptions-constraints-dependencies-risks.md` | Có | Nguồn chuẩn cho giả định, ràng buộc, phụ thuộc và rủi ro; câu hỏi mở có register riêng tại `10-assumptions-constraints-risks/open-questions.md`. |
| `requirement-traceability.md` | `11-requirement-traceability/requirement-traceability-matrix.md` | Có | Mẫu chuẩn RTM: Nguồn/Mục tiêu → BRQ → FR/NFR đến AC; BR và US/UC khi áp dụng. |
| `requirement-review-record.md` | `12-requirement-review/requirement-review-record.md` | Có | Ghi quá trình review, findings, resolution và bằng chứng. |
| `G1-approval.md` | `12-requirement-review/G1-approval.md` | Có | Dẫn chiếu quyết định G1 chính thức của Product Owner (ghi trên platform) cho đúng phiên bản baseline/review package. |

## 3. Nguyên tắc sử dụng

- Business Rules Catalogue là nguồn chuẩn duy nhất cho nội dung BR; các artifact khác chỉ tham chiếu BR ID.
- Scope Definition là nguồn chuẩn duy nhất cho phạm vi; BRD và báo cáo chỉ tóm tắt hoặc dẫn chiếu.
- Requirement Review Record và G1 Approval là hai artifact riêng: một ghi quá trình review, một dẫn chiếu quyết định gate chính thức trên platform và phiên bản được duyệt.
- [Template RTM Stage 01](requirement-traceability.md) là chuẩn duy nhất cho RTM trước G1. Bản khởi tạo trong `outputs/` được tạo từ template này. Thiết kế, task, implementation, test và release được nối ở các stage sau.
- Business Process Model và Glossary là đầu ra tùy chọn; không xóa template khỏi framework khi một project không dùng. Project ghi N/A và lý do khi cần báo cáo tính đầy đủ.
- Dùng [Quy ước định danh](../../standards/metadata/id-conventions.md), trạng thái chuẩn và yêu cầu metadata của framework. Không tự khẳng định một ID đã được cấp phát nếu chưa có registry đáng tin cậy.
- Mỗi artifact có ID, phiên bản, trạng thái và nguồn liên quan khi áp dụng. Nội dung do AI suy luận phải được đánh dấu và không được trình bày như dữ kiện đã xác nhận.

## 4. Cấu trúc thư mục

```text
templates/
├── README.md
├── business-requirement.md
├── scope-definition.md
├── functional-requirements.md
├── non-functional-requirements.md
├── user-story.md
├── acceptance-criteria.md
├── use-case.md
├── business-rules.md
├── business-process-model.md                 # Optional
├── glossary.md                                # Optional
├── assumptions-constraints-dependencies-risks.md
├── requirement-traceability.md
├── requirement-review-record.md
└── G1-approval.md
```

## 5. Vai trò và quan hệ template

| Template | Nội dung chính | Phụ thuộc / phân biệt |
|---|---|---|
| `business-requirement.md` | Mục tiêu, nhu cầu và Business Requirements (BRQ). | Tham chiếu BR ID, Scope Definition và NFR; không sở hữu nội dung của chúng. |
| `scope-definition.md` | Phạm vi, ranh giới hệ thống, in-scope/out-of-scope. | Nguồn chuẩn duy nhất cho phạm vi. |
| `functional-requirements.md` | FRS và yêu cầu FR có thể xác minh. | Liên kết BRQ, BR, NFR, US/UC và AC bằng ID. |
| `non-functional-requirements.md` | NFR cùng chỉ số/mục tiêu và phương pháp kiểm chứng. | Không tự đặt target khi chưa có căn cứ. |
| `user-story.md` / `use-case.md` | Nhu cầu người dùng và luồng tương tác. | Dùng riêng theo nhu cầu; tránh lặp chi tiết luồng giữa FR, US và UC. |
| `acceptance-criteria.md` | Điều kiện đạt có thể kiểm chứng. | Liên kết US/UC; Test Case được tạo ở Stage 06. |
| `business-rules.md` | Danh mục Business Rules (BR). | Nguồn chuẩn duy nhất cho nội dung BR. |
| `business-process-model.md` / `glossary.md` | Mô hình quy trình / thuật ngữ nghiệp vụ. | Tùy chọn; giữ để project cần thì sử dụng. |
| `assumptions-constraints-dependencies-risks.md` | Register assumption, constraint, dependency và risk. | Có owner/trạng thái; OQ lifecycle chi tiết nằm ở `outputs/10-assumptions-constraints-risks/open-questions.md`. |
| `requirement-traceability.md` | RTM Stage 01. | Kết thúc tại AC; kiểm độ bao phủ từng chiều trước G1. |
| `requirement-review-record.md` | Findings, resolution và bằng chứng review. | Không ghi thay quyết định G1. |
| `G1-approval.md` | Dẫn chiếu quyết định G1 trên platform và liệt kê phiên bản được duyệt (gồm OQ, giả định, ràng buộc). | Tham chiếu quyết định của PO cho đúng phiên bản baseline/review package. |

Mỗi template có cùng tên artifact trong `../outputs/` theo bảng ánh xạ ở mục 2. Báo cáo phân tích tổng hợp là artifact bổ sung, không thuộc danh sách 12 deliverable chuẩn.
