# Quy ước định danh (ID Conventions)

## 1. Mục đích

Tài liệu này định nghĩa các quy tắc định danh chuẩn cho artifact được tạo ra và duy trì trong suốt AI-Driven SDLC Framework.

Mục tiêu:

- Đảm bảo mọi artifact có một định danh duy nhất.
- Cho phép truy vết giữa các artifact liên quan.
- Hỗ trợ tham chiếu xuyên suốt các giai đoạn.
- Hỗ trợ kiểm tra và báo cáo tự động.
- Ngăn chặn định danh trùng lặp hoặc không rõ ràng.

## 2. Nguyên tắc chung

1. Mỗi artifact cần được theo dõi chính thức PHẢI có một ID.
2. ID PHẢI là duy nhất trong phạm vi dự án và namespace của artifact.
3. ID PHẢI giữ nguyên trong suốt vòng đời của artifact.
4. ID của artifact đã bị xóa, hủy, từ chối hoặc ngừng sử dụng KHÔNG ĐƯỢC tái sử dụng.
5. ID KHÔNG ĐƯỢC mang thông tin có thể thay đổi như trạng thái, người phụ trách hoặc mức ưu tiên.
6. ID NÊN vừa dễ đọc với con người, vừa dễ xử lý bằng máy.
7. Các artifact liên quan PHẢI tham chiếu lẫn nhau bằng ID.

## 3. Định dạng ID chuẩn

Sử dụng định dạng:

`{PREFIX}-{SEQUENCE}`

Ví dụ:

- `BRD-0001`
- `BRQ-0001`
- `BR-0001`
- `US-0001`
- `AC-0001`
- `TASK-0001`
- `TC-0001`

Trong đó:

| Thành phần | Mô tả |
|---|---|
| PREFIX | Định danh loại artifact. |
| SEQUENCE | Số thứ tự tăng dần, độ dài cố định 4 chữ số (có số 0 đứng đầu). |

Số thứ tự PHẢI được quản lý trong phạm vi dự án và namespace của artifact.

Nếu nhiều repository hoặc nhiều nhóm cùng sử dụng một namespace dự án, họ PHẢI dùng cơ chế cấp phát ID được phối hợp.

## 4. Prefix chuẩn

| Prefix | Loại artifact | Giai đoạn SDLC |
|---|---|---|
| BRD | Business Requirements Document (Tài liệu yêu cầu nghiệp vụ) | Requirement Analysis |
| BRQ | Business Requirement (Một yêu cầu nghiệp vụ trong BRD) | Requirement Analysis |
| BR | Business Rule (Quy tắc nghiệp vụ) | Requirement Analysis |
| NFR | Non-Functional Requirement (Yêu cầu phi chức năng) | Requirement Analysis |
| EPIC | Epic | Requirement Analysis |
| US | User Story | Requirement Analysis |
| AC | Acceptance Criteria (Tiêu chí nghiệm thu) | Requirement Analysis |
| UC | Use Case | Requirement Analysis |
| STK | Stakeholder (Bên liên quan) | Requirement Analysis |
| DES | Design Document (Tài liệu thiết kế) | System Design |
| ADR | Architecture Decision Record | System Design |
| API | API Specification (Đặc tả API) | System Design |
| DB | Database Design (Thiết kế cơ sở dữ liệu) | System Design |
| TASK | Development Task (Task phát triển) | Task Planning |
| SPIKE | Technical Investigation (Điều tra kỹ thuật) | Task Planning |
| DPN | Dependency (Phụ thuộc của yêu cầu, phạm vi, task hoặc kế hoạch) | Cross-stage |
| CR | Code Review | Code Review |
| TC | Test Case | Testing & QA |
| TS | Test Suite (Bộ test) | Testing & QA |
| BUG | Defect / Bug (Lỗi) | Testing & QA |
| TESTRUN | Test Execution (Lần thực thi test) | Testing & QA |
| REL | Release | Deployment |
| DEP | Deployment Record (Bản ghi triển khai) | Deployment |
| INC | Incident (Sự cố) | Monitoring & Maintenance |
| PROB | Problem Record (Bản ghi vấn đề gốc) | Monitoring & Maintenance |
| CR | Change Request (Yêu cầu thay đổi) | Cross-stage |
| RISK | Risk (Rủi ro) | Cross-stage |
| DEC | Decision (Quyết định) | Cross-stage |

