# Tiêu chuẩn thiết kế cơ sở dữ liệu (Database Design Standards)

## 1. Mục đích

Định nghĩa các tiêu chuẩn chung cho mô hình hóa cơ sở dữ liệu, thiết kế schema, triển khai, migration và quản lý dữ liệu.

## 2. Nguyên tắc chung

Thiết kế cơ sở dữ liệu PHẢI ưu tiên:

- Tính toàn vẹn dữ liệu.
- Tính nhất quán.
- Bảo mật.
- Khả năng bảo trì.
- Hiệu năng.
- Khả năng mở rộng.
- Khả năng phục hồi.
- Quyền sở hữu dữ liệu rõ ràng.

Các quyết định thiết kế cơ sở dữ liệu PHẢI xem xét yêu cầu nghiệp vụ và khối lượng công việc dự kiến.

## 3. Lựa chọn công nghệ cơ sở dữ liệu

Công nghệ cơ sở dữ liệu PHẢI được lựa chọn dựa trên:

- Cấu trúc dữ liệu và mẫu truy cập.
- Yêu cầu giao dịch (transaction).
- Yêu cầu về tính nhất quán.
- Yêu cầu khả năng mở rộng.
- Yêu cầu tính sẵn sàng.
- Năng lực vận hành.
- Yêu cầu bảo mật và tuân thủ.

Công nghệ được chọn và lý do lựa chọn NÊN được ghi nhận trong các quyết định kiến trúc.

## 4. Quy ước đặt tên

Dự án PHẢI sử dụng quy ước đặt tên nhất quán.

Quy ước khuyến nghị:

| Đối tượng | Quy ước | Ví dụ |
|---|---|---|
| Table | snake_case | `customer_orders` |
| Column | snake_case | `created_at` |
| Primary key | `id` hoặc theo quy định của dự án | `id` |
| Foreign key | `{entity}_id` | `customer_id` |
| Index | `idx_{table}_{columns}` | `idx_orders_customer_id` |
| Unique constraint | `uq_{table}_{columns}` | `uq_users_email` |
| Foreign key constraint | `fk_{table}_{reference}` | `fk_orders_customer` |

NÊN KHÔNG sử dụng từ khóa dành riêng (reserved keyword) làm định danh.

## 5. Mô hình hóa dữ liệu

Mô hình cơ sở dữ liệu PHẢI:

- Biểu diễn chính xác các thực thể và mối quan hệ nghiệp vụ.
- Định nghĩa khóa chính.
- Định nghĩa khóa ngoại khi cần toàn vẹn quan hệ.
- Định nghĩa các ràng buộc unique phù hợp.
- Khai báo rõ ràng khả năng null của từng cột.
- Định nghĩa kiểu dữ liệu phù hợp.
- Tránh trùng lặp dữ liệu không cần thiết.
- Hỗ trợ các truy vấn nghiệp vụ cần thiết.

Các mối quan hệ PHẢI được xác định rõ ràng:

- Một-một (one-to-one).
- Một-nhiều (one-to-many).
- Nhiều-nhiều (many-to-many).

Quan hệ nhiều-nhiều trong cơ sở dữ liệu quan hệ NÊN sử dụng bảng trung gian (junction table) tường minh khi phù hợp.

## 6. Kiểu dữ liệu và độ chính xác

Kiểu dữ liệu PHẢI phù hợp với ý nghĩa nghiệp vụ.

Ví dụ:

- Giá trị tiền tệ PHẢI dùng kiểu decimal với độ chính xác phù hợp, không dùng kiểu số thực dấu phẩy động khi cần tính toán tài chính chính xác.
- Ngày và thời điểm PHẢI có ngữ nghĩa và cách xử lý múi giờ được định nghĩa rõ ràng.
- Trường boolean PHẢI biểu diễn rõ ràng ý nghĩa đúng/sai.
- Trường văn bản lớn CHỈ được dùng khi có lý do chính đáng.
- Trường số PHẢI định nghĩa độ chính xác và phạm vi phù hợp.

Dự án PHẢI định nghĩa một chiến lược nhất quán để lưu trữ và hiển thị thời điểm, ưu tiên dùng UTC cho các thời điểm được lưu trữ.

## 7. Ràng buộc và toàn vẹn dữ liệu

Cơ sở dữ liệu NÊN thực thi các quy tắc toàn vẹn dữ liệu quan trọng thông qua:

- Ràng buộc khóa chính.
- Ràng buộc khóa ngoại.
- Ràng buộc unique.
- Ràng buộc check.
- Ràng buộc not null.

Kiểm tra ở tầng ứng dụng KHÔNG ĐƯỢC là cơ chế bảo vệ duy nhất cho toàn vẹn dữ liệu quan trọng.

## 8. Index và hiệu năng

Index NÊN được tạo dựa trên mẫu truy vấn thực tế và yêu cầu hiệu năng.

Trước khi thêm index, kỹ sư NÊN cân nhắc:

- Tần suất truy vấn.
- Điều kiện lọc.
- Điều kiện join.
- Yêu cầu sắp xếp.
- Chi phí ghi.
- Chi phí lưu trữ.

