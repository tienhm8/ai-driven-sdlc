# User Stories

## 1. Thông tin tài liệu

| Trường | Giá trị |
|---|---|
| Tên dự án | [Tên dự án] |
| Phiên bản tài liệu | 1.0 |
| Trạng thái | Draft |
| Product Owner | [Họ tên] |
| Tác giả | [Họ tên] |
| Cập nhật lần cuối | [YYYY-MM-DD] |

## 2. Tổng quan User Story

### 2.1 Nhận diện story

| Trường | Giá trị |
|---|---|
| Mã User Story | US-001 |
| Tiêu đề | [Tiêu đề ngắn gọn, mô tả rõ] |
| Mã Epic | EPIC-001 |
| Yêu cầu nghiệp vụ liên quan | BRQ-0001 |
| Module | [Tên module] |
| Độ ưu tiên | Phải có |
| Story Points | [Ước lượng] |
| Trạng thái | Draft |

### 2.2 Phát biểu User Story

**Với vai trò** [Vai trò người dùng],

**Tôi muốn** [Hành động/Khả năng],

**Để** [Giá trị nghiệp vụ/Lợi ích].

> Giữ định dạng chuẩn tiếng Anh *As a / I want / So that* khi cần đồng bộ với công cụ quản lý backlog.

### 2.3 Bối cảnh nghiệp vụ
[Mô tả bối cảnh nghiệp vụ của User Story.]

### 2.4 Vai trò người dùng / Actor
- Actor chính: [Actor]
- Actor phụ: [Actor]
- Điều kiện tiên quyết: [Điều kiện]

## 3. Chi tiết chức năng

### 3.1 Mô tả
[Mô tả chi tiết chức năng cần thực hiện.]

### 3.2 Luồng chính
1. [Bước 1]
2. [Bước 2]
3. [Bước 3]

### 3.3 Luồng thay thế
1. [Kịch bản thay thế]
2. [Hành vi mong đợi]

### 3.4 Luồng ngoại lệ
1. [Điều kiện lỗi]
2. [Cách xử lý lỗi mong đợi]

## 4. Quy tắc nghiệp vụ và phụ thuộc

- Business Rules: tham chiếu BR ID trong `../outputs/07-business-rules/business-rules.md`.
- Dependencies: tham chiếu DEP ID trong `../outputs/10-assumptions-constraints-risks/assumptions-constraints-dependencies-risks.md`.

| Loại | ID | Mô tả ngắn/ghi chú |
|---|---|---|
| BR | BR-0001 | [Tên quy tắc] |
| DEP | DEP-0001 | [Phụ thuộc] |

## 6. Tham chiếu tiêu chí nghiệm thu

| Mã AC | Mô tả | Độ ưu tiên |
|---|---|---|
| AC-001 | [Tiêu chí nghiệm thu] | Cao |
| AC-002 | [Tiêu chí nghiệm thu] | Cao |

Tiêu chí nghiệm thu chi tiết được quản lý trong `../outputs/06-acceptance-criteria/acceptance-criteria.md`.

## 7. Yêu cầu UX/UI

- Màn hình/Trang: [Tên màn hình]
- Tương tác người dùng: [Mô tả tương tác]
- Trường nhập liệu: [Các trường]
- Đầu ra: [Kết quả mong đợi]
- Kiểm tra dữ liệu: [Quy tắc kiểm tra]
- Tham chiếu UI/UX: [Liên kết thiết kế]

## 8. Yêu cầu phi chức năng liên quan

Tham chiếu NFR ID trong `../outputs/04-non-functional-requirements/non-functional-requirements.md`:

- NFR IDs:
- Điều kiện áp dụng:

## 9. Định nghĩa sẵn sàng (Definition of Ready - DoR)

- [ ] Yêu cầu nghiệp vụ đã được xác định.
- [ ] Vai trò người dùng đã được định nghĩa rõ ràng.
- [ ] User Story dễ hiểu.
- [ ] Tiêu chí nghiệm thu đã được định nghĩa.
- [ ] Các phụ thuộc đã được xác định.
- [ ] Không còn câu hỏi quan trọng chưa được giải quyết.
- [ ] Story đủ nhỏ để triển khai.

## 10. Định nghĩa hoàn thành (Definition of Done - DoD)

- [ ] Đã hoàn thành triển khai.
- [ ] Unit test đã pass.
- [ ] Code review đã được phê duyệt.
- [ ] Tiêu chí nghiệm thu đã được đáp ứng.
- [ ] Kiểm thử QA đã pass.
- [ ] Tài liệu đã được cập nhật.
- [ ] Không còn lỗi nghiêm trọng chưa được xử lý.

## 11. Review và phê duyệt

| Vai trò | Họ tên | Quyết định | Ngày |
|---|---|---|---|
| Business Analyst | [Họ tên] | [Quyết định] | [Ngày] |
| Product Owner | [Họ tên] | [Quyết định] | [Ngày] |
| Tech Lead | [Họ tên] | [Quyết định] | [Ngày] |

## 12. Lịch sử thay đổi

| Phiên bản | Ngày | Mô tả thay đổi |
|---|---|---|
| 1.0 | [Ngày] | Phiên bản khởi tạo |

---

**Hướng dẫn cho AI:**
- Tạo User Story từ các Yêu cầu nghiệp vụ đã được phê duyệt.
- Dùng định dạng chuẩn As a / I want / So that.
- Đảm bảo mỗi story thể hiện một kết quả có ý nghĩa đối với người dùng.
- Tránh gộp nhiều mục tiêu nghiệp vụ độc lập vào một story.
- Nhận diện phụ thuộc và thông tin còn thiếu.
- KHÔNG tạo quy tắc nghiệp vụ mới khi không có bằng chứng.
- Liên kết mỗi User Story với mã BRQ nguồn.
- KHÔNG phê duyệt hoặc ưu tiên story thay mặt Product Owner.