Dự án CÓ THỂ định nghĩa thêm prefix khi cần.

Prefix mới PHẢI được tài liệu hóa trước khi sử dụng.

**Chuyển đổi ID dependency:** Dùng `DPN-xxxx` cho dependency mới ở mọi stage. Với hồ sơ hiện có dùng `DEP-xxxx` hoặc `TDEP-xxxx` cho dependency, giữ nguyên ID trong hồ sơ lịch sử và lưu ánh xạ ID cũ → ID `DPN` duy nhất trong sổ dependency của dự án; cập nhật tham chiếu trong tài liệu đang dùng theo quy trình quản lý thay đổi. Không đổi ID bản ghi triển khai `DEP-xxxx` hoặc sửa baseline đã duyệt tại chỗ.

## 5. Quan hệ giữa các ID

Artifact NÊN tham chiếu đến artifact liên quan bằng ID của chúng.

Ví dụ:

- `BRD-0001` chứa yêu cầu nghiệp vụ `BRQ-0001`.
- Quy tắc nghiệp vụ `BR-0001` áp dụng cho `BRQ-0001`.
- `BRQ-0001` được phân rã thành `US-0001`.
- `US-0001` được hỗ trợ bởi `AC-0001`.
- `AC-0001` được hiện thực bởi `TASK-0001`.
- `TASK-0001` được kiểm chứng bởi `TC-0001`.
- `TC-0001` góp phần xác nhận `REL-0001`.

Một artifact có thể tham chiếu nhiều artifact liên quan.

Việc tham chiếu KHÔNG ĐƯỢC chỉ dựa vào tên file hoặc tiêu đề tài liệu.

## 6. Quy tắc cấp phát ID

1. Gán ID khi artifact được tạo và đi vào quy trình theo dõi chính thức.
2. Không gán ID cho ghi chú tạm thời hoặc bản nháp dùng một lần, trừ khi chính sách dự án yêu cầu.
3. KHÔNG thay đổi ID hiện có chỉ vì tiêu đề hoặc phạm vi của artifact thay đổi.
4. KHÔNG tái sử dụng ID sau khi artifact bị xóa hoặc hủy.
5. Nếu một artifact bị tách, tạo ID mới cho các artifact kết quả và ghi nhận quan hệ.
6. Nếu nhiều artifact được gộp, giữ lại hoặc tạo ID được chỉ định làm ID đại diện và ghi nhận lịch sử gộp.

## 7. Phạm vi dự án

ID là duy nhất trong phạm vi một dự án.

Các dự án khác nhau CÓ THỂ dùng cùng một ID vì mỗi dự án có namespace riêng.

Khi tham chiếu chéo giữa các dự án, PHẢI kèm định danh dự án:

`{PROJECT-ID}:{ARTIFACT-ID}`

Ví dụ:

`CRM:BRQ-0001`

## 8. Yêu cầu metadata

Artifact được theo dõi chính thức NÊN có các trường sau:

| Trường | Bắt buộc | Mô tả |
|---|---|---|
| ID | Có | Định danh duy nhất của artifact. |
| Title | Có | Tiêu đề artifact. |
| Type | Có | Loại artifact. |
| Status | Có | Trạng thái vòng đời hiện tại. |
| Created Date | Có | Ngày tạo. |
| Created By | Có | Người hoặc AI agent đã tạo artifact. |
| Owner | Khuyến nghị | Người phụ trách artifact. |
| Version | Có | Phiên bản hiện tại của artifact. |
| Related IDs | Khi áp dụng | Tham chiếu đến các artifact liên quan. |

## 9. Hướng dẫn cho AI

AI Agent PHẢI:

- Tuân theo định dạng ID đã định nghĩa.
- Kiểm tra các ID hiện có trước khi đề xuất ID mới.
- KHÔNG bịa ra ID và khẳng định ID đó đã được đăng ký chính thức.
- KHÔNG tái sử dụng ID đã tồn tại.
- Giữ nguyên ID khi cập nhật artifact hiện có.
- Yêu cầu cấp phát ID khi không có cơ chế cấp phát đáng tin cậy.
- Duy trì quan hệ giữa các artifact liên quan.
- Báo cáo ID trùng lặp hoặc không hợp lệ.

AI Agent KHÔNG ĐƯỢC tự ý thay đổi ID của artifact đã được phê duyệt.
