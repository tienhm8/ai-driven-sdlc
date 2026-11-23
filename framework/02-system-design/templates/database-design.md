# Mẫu Thiết kế Cơ sở dữ liệu

## 1. Kiểm soát tài liệu
| Trường | Giá trị |
|---|---|
| CSDL / miền nghiệp vụ | |
| ID / phiên bản thiết kế | `DB-XXX / 0.1` |
| Trạng thái | `Draft / In Review / Approved` |
| Chủ sở hữu | |
| Requirement baseline | |
| Engine / phiên bản CSDL | |

## 2. Yêu cầu dữ liệu & Khối lượng công việc
- Mục đích nghiệp vụ:
- Mẫu đọc/ghi:
- Khối lượng và tốc độ tăng trưởng ước tính:
- Yêu cầu transaction / nhất quán:
- Mục tiêu sẵn sàng và phục hồi:
- Phân loại dữ liệu / tuân thủ quy định:

## 3. Quyết định công nghệ
- Engine/phiên bản được chọn:
- Phương án thay thế và lý do:
- Hosting / topology:
- ADR liên quan:
- Ràng buộc vận hành:

## 4. Schema logic & vật lý
| Schema / Bảng | Mục đích | Primary key | Foreign key | Index quan trọng |
|---|---|---|---|---|

### Định nghĩa bảng — `[schema].[table_name]`
| Cột | Kiểu dữ liệu | Nullable | Mặc định | Khóa / constraint | Mô tả |
|---|---|---:|---|---|---|

## 5. Quan hệ & Toàn vẹn dữ liệu
- Quy tắc quan hệ:
- Constraint unique / check:
- Toàn vẹn tham chiếu:
- Hành vi khi xóa/cập nhật:
- Ranh giới transaction:

## 6. Index & Hiệu năng
| Mẫu truy vấn / truy cập | Index / tối ưu | Lợi ích kỳ vọng | Đánh đổi |
|---|---|---|---|
- Query plan / bằng chứng benchmark:
- Partitioning / sharding:
- Connection pooling / cache:

## 7. Bảo mật & Bảo vệ dữ liệu
- Role theo nguyên tắc least privilege:
- Mã hóa khi lưu trữ / khi truyền:
- Xử lý trường nhạy cảm:
- Bảo vệ bản backup:
- Audit log:
- Che dữ liệu khi dùng ngoài production:

## 8. Migration & Tương thích
- ID / script migration:
- Thứ tự migration:
- Backfill / kiểm tra:
- Rủi ro khóa bảng / downtime:
- Tương thích ngược:
- Chiến lược rollback / forward-fix:
- Backup trước migration:

## 9. Backup & Phục hồi
| Hạng mục | Mục tiêu / chính sách | Kiểm chứng |
|---|---|---|
| Tần suất backup | | |
| RPO | | |
| RTO | | |
| Kiểm thử restore | | |
| Thời gian lưu giữ | | |

## 10. Rủi ro, Truy vết & Phê duyệt
| Rủi ro / câu hỏi | Tác động | Giải pháp giảm thiểu / người phụ trách |
|---|---|---|

| ID Requirement | Bảng / trường / constraint | Bằng chứng |
|---|---|---|

| Người review | Vai trò | Quyết định | Ngày |
|---|---|---|---|
| | DBA / Data Architect | | |
| | Architect / Tech Lead | | |
