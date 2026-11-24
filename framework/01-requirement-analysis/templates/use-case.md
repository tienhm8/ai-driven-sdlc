# Đặc tả Use Case (Use Case Specification)

## 1. Thông tin tài liệu

| Trường | Giá trị |
|---|---|
| Tên dự án | [Tên dự án] |
| Phiên bản tài liệu | 1.0 |
| Trạng thái | Draft |
| Tác giả | [Tác giả] |
| Cập nhật lần cuối | [YYYY-MM-DD] |

## 2. Nhận diện Use Case

| Trường | Giá trị |
|---|---|
| Mã Use Case | UC-001 |
| Tên Use Case | [Tên Use Case] |
| Yêu cầu nghiệp vụ liên quan | BRQ-0001 |
| User Story liên quan | US-001 |
| Tiêu chí nghiệm thu liên quan | AC-001 |
| Module | [Tên module] |
| Độ ưu tiên | Cao |

## 3. Mô tả Use Case

### 3.1 Mục tiêu
[Mục tiêu của Use Case.]

### 3.2 Mô tả
[Mô tả tổng quan chức năng.]

### 3.3 Phạm vi
[Phạm vi hệ thống liên quan.]

### 3.4 Cấp độ
- Mục tiêu người dùng (User Goal)
- Chức năng con (Subfunction)
- Tổng hợp (Summary)

## 4. Actor

| Mã Actor | Tên Actor | Mô tả | Trách nhiệm |
|---|---|---|---|
| ACT-001 | [Actor] | [Mô tả] | [Trách nhiệm] |

### 4.1 Actor chính
[Actor khởi tạo Use Case.]

### 4.2 Actor phụ
[Actor hoặc hệ thống bên ngoài hỗ trợ.]

## 5. Điều kiện tiên quyết

Các điều kiện phải thỏa mãn trước khi Use Case được thực hiện:

1. [Điều kiện tiên quyết 1]
2. [Điều kiện tiên quyết 2]

## 6. Sự kiện kích hoạt

[Sự kiện kích hoạt Use Case.]

## 7. Luồng chính (Main Success Scenario)

| Bước | Actor/Hệ thống | Hành động |
|---|---|---|
| 1 | Actor | [Hành động của người dùng] |
| 2 | Hệ thống | [Phản hồi của hệ thống] |
| 3 | Actor | [Hành động của người dùng] |
| 4 | Hệ thống | [Phản hồi của hệ thống] |

## 8. Luồng thay thế (Alternative Flows)

### AF-01: [Tên luồng thay thế]

- Kích hoạt: [Điều kiện]
- Các bước:
  1. [Bước 1]
  2. [Bước 2]
- Kết quả mong đợi: [Kết quả]
- Quay lại luồng chính: [Số bước / Kết thúc]

## 9. Luồng ngoại lệ (Exception Flows)

### EX-01: [Tên ngoại lệ]

- Kích hoạt: [Điều kiện lỗi]
- Các bước:
  1. [Hệ thống phát hiện lỗi]
  2. [Hệ thống xử lý lỗi]
  3. [Hệ thống trả về phản hồi lỗi mong đợi]
- Kết quả mong đợi: [Kết quả]

## 10. Quy tắc nghiệp vụ liên quan

Business Rules là nội dung chuẩn trong `../outputs/07-business-rules/business-rules.md`; Use Case chỉ tham chiếu ID.

| Mã BR | Tên/quy tắc liên quan |
|---|---|
| BR-0001 | [Tên quy tắc] |

## 11. Đầu vào / Đầu ra

### 11.1 Đầu vào

| Trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|---|---|
| [Trường] | [Kiểu] | Có | [Mô tả] |

### 11.2 Đầu ra

| Trường | Kiểu dữ liệu | Mô tả |
|---|---|---|
| [Trường] | [Kiểu] | [Mô tả] |

## 12. Hậu điều kiện

### 12.1 Hậu điều kiện khi thành công
[Trạng thái hệ thống sau khi thực hiện thành công.]

### 12.2 Hậu điều kiện khi thất bại
[Trạng thái hệ thống khi thực hiện thất bại.]

## 13. Yêu cầu phi chức năng liên quan

Tham chiếu NFR ID trong `../outputs/04-non-functional-requirements/non-functional-requirements.md`:

- NFR IDs:
- Điều kiện áp dụng:

## 14. Use Case liên quan

| Use Case liên quan | Quan hệ | Mô tả |
|---|---|---|
| UC-002 | Include / Extend / Generalization | [Mô tả] |

## 15. Ánh xạ tiêu chí nghiệm thu

| Kịch bản Use Case | Tiêu chí nghiệm thu (AC ID) | Ghi chú |
|---|---|---|
| Luồng chính | AC-0001 | [Điều kiện/kết quả] |
| Luồng thay thế | AC-0002 | [Điều kiện/kết quả] |
| Luồng ngoại lệ | AC-0003 | [Điều kiện/kết quả] |

Test Case được liên kết ở Stage 06; không tạo Test Case ID tại Requirement Analysis.

## 16. Nguồn và lịch sử thay đổi

- Nguồn:
- Owner:

| Phiên bản | Ngày | Người cập nhật | Mô tả thay đổi |
|---|---|---|---|
| 0.1 | [Ngày] | [Owner] | Bản nháp ban đầu |

## 17. Lịch sử thay đổi

| Phiên bản | Ngày | Mô tả thay đổi |
|---|---|---|
| 1.0 | [Ngày] | Phiên bản khởi tạo |

---

**Hướng dẫn cho AI:**
- Xác định đầy đủ các actor liên quan và ranh giới hệ thống.
- Mô tả tương tác từ góc nhìn của actor.
- Tách riêng luồng chính, luồng thay thế và luồng ngoại lệ.
- KHÔNG trộn chi tiết triển khai vào hành vi nghiệp vụ.
- Liên kết Use Case với các mã BRQ, US và AC hiện có.
- Nhận diện điều kiện tiên quyết còn thiếu và hành vi lỗi chưa được định nghĩa.
- KHÔNG tự tạo quy tắc nghiệp vụ.
