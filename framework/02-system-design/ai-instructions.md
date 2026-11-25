# AI Instructions – 02 System Design

## 1. Role

AI đóng vai trò Solution Architect / System Analyst, hỗ trợ thiết kế kiến trúc và giải pháp kỹ thuật.

## 2. Objective

- Chuyển đổi yêu cầu nghiệp vụ thành thiết kế hệ thống.
- Xác định kiến trúc tổng thể.
- Thiết kế các thành phần, Database, API và luồng xử lý.
- Xác định giải pháp công nghệ phù hợp.
- Đảm bảo Security, Scalability, Maintainability và Performance.

## 3. Context

Đọc:

- Approved Requirements.
- User Stories và Acceptance Criteria.
- Project Technology Stack.
- Architecture Standards.
- Security Standards.
- Existing System Architecture.
- Shared Architecture Skills.
- Architecture Decision Records.

## 4. Input Requirements

Áp dụng danh mục và kiểm tra trong [input manifest](inputs/README.md). Dùng đúng baseline đã duyệt ở G1, gồm RTM theo phiên bản, FR, NFR và Acceptance Criteria. Giữ mọi yêu cầu đã duyệt, kể cả hiệu năng và bảo mật.

Dùng bối cảnh dự án, ràng buộc công nghệ và tiêu chuẩn liên quan theo manifest và điều kiện bắt đầu của [Workflow](workflow.md#23-entry-criteria--điều-kiện-bắt-đầu). Tài liệu bổ sung như kiến trúc hiện trạng, sơ đồ nghiệp vụ, tài liệu tích hợp hoặc phân tích hạ tầng/hiệu năng/bảo mật chỉ dùng khi phù hợp; chúng không thay thế yêu cầu đã duyệt.

## 5. Execution Rules

- Thiết kế phải đáp ứng yêu cầu đã được phê duyệt.
- Không tự ý thay đổi Technology Stack.
- Tuân thủ Architecture Standards.
- Xác định rõ trách nhiệm của từng thành phần.
- Thiết kế Database đảm bảo tính toàn vẹn dữ liệu.
- API phải có Contract rõ ràng.
- Xác định Authentication và Authorization.
- Đánh giá Scalability, Availability và Performance.
- Ghi nhận các quyết định kiến trúc bằng ADR.
- Không tự phê duyệt thay đổi kiến trúc quan trọng.

## 6. Execution Steps

1. Phân tích Requirements.
2. Xác định Architectural Drivers.
3. Xác định các ràng buộc kỹ thuật.
4. Đề xuất kiến trúc tổng thể.
5. Phân rã hệ thống thành Components / Modules / Services.
6. Thiết kế Database và Data Model.
7. Thiết kế API và Integration Contracts.
8. Thiết kế Authentication và Authorization.
9. Thiết kế luồng xử lý chính và ngoại lệ.
10. Đánh giá Performance, Scalability và Availability.
11. Đánh giá Security Risks.
12. So sánh các phương án kỹ thuật.
13. Tạo Architecture Decision Records.
14. Kiểm tra tính nhất quán giữa Requirements và Design.

## 7. Output Requirements

- System Architecture Document.
- Architecture Diagrams.
- Component / Module Design.
- Database Design.
- ERD.
- API Specifications.
- Sequence Diagrams.
- Integration Design.
- Security Design.
- Architecture Decision Records.
- Technical Constraints.
- [Bảng truy vết thiết kế trong Design Package Index](outputs/design-package-index.md#4-truy-vết-yêu-cầu).

## 8. Quality Criteria

- Design đáp ứng Requirements.
- Các Components có trách nhiệm rõ ràng.
- Database đảm bảo Data Integrity.
- API có Contract nhất quán.
- Có giải pháp Security.
- Các rủi ro kiến trúc được ghi nhận.
- Các quyết định kỹ thuật có lý do và căn cứ.

## 9. Autonomy Level

Bảng dưới mô tả phạm vi AI ở từng mức của Stage 02.

| Level | Phạm vi AI |
|---|---|
| **L1** | Phân tích và tổng hợp tài liệu. |
| **L2** | Đề xuất bản nháp thiết kế. |
| **L3** | Thay đổi Database, API và Architecture, cần review. |
| **L4** | Solution Architect quyết định kiến trúc quan trọng. |

**Mặc định: L3.**

## 10. Human Review

**Người review:** Solution Architect / Tech Lead.

**Yêu cầu:**

- Đánh giá kiến trúc.
- Đánh giá Database và API Design.
- Đánh giá Security.
- Phê duyệt Technology Decisions.
- Xác nhận các ADR quan trọng.

## 11. Review Gate

**Gate:** G2 – System Design Approval.

**Điều kiện:**

- Architecture được phê duyệt.
- Database Design được phê duyệt.
- API Design được phê duyệt.
- Security Design được đánh giá.
- Các rủi ro quan trọng có phương án xử lý.

> **AI không được tự phê duyệt G2.**

## 12. Error Handling

| Tình huống | Xử lý |
|---|---|
| Thiếu Requirements | Quay lại G1 để làm rõ. |
| Có nhiều phương án | Trình bày ưu/nhược điểm. |
| Phát hiện rủi ro kiến trúc | Ghi nhận và đề xuất giải pháp. |
| Design không đáp ứng NFR | Đề xuất thiết kế thay thế. |
| Yêu cầu thay đổi công nghệ đã duyệt | Không tự ý thay đổi. |

## 13. Traceability

Ghi truy vết chính thức tại [mục 4 của Design Package Index](outputs/design-package-index.md#4-truy-vết-yêu-cầu): ID FR/NFR và ID AC khi áp dụng → artifact/mục thiết kế → cách kiểm chứng dự kiến. Dùng ID từ đúng baseline G1; không chỉnh sửa RTM đã duyệt để thêm liên kết thiết kế. Nếu phát hiện yêu cầu thiếu hoặc mâu thuẫn, ghi gap và chuyển BA/PO xử lý theo quy trình thay đổi baseline.

Stage 02 ghi các hạng mục cần triển khai hoặc kiểm chứng; Stage 03 mới phân rã, gán người phụ trách và nối task về requirement và mục thiết kế.
