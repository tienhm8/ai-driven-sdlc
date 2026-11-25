# Định nghĩa phạm vi (Scope Definition)

## 1. Thông tin tài liệu

| Trường | Giá trị |
|---|---|
| Mã tài liệu | SCOPE-0001 |
| Dự án | [Tên dự án] |
| Phiên bản | 0.1 |
| Trạng thái | Draft |
| Owner | [Vai trò/người phụ trách] |
| Nguồn đầu vào | [Liên kết hoặc ID tài liệu] |
| Ngày cập nhật | [YYYY-MM-DD] |

## 2. Mục đích và mục tiêu

- Vấn đề nghiệp vụ cần giải quyết: [Mô tả]
- Mục tiêu dự án/hệ thống: [Mô tả và chỉ số thành công nếu có]
- Đối tượng hưởng lợi: [Stakeholder/actor]

## 3. Phạm vi hệ thống

- Mô tả phạm vi: [Hệ thống/sản phẩm và năng lực được bao phủ]
- Người dùng/actor chính: [Danh sách hoặc tham chiếu]
- Môi trường/vòng đời áp dụng: [Nếu phù hợp]

## 4. Trong phạm vi (In-scope)

| ID | Năng lực/quy trình/phạm vi | Lý do | BRQ/FR liên quan |
|---|---|---|---|
| SCP-0001 | [Nội dung] | [Lý do] | [ID hoặc TBD] |

## 5. Ngoài phạm vi (Out-of-scope)

| ID | Năng lực/quy trình bị loại trừ | Lý do/giả định | Tác động nếu thay đổi |
|---|---|---|---|
| SCP-EX-0001 | [Nội dung] | [Lý do] | [Tác động] |

## 6. Ranh giới hệ thống và giao diện

| Thành phần/hệ thống | Trong/ngoài ranh giới | Trách nhiệm/giao tiếp | Owner |
|---|---|---|---|
| [Tên] | [Trong / Ngoài] | [Mô tả] | [Owner] |

Sơ đồ context hoặc tham chiếu: [Liên kết nếu có]

## 7. Phụ thuộc bên ngoài

Tham chiếu dependency chi tiết trong `../outputs/10-assumptions-constraints-risks/assumptions-constraints-dependencies-risks.md`.

| Dependency ID | Hệ thống/bên ngoài | Phụ thuộc vào | Owner | Trạng thái |
|---|---|---|---|---|
| TDEP-0001 | [Tên] | [Mô tả] | [Owner] | [Draft / Confirmed / Blocked] |

## 8. Giả định và ràng buộc ảnh hưởng phạm vi

Tham chiếu ID tương ứng trong artifact Assumptions, Constraints, Dependencies & Risks; không sao chép chi tiết tại đây.

| Loại | ID | Tác động đến phạm vi |
|---|---|---|
| [Assumption / Constraint] | [ID] | [Mô tả] |

## 9. Tiêu chí hoàn thành phạm vi

- [Tiêu chí có thể xác minh]
- [Liên kết đến AC/BRQ/FR nếu có]

## 10. Quyết định và lịch sử thay đổi

| Phiên bản | Ngày | Người cập nhật | Thay đổi | Quyết định/nguồn |
|---|---|---|---|---|
| 0.1 | [YYYY-MM-DD] | [Owner] | Bản nháp ban đầu | [Nguồn] |

**Hướng dẫn:** Đây là nguồn chuẩn duy nhất cho phạm vi dự án/hệ thống. BRD và báo cáo phân tích chỉ tóm tắt hoặc dẫn chiếu, không duy trì bản sao phạm vi.
