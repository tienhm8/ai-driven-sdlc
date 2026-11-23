# Ma trận truy vết yêu cầu (Requirement Traceability Matrix - RTM)

## 1. Thông tin tài liệu

| Trường | Giá trị |
|---|---|
| Tên dự án | [Tên dự án] |
| Mã tài liệu | RTM-001 |
| Phiên bản tài liệu | 1.0 |
| Trạng thái | Draft |
| Chủ sở hữu | Business Analyst |
| Cập nhật lần cuối | [YYYY-MM-DD] |

## 2. Mục tiêu truy vết

Ma trận truy vết yêu cầu (RTM) đảm bảo rằng:

- Mọi yêu cầu có nguồn gốc có thể nhận diện.
- Mọi Yêu cầu nghiệp vụ được phân rã thành các User Story liên quan.
- Mọi User Story có Tiêu chí nghiệm thu có thể đo lường.
- Mọi yêu cầu liên quan được hỗ trợ bởi Use Case.
- Yêu cầu được liên kết với các artifact thiết kế, phát triển và kiểm thử.
- Có thể đánh giá tác động của thay đổi lên các artifact phía sau.
- Không có yêu cầu nào được triển khai khi thiếu cơ sở nghiệp vụ đã được phê duyệt.
- Không có yêu cầu quan trọng nào bị bỏ sót khỏi kiểm thử.

## 3. Ma trận truy vết yêu cầu

### 3.1 Truy vết từ đầu đến cuối

| Mã BR | Mã US | Mã AC | Mã UC | Mã thiết kế | Mã Task | Mã Test Case | Trạng thái |
|---|---|---|---|---|---|---|---|
| BR-001 | US-001 | AC-001 | UC-001 | DES-001 | TASK-001 | TC-001 | Đang thực hiện |
| BR-001 | US-002 | AC-002 | UC-002 | DES-002 | TASK-002 | TC-002 | Đang thực hiện |
| BR-002 | US-003 | AC-003 | UC-003 | DES-003 | TASK-003 | Chưa bắt đầu |

### 3.2 Độ bao phủ theo Yêu cầu nghiệp vụ

| Mã BR | Tên yêu cầu | Tổng số User Story | Đã bao phủ | Tỷ lệ bao phủ |
|---|---|---:|---:|---:|
| BR-001 | [Tên] | 3 | 3 | 100% |
| BR-002 | [Tên] | 2 | 1 | 50% |

### 3.3 Độ bao phủ theo User Story

| Mã US | BR liên quan | Số AC | Số UC | Số Test Case | Trạng thái bao phủ |
|---|---|---:|---:|---:|---|
| US-001 | BR-001 | 3 | 1 | 5 | Đã bao phủ |
| US-002 | BR-001 | 2 | 1 | 0 | Chưa kiểm thử |

## 4. Truy vết xuôi dòng (Downstream Traceability)

### 4.1 Ánh xạ thiết kế

| Mã yêu cầu | Artifact kiến trúc/thiết kế | Tham chiếu thiết kế | Trạng thái |
|---|---|---|---|
| BR-001 | [Tài liệu thiết kế] | DES-001 | Đã review |

### 4.2 Ánh xạ phát triển

| Mã US | Task phát triển | Tham chiếu mã nguồn | Pull Request | Trạng thái |
|---|---|---|---|---|
| US-001 | TASK-001 | [File/Module] | PR-001 | Đang thực hiện |

### 4.3 Ánh xạ kiểm thử

| Mã AC | Mã Test Case | Lần thực thi | Kết quả | Bằng chứng |
|---|---|---|---|---|
| AC-001 | TC-001 | [Mã thực thi] | Đạt | [Báo cáo] |
| AC-002 | TC-002 | [Mã thực thi] | Chờ xử lý | [Báo cáo] |

### 4.4 Ánh xạ triển khai

| Mã yêu cầu | Phiên bản release | Mã triển khai | Môi trường | Trạng thái |
|---|---|---|---|---|
| BR-001 | v1.0.0 | REL-001 | Production | Đã triển khai |

## 5. Phân tích yêu cầu mồ côi và khoảng trống

### 5.1 Yêu cầu mồ côi

Các yêu cầu không có artifact tương ứng ở các giai đoạn phía sau.

| Mã yêu cầu | Artifact còn thiếu | Tác động | Cách xử lý |
|---|---|---|---|
| BR-003 | User Story | Cao | Tạo User Story |

### 5.2 Task phát triển chưa được liên kết

Các task không có tham chiếu đến yêu cầu hợp lệ.

| Mã Task | Mô tả | Yêu cầu liên quan | Hành động |
|---|---|---|---|
| TASK-010 | [Mô tả] | Không có | Cần điều tra |

### 5.3 Yêu cầu chưa được kiểm thử

| Mã yêu cầu | AC liên quan | Test Case còn thiếu | Rủi ro |
|---|---|---|---|
| BR-002 | AC-003 | TC-003 | Cao |

### 5.4 Yêu cầu chưa được triển khai

