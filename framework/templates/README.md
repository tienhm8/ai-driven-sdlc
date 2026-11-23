# Thư viện Template dùng chung của Framework

Thư viện biểu mẫu chuẩn dùng chung cho 8 giai đoạn AI-Driven SDLC.

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
