# Mẫu Thiết kế Bảo mật

## 1. Kiểm soát tài liệu
| Trường | Giá trị |
|---|---|
| Hệ thống / thành phần | |
| ID / phiên bản thiết kế bảo mật | `SEC-DES-XXX / 0.1` |
| Trạng thái | `Draft / In Review / Approved` |
| Chủ sở hữu bảo mật | |
| Kiến trúc / requirement liên quan | |

## 2. Phạm vi & Mục tiêu bảo mật
- Ranh giới hệ thống:
- Tài sản cần bảo vệ:
- Mục tiêu bảo mật:
- Chính sách / tiêu chuẩn áp dụng:
- Giả định / loại trừ:

## 3. Phân loại dữ liệu & Ranh giới tin cậy
| Dữ liệu / tài sản | Phân loại | Vị trí lưu trữ | Đường truyền | Biện pháp bảo vệ |
|---|---|---|---|---|

- Sơ đồ ranh giới tin cậy:
- Actor bên ngoài / phụ thuộc:
- PII / dữ liệu nhạy cảm:

## 4. Mô hình hóa mối đe dọa
| ID mối đe dọa | Tài sản / điểm vào | Kịch bản đe dọa | Tác động | Khả năng xảy ra | Biện pháp giảm thiểu | Rủi ro tồn dư |
|---|---|---|---|---|---|---|

- Phương pháp: `[STRIDE / attack tree / khác]`
- Kịch bản lạm dụng:
- Giả định cần kiểm chứng:

## 5. Quản lý định danh & truy cập (IAM)
- Xác thực:
- Mô hình phân quyền: `[RBAC / ABAC / dựa trên policy]`
- Ma trận role / quyền:
- Định danh giữa các service:
- Vòng đời session / token:
- Truy cập đặc quyền / phân tách nhiệm vụ:

## 6. Bảo mật ứng dụng & API
- Kiểm tra đầu vào / mã hóa đầu ra:
- Chống injection:
- CSRF / CORS:
- Rate limiting / chống lạm dụng:
- Kiểm soát upload file:
- Truy cập mức object:
- Xử lý lỗi an toàn:

## 7. Hạ tầng & Secret
- Phân tách mạng:
- TLS / mã hóa:
- Lưu trữ và xoay vòng secret:
- Hardening runtime / container:
- Quét dependency và image:
- Truy cập quản trị:

## 8. Bảo vệ dữ liệu & Quyền riêng tư
- Mã hóa khi lưu trữ / khi truyền:
- Quản lý khóa:
- Che / tokenization:
- Tối thiểu hóa dữ liệu:
- Lưu giữ / xóa:
- Bảo vệ backup:
- Audit trail:

## 9. Phát hiện & Ứng phó
- Log / sự kiện bảo mật:
- Cảnh báo:
- Tham chiếu quy trình ứng phó sự cố:
- Yêu cầu điều tra số (forensic):
- Khôi phục / ngăn chặn:

## 10. Kế hoạch kiểm chứng
| Kiểm soát | Phương pháp kiểm chứng | Bằng chứng | Người phụ trách | Trạng thái |
|---|---|---|---|---|

- SAST / DAST / quét dependency:
- Kiểm thử xâm nhập (nếu yêu cầu):
- Xác nhận bảo mật:

## 11. Rủi ro tồn dư & Ngoại lệ
| Rủi ro / ngoại lệ | Lý do | Kiểm soát bù đắp | Người chịu rủi ro | Ngày review | Phê duyệt |
|---|---|---|---|---|---|

## 12. Phê duyệt
| Người review | Vai trò | Quyết định | Ngày | Tham chiếu |
|---|---|---|---|---|
| | Reviewer bảo mật | | | |
| | Solution Architect | | | |
| | Chủ sở hữu hệ thống / dữ liệu (nếu cần) | | | |
