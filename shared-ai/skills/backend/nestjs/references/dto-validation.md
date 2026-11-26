# DTO và validation

- Khai báo DTO cho body/query khi cần; với route param đơn, có thể dùng pipe phù hợp như `ParseIntPipe`. Tách input khỏi entity và response DTO; không trả entity thô.
- Kiểm tra phiên bản `class-validator`/`class-transformer` và `ValidationPipe` hiện có (toàn cục hoặc theo route) trước khi thêm; theo cấu hình dự án.
- Bật `whitelist` và cân nhắc `forbidNonWhitelisted` để loại hoặc từ chối field thừa (chống mass assignment); bật `transform` khi cần ép kiểu và kiểm tra kết quả.
- Khai báo ràng buộc rõ trên từng field (kiểu, độ dài, enum, định dạng); với object/mảng lồng nhau dùng `@ValidateNested` kèm `@Type`.
- Validation DTO chỉ kiểm tra dạng dữ liệu; quyền theo tài nguyên và invariant nghiệp vụ vẫn thuộc service.
- Lỗi validation trả theo định dạng lỗi chung của dự án, không lộ chi tiết nội bộ; xem [xử lý lỗi](exception-handling.md).
- Kiểm thử các trường hợp thiếu field, sai kiểu, field thừa và giá trị biên; xem [kiểm thử](testing.md).