Index PHẢI được rà soát để loại bỏ những định nghĩa trùng lặp hoặc không được sử dụng.

Các truy vấn quan trọng về hiệu năng NÊN được phân tích bằng công cụ phân tích thực thi truy vấn phù hợp.

## 9. Giao dịch và đồng thời

Các thao tác cần tính nguyên tử (atomicity) PHẢI sử dụng cơ chế giao dịch phù hợp.

Quá trình triển khai PHẢI xem xét:

- Ranh giới giao dịch.
- Yêu cầu mức cô lập (isolation).
- Deadlock.
- Cập nhật đồng thời.
- Khóa lạc quan hoặc khóa bi quan khi phù hợp.
- Hành vi retry.

NÊN tránh giao dịch phân tán (distributed transaction) trừ khi có lý do chính đáng. Có thể cân nhắc các mẫu thay thế như Saga hoặc Outbox.

## 10. Migration cơ sở dữ liệu

Mọi thay đổi schema cơ sở dữ liệu PHẢI được quản lý phiên bản.

Script migration PHẢI:

- Có thể chạy lặp lại hoặc được kiểm soát an toàn thông qua công cụ migration.
- Định nghĩa hành vi nâng cấp (upgrade).
- Cân nhắc việc bảo toàn dữ liệu.
- Được kiểm thử trước khi triển khai production.
- Có chiến lược rollback hoặc phục hồi khi khả thi.
- Tránh thay đổi mang tính phá hủy nếu chưa đánh giá tác động rõ ràng.

Migration trên production PHẢI tuân theo quy trình phê duyệt triển khai.

## 11. Bảo mật dữ liệu

Cơ sở dữ liệu PHẢI tuân theo nguyên tắc quyền tối thiểu (least privilege).

Dữ liệu nhạy cảm PHẢI được bảo vệ theo mức phân loại của nó.

Quá trình triển khai PHẢI:

- Không hardcode thông tin xác thực.
- Sử dụng cơ chế quản lý secret an toàn.
- Mã hóa dữ liệu khi truyền (encryption in transit).
- Mã hóa dữ liệu khi lưu trữ (encryption at rest) khi rủi ro hoặc quy định yêu cầu.
- Hạn chế quyền truy cập vào bảng và trường nhạy cảm.
- Không ghi log các giá trị nhạy cảm.
- Sử dụng truy vấn tham số hóa (parameterized query) hoặc cơ chế xây dựng truy vấn an toàn.

Việc lưu giữ và xóa dữ liệu PHẢI tuân theo quy định pháp lý và chính sách của dự án.

## 12. Sao lưu và phục hồi

Cơ sở dữ liệu production PHẢI có chiến lược sao lưu và phục hồi đã được phê duyệt.

Chiến lược NÊN định nghĩa:

- Tần suất sao lưu.
- Thời gian lưu trữ bản sao lưu.
- Mã hóa bản sao lưu.
- Recovery Point Objective (RPO).
- Recovery Time Objective (RTO).
- Kiểm thử khôi phục.
- Trách nhiệm khi khôi phục sau thảm họa (disaster recovery).

Một bản sao lưu chỉ được coi là đáng tin cậy sau khi việc khôi phục đã được kiểm thử.

## 13. Vòng đời dữ liệu

Dự án PHẢI định nghĩa chính sách vòng đời dữ liệu khi áp dụng:

- Tạo dữ liệu.
- Sửa đổi dữ liệu.
- Lưu trữ (archival).
- Thời gian lưu giữ (retention).
- Xóa dữ liệu.
- Ẩn danh hoặc giả danh hóa (anonymization hoặc pseudonymization).

Các thao tác xóa dữ liệu mang tính phá hủy PHẢI có biện pháp bảo vệ và được ủy quyền phù hợp.

## 14. Yêu cầu kiểm thử

Thay đổi cơ sở dữ liệu NÊN bao gồm kiểm thử cho:

- Tính đúng đắn của schema.
- Các ràng buộc.
- Migration.
- Toàn vẹn dữ liệu.
- Hành vi giao dịch.
- Tính đúng đắn của truy vấn.
- Các thao tác quan trọng về hiệu năng.
- Quy trình sao lưu và khôi phục khi áp dụng.

## 15. Quy tắc triển khai cho AI

AI Agent PHẢI:

- Kiểm tra các model cơ sở dữ liệu hiện có trước khi đề xuất thay đổi.
- Bảo toàn dữ liệu và quan hệ hiện có, trừ khi thay đổi đã được phê duyệt rõ ràng.
- Tạo script migration cho mọi thay đổi schema.
- Nhận diện các thao tác mang tính phá hủy.
- Không trực tiếp sửa đổi dữ liệu production.
- Xem xét index và hiệu năng truy vấn.
- Đánh dấu các thay đổi ảnh hưởng đến khả năng tương thích hoặc lưu giữ dữ liệu.
- Yêu cầu con người review đối với các thay đổi schema hoặc dữ liệu có rủi ro cao.

## 16. Tài liệu tham chiếu

- `api-standards.md`
- `../coding/testing-standards.md`
- `../security/security-standards.md`
