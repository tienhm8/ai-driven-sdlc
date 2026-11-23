# Tiêu chí nghiệm thu (Acceptance Criteria)

## 1. Thông tin tài liệu

| Trường | Giá trị |
|---|---|
| Tên dự án | [Tên dự án] |
| Phiên bản tài liệu | 1.0 |
| Trạng thái | Draft |
| Tác giả | [Tác giả] |
| Cập nhật lần cuối | [YYYY-MM-DD] |

## 2. Tổng quan tiêu chí nghiệm thu

| Trường | Giá trị |
|---|---|
| Mã tiêu chí nghiệm thu | AC-001 |
| User Story liên quan | US-001 |
| Yêu cầu nghiệp vụ liên quan | BRQ-0001 |
| Chức năng / Module | [Tên chức năng] |
| Độ ưu tiên | Cao |
| Trạng thái | Draft |

## 3. Định nghĩa tiêu chí nghiệm thu

### AC-001: [Tên tiêu chí nghiệm thu]

**Mô tả:**

[Mô tả điều kiện cần đạt để chức năng được chấp nhận.]

**Kịch bản:** [Tên kịch bản]

**Given (Cho):** [Bối cảnh ban đầu / Điều kiện tiên quyết]

**When (Khi):** [Hành động của người dùng / Tác nhân kích hoạt]

**Then (Thì):** [Kết quả mong đợi]

### 3.1 Kịch bản bổ sung

| Mã kịch bản | Kịch bản | Kết quả mong đợi |
|---|---|---|
| SC-001 | [Kịch bản bình thường] | [Kết quả mong đợi] |
| SC-002 | [Kịch bản thay thế] | [Kết quả mong đợi] |
| SC-003 | [Kịch bản dữ liệu đầu vào không hợp lệ] | [Kết quả mong đợi] |
| SC-004 | [Kịch bản bị từ chối quyền truy cập] | [Kết quả mong đợi] |

## 4. Tiêu chí kiểm tra dữ liệu đầu vào

| Trường | Kiểu dữ liệu | Bắt buộc | Quy tắc kiểm tra | Thông báo lỗi |
|---|---|---|---|---|
| [Trường 1] | Chuỗi | Có | [Quy tắc] | [Thông báo] |
| [Trường 2] | Số | Không | [Quy tắc] | [Thông báo] |

## 5. Kiểm tra quy tắc nghiệp vụ

| Mã quy tắc | Quy tắc nghiệp vụ | Hành vi mong đợi |
|---|---|---|
| BR-0001 | [Quy tắc] | [Hành vi mong đợi] |

## 6. Tiêu chí kiểm thử âm tính

| Mã | Điều kiện không hợp lệ | Hành vi mong đợi |
|---|---|---|
| NEG-001 | Thiếu trường bắt buộc | Hiển thị lỗi kiểm tra dữ liệu |
| NEG-002 | Dữ liệu đầu vào không hợp lệ | Từ chối dữ liệu không hợp lệ |
| NEG-003 | Truy cập trái phép | Từ chối truy cập |
| NEG-004 | Yêu cầu trùng lặp | Tuân theo quy tắc nghiệp vụ đã định nghĩa |

## 7. Tiêu chí nghiệm thu phi chức năng

| Mã | Hạng mục | Điều kiện nghiệm thu | Cách đo |
|---|---|---|---|
| NFR-AC-001 | Hiệu năng | [Điều kiện] | [Chỉ số] |
| NFR-AC-002 | Bảo mật | [Điều kiện] | [Chỉ số] |
| NFR-AC-003 | Tính sẵn sàng | [Điều kiện] | [Chỉ số] |

## 8. Ánh xạ kiểm thử nghiệm thu

| Mã AC | Mã Test Case | Loại kiểm thử | Kết quả mong đợi |
|---|---|---|---|
| AC-001 | TC-001 | Chức năng | Đạt |
| AC-001 | TC-002 | Âm tính | Đạt |

## 9. Trạng thái nghiệm thu

| Mã AC | Kết quả kiểm chứng | Bằng chứng | Trạng thái |
|---|---|---|---|
| AC-001 | [Kết quả] | [Báo cáo test] | Chờ xử lý |

Các trạng thái có thể có:
- Chờ xử lý (Pending)
- Đạt (Passed)
- Không đạt (Failed)
- Bị chặn (Blocked)
- Không áp dụng (Not Applicable)

## 10. Phê duyệt

| Vai trò | Họ tên | Quyết định | Ngày | Ghi chú |
|---|---|---|---|---|
| Business Analyst | [Họ tên] | [Quyết định] | [Ngày] | [Ghi chú] |
| Product Owner | [Họ tên] | [Quyết định] | [Ngày] | [Ghi chú] |
| QA Lead | [Họ tên] | [Quyết định] | [Ngày] | [Ghi chú] |

## 11. Lịch sử thay đổi

| Phiên bản | Ngày | Mô tả thay đổi |
|---|---|---|
| 1.0 | [Ngày] | Phiên bản khởi tạo |

---

**Hướng dẫn cho AI:**
- Tạo tiêu chí nghiệm thu có thể kiểm thử và không mơ hồ.
- Ưu tiên định dạng Given / When / Then.
- Bao phủ kịch bản bình thường, thay thế, ngoại lệ và âm tính.
- Bao gồm các điều kiện biên khi áp dụng.
- Bao gồm điều kiện phân quyền và bảo mật khi có liên quan.
- Mỗi tiêu chí PHẢI có mã AC duy nhất.
- KHÔNG giả định hành vi mong đợi chưa được xác định.
- Đánh dấu các quy tắc nghiệp vụ còn thiếu để làm rõ.
- KHÔNG đánh dấu tiêu chí nghiệm thu là đã phê duyệt khi chưa có ủy quyền của con người.