| Mã yêu cầu | Độ ưu tiên | Trạng thái triển khai | Hành động |
|---|---|---|---|
| BR-004 | Phải có | Chưa bắt đầu | Leo thang |

## 6. Phân tích tác động thay đổi

Mỗi khi một yêu cầu thay đổi, PHẢI xác định toàn bộ artifact phía sau bị ảnh hưởng.

| Mã thay đổi | Artifact thay đổi | Yêu cầu liên quan | Artifact bị ảnh hưởng | Mức độ tác động |
|---|---|---|---|---|
| CHG-001 | BR-001 | BR-001 | US-001, AC-001, UC-001, DES-001, TC-001 | Cao |

### 6.1 Đánh giá tác động

- Tác động nghiệp vụ: [Mô tả]
- Tác động thiết kế: [Mô tả]
- Tác động phát triển: [Mô tả]
- Tác động kiểm thử: [Mô tả]
- Tác động triển khai: [Mô tả]
- Tác động tài liệu: [Mô tả]

### 6.2 Phê duyệt thay đổi

| Vai trò | Họ tên | Quyết định | Ngày |
|---|---|---|---|
| Business Analyst | [Họ tên] | [Quyết định] | [Ngày] |
| Product Owner | [Họ tên] | [Quyết định] | [Ngày] |
| Tech Lead | [Họ tên] | [Quyết định] | [Ngày] |

## 7. Chỉ số truy vết

| Chỉ số | Cách tính | Mục tiêu |
|---|---|---|
| Độ bao phủ từ Yêu cầu đến Story | Số BR có US liên kết / Tổng số BR đã duyệt | 100% |
| Độ bao phủ từ Story đến AC | Số US có AC / Tổng số US đã duyệt | 100% |
| Độ bao phủ kiểm thử yêu cầu | Số yêu cầu đã duyệt có test ánh xạ / Tổng số yêu cầu đã duyệt | 100% |
| Độ bao phủ triển khai yêu cầu | Số yêu cầu đã duyệt đã triển khai / Tổng số yêu cầu đã duyệt trong phạm vi release | 100% |
| Tỷ lệ Task mồ côi | Số Task không liên kết / Tổng số Task | 0% |
| Độ bao phủ đánh giá tác động thay đổi | Số thay đổi có đánh giá tác động / Tổng số thay đổi | 100% |

*Các chỉ số cần được tính trên phạm vi dự án đã duyệt và baseline release áp dụng.*

## 8. Review truy vết

### Checklist review

- [ ] Mọi Yêu cầu nghiệp vụ đã duyệt có mã duy nhất.
- [ ] Mọi Yêu cầu nghiệp vụ áp dụng được liên kết với User Story.
- [ ] Mọi User Story đã duyệt có Tiêu chí nghiệm thu.
- [ ] Mọi yêu cầu áp dụng có Use Case hoặc lý do được ghi nhận khi không cần.
- [ ] Artifact thiết kế được liên kết với yêu cầu nguồn.
- [ ] Task phát triển tham chiếu đến yêu cầu đã duyệt hoặc công việc kỹ thuật được ủy quyền.
- [ ] Test Case bao phủ các Tiêu chí nghiệm thu áp dụng.
- [ ] Mọi yêu cầu mồ côi quan trọng đã được xử lý.
- [ ] Các thay đổi yêu cầu đã có đánh giá tác động.
- [ ] Thông tin truy vết được cập nhật.

## 9. Phê duyệt

| Vai trò | Họ tên | Quyết định | Ngày | Ghi chú |
|---|---|---|---|---|
| Business Analyst | [Họ tên] | [Quyết định] | [Ngày] | [Ghi chú] |
| Product Owner | [Họ tên] | [Quyết định] | [Ngày] | [Ghi chú] |
| Tech Lead | [Họ tên] | [Quyết định] | [Ngày] | [Ghi chú] |
| QA Lead | [Họ tên] | [Quyết định] | [Ngày] | [Ghi chú] |

## 10. Lịch sử thay đổi

| Phiên bản | Ngày | Tác giả | Mô tả thay đổi |
|---|---|---|---|
| 1.0 | [Ngày] | [Tác giả] | Phiên bản khởi tạo |

---

**Hướng dẫn cho AI:**
- Duy trì truy vết xuyên suốt mọi giai đoạn SDLC.
- KHÔNG tạo mã ID trùng với artifact đã tồn tại.
- Phát hiện liên kết còn thiếu, yêu cầu mồ côi và yêu cầu chưa được kiểm thử.
- Xác định tác động xuôi dòng khi yêu cầu thay đổi.
- KHÔNG đánh dấu artifact là đã duyệt chỉ vì artifact đó tồn tại.
- Phân biệt liên kết còn thiếu với liên kết không áp dụng hợp lệ.
- Báo cáo khoảng trống truy vết kèm mức độ nghiêm trọng và hành động đề xuất.
- Giữ nguyên quan hệ lịch sử khi yêu cầu được thay đổi hoặc loại bỏ.
- Yêu cầu con người review đối với các thay đổi yêu cầu quan trọng.
