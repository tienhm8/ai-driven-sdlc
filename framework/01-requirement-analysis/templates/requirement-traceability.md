# Ma trận truy vết yêu cầu (Requirement Traceability Matrix — RTM)

## 1. Thông tin tài liệu

| Trường | Giá trị |
|---|---|
| Mã tài liệu | RTM-0001 |
| Dự án | [Tên dự án] |
| Phiên bản | 0.1 |
| Trạng thái | Draft |
| Owner | [Business Analyst] |
| Ngày cập nhật | [YYYY-MM-DD] |

## 2. Mục đích và phạm vi

RTM tại Requirement Analysis truy vết BRQ → FR/NFR → User Story/Use Case → Acceptance Criteria. Test Case, thiết kế, task, implementation và deployment được liên kết ở các giai đoạn tương ứng.

- Mọi liên kết tham chiếu ID artifact; không chỉ dựa trên tên file/tiêu đề.
- Ghi nhận rõ liên kết thiếu, chưa xác định hoặc không áp dụng.
- Không ghi Test Case IDs trước khi được tạo ở Stage 06.

## 3. Ma trận truy vết Stage 01

| BRQ ID | FR ID | NFR ID | US ID | UC ID | AC ID | Nguồn/ghi chú/khoảng trống |
|---|---|---|---|---|---|---|
| BRQ-0001 | FR-0001 | NFR-0001 / N/A | US-0001 | UC-0001 / N/A | AC-0001 | [Nguồn hoặc lý do N/A] |

Business Rules tham chiếu bằng BR ID trong Business Rules Catalogue; mỗi FR/NFR/US/UC/AC ghi ID liên quan phù hợp.

## 4. Khoảng trống và yêu cầu mồ côi

| Artifact/ID | Liên kết mong đợi | Tác động | Owner/hành động | Trạng thái |
|---|---|---|---|---|
| [ID] | [Artifact đích] | [Mô tả] | [Owner/action] | [Open/Resolved/N/A] |

## 5. Tóm tắt độ bao phủ

- BRQ → FR/NFR:
- FR/NFR → US/UC:
- US/UC → AC:
- Yêu cầu mồ côi/liên kết còn thiếu:
- Lý do cho liên kết N/A:

## 6. Thay đổi và tác động trong Stage 01

| Change/Decision ID | Artifact/ID thay đổi | Artifact/ID bị ảnh hưởng | Tác động | Owner |
|---|---|---|---|---|

## 7. Bàn giao truy vết downstream

| Stage | Liên kết cần bổ sung | Owner |
|---|---|---|
| System Design | Requirement → design/ADR/API/data artifacts | Solution Architect |
| Task Planning/Development | Requirement/US → task và implementation | Delivery/Engineering |
| Testing & QA (Stage 06) | Requirement/AC → Test Case và test evidence | QA |
| Deployment | Requirement/AC → release/deployment evidence khi áp dụng | Release owner |

## 8. Lịch sử thay đổi

| Phiên bản | Ngày | Người cập nhật | Mô tả | Nguồn/quyết định |
|---|---|---|---|---|
| 0.1 | [YYYY-MM-DD] | [Owner] | Bản nháp ban đầu | [Nguồn] |
