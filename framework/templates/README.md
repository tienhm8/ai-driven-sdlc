# Thư viện Template dùng chung của Framework

Thư viện biểu mẫu xuyên giai đoạn và chỉ dẫn tới các mẫu chuẩn theo stage. Nếu một file chỉ dẫn sang mẫu chuẩn, hãy điền mẫu đích, không điền file chỉ dẫn.

| Artifact | Mẫu chuẩn / đầu ra | Người điền hoặc review |
|---|---|---|
| BRD, User Story, RTM trước G1 | [Danh mục Stage 01](../01-requirement-analysis/templates/README.md) quy định mẫu và tên đầu ra trong `docs/01-requirement-analysis/outputs/`. | Business Analyst soạn; người có thẩm quyền duyệt gói G1. |
| RTM sau G1 | [RTM downstream](requirement/requirements-traceability-matrix.md) bổ sung liên kết design, task, PR, test và release. | Owner truy vết của dự án và các stage liên quan. |
| Implementation Plan | [Mẫu Stage 04](../04-development/templates/implementation-plan.md); lập kế hoạch theo task trước khi sửa code, lưu cùng hồ sơ task. | Developer phụ trách (AI có thể soạn); Tech Lead review nếu cần. |
| Pull Request | [Mẫu Stage 05](../05-code-review/templates/pull-request-template.md); đầu ra là mô tả PR trên hệ thống quản lý mã nguồn. | Developer điền, reviewer kiểm tra. |
| Hồ sơ QA | [Danh mục Stage 06](../06-testing-qa/templates/README.md) quy định mẫu, đầu ra và vai trò theo đợt test/release. | QA soạn; QA Lead và Product Owner duyệt G5. |
| Hồ sơ Deployment | [Danh mục Stage 07](../07-deployment/templates/README.md) quy định mẫu cho từng release; kết quả thực thi và bàn giao nằm trong [Deployment Record](deployment/deployment-record.md). | Release Engineer/DevOps chuẩn bị; Release Manager duyệt G6. |

## Quy ước
- Giữ placeholder `{{...}}` đến khi được điền; dùng ID duy nhất theo metadata standard.
- Ngày giờ theo ISO 8601; ghi timezone khi cần.
- Mỗi artifact có owner, status, version, nguồn tham chiếu.
- Phân biệt AI-drafted, human-reviewed và approved.
- Không lưu secret, token, credential hoặc dữ liệu production nhạy cảm.
- Không ghi đè tài liệu đã duyệt; tạo revision mới và lưu lịch sử.

## Danh mục
- `requirement/`: BRD, User Story, traceability matrix.
- `design/`: Architecture Decision Record.
- `planning/`: Risk assessment.
- `development/`: implementation plan, technical change, handover.
- `review/`: review checklist, approval record.
- `testing/`: test plan, test case, execution report, defect.
- `deployment/`: deployment plan, release notes, rollback, deployment record.

AI có thể tạo bản nháp và tổng hợp bằng chứng; người có thẩm quyền xác nhận nội dung và phê duyệt Gate tương ứng.
