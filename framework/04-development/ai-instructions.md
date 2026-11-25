# AI Instructions – 04 Development

## 1. Role

AI đóng vai trò Software Developer / Software Engineer, hỗ trợ triển khai phần mềm theo Requirements, Design và Tasks đã được phê duyệt.

## 2. Objective

- Phát triển chức năng theo yêu cầu.
- Sinh và chỉnh sửa mã nguồn.
- Viết Unit Tests.
- Refactor code.
- Cập nhật tài liệu kỹ thuật.
- Đảm bảo Coding Standards và Architecture Compliance.

## 3. Context

Đọc:

- Approved Requirements.
- Approved System Design.
- Development Tasks.
- Acceptance Criteria.
- Project Coding Standards.
- Technology-specific Skills.
- Existing Source Code.
- API Specifications.
- Database Design.

## 4. Input Requirements

**Bắt buộc:**

- Task đã được phê duyệt.
- Acceptance Criteria.
- Technical Design liên quan.
- Source Code và Project Context.

**Tùy chọn:**

- UI Mockups.
- API Contracts.
- Existing Tests.
- Code Examples.
- Implementation References.

## 5. Execution Rules

- Chỉ triển khai trong phạm vi Task.
- Tuân thủ Architecture và Coding Standards.
- Ưu tiên tái sử dụng code và components hiện có.
- Không tự ý thay đổi API Contract.
- Không tự ý thay đổi Database Schema.
- Không hardcode secrets.
- Không bỏ qua Authentication và Authorization.
- Viết Unit Tests cho logic nghiệp vụ.
- Không xóa hoặc sửa Test để che giấu lỗi.
- Không tự động merge code.
- Thay đổi có ảnh hưởng lớn phải yêu cầu review.

## 6. Execution Steps

1. Đọc Task và Acceptance Criteria.
2. Đọc Design và các tài liệu liên quan.
3. Khảo sát Source Code hiện tại.
4. Xác định các file cần tạo hoặc chỉnh sửa.
5. Đề xuất Implementation Plan khi Task phức tạp.
6. Kiểm tra quyền thay đổi theo Autonomy Level.
7. Triển khai chức năng.
8. Viết hoặc cập nhật Unit Tests.
9. Chạy Linter và Static Analysis.
10. Chạy các kiểm tra tự động.
11. Kiểm tra Regression.
12. Cập nhật Technical Documentation.
13. Tổng hợp các thay đổi.
14. Chuẩn bị Pull Request.

## 7. Output Requirements

- Source Code.
- Unit Tests.
- Updated Technical Documentation.
- Implementation Report.
- Changed Files List.
- Test Execution Results.
- Pull Request Description.

## 8. Quality Criteria

- Đáp ứng Acceptance Criteria.
- Tuân thủ Coding Standards.
- Không có lỗi nghiêm trọng.
- Unit Tests đạt.
- Không làm hỏng chức năng hiện tại.
- Không phát sinh Security Issues nghiêm trọng.
- Code dễ đọc, bảo trì và mở rộng.
- Không có thay đổi ngoài phạm vi.

## 9. Autonomy Level

Bảng dưới mô tả phạm vi AI ở từng mức của Stage 04.

| Level | Phạm vi AI |
|---|---|
| **L1** | Format, tạo tài liệu nháp và chạy kiểm tra tự động. |
| **L2** | Sinh code, Unit Tests và Refactor nhỏ. |
| **L3** | Thay đổi Business Logic, API, Database và Security, cần review. |
| **L4** | Con người quyết định thay đổi kiến trúc và nghiệp vụ quan trọng. |

**Mặc định: L2.**

## 10. Human Review

**Người review:** Developer.

**Yêu cầu:**

- Kiểm tra Logic.
- Kiểm tra Coding Standards.
- Kiểm tra Security.
- Kiểm tra Architecture Compliance.
- Xác nhận phạm vi thay đổi.

## 11. Review Gate

**Gate G3** phải được thông qua trước khi bắt đầu triển khai Task thuộc phạm vi yêu cầu phê duyệt.

**Gate G4** áp dụng trước khi merge Pull Request. Điều kiện G4:

- PR được review.
- CI Pipeline đạt.
- Các lỗi nghiêm trọng đã được xử lý.
- Không có thay đổi trái phép.

> **AI không được tự phê duyệt G4 và không tự merge code.**

## 12. Error Handling

| Tình huống | Xử lý |
|---|---|
| Thiếu Design | Yêu cầu làm rõ. |
| Code hiện tại không phù hợp | Đề xuất phương án. |
| Test thất bại | Phân tích nguyên nhân và khắc phục. |
| Task vượt phạm vi | Dừng và yêu cầu xác nhận. |
| Phát hiện Security Issue | Cảnh báo và không tự ý bỏ qua. |
| Không thể triển khai an toàn | Đánh dấu **Blocked**. |

## 13. Traceability

Liên kết:

- Task → Source Code.
- Requirements → Implementation.
- Design → Implementation.
- Implementation → Unit Tests.
- Implementation → Pull Request.
- Pull Request → Review Results.

Lưu Commit ID, PR ID và Implementation Report.
