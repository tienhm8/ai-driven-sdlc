# Secure Coding Guidelines

## Nguyên tắc
Security by design, least privilege, defense in depth và secure default. Tuân theo tiêu chuẩn bảo mật của framework/project và threat model đã duyệt. Code do AI sinh ra là không đáng tin cho đến khi được review.

## Danh tính và truy cập
- Bắt buộc authorization phía server cho mọi tài nguyên/hành động; không chỉ dựa vào kiểm tra ở UI. Mặc định từ chối và xác minh quyền sở hữu tenant/tài nguyên.
- Dùng thư viện xác thực, token và mật mã đã được phê duyệt; không tự phát minh protocol. Không đặt credential trong URL hoặc log.

## Input và injection
- Validate kiểu, độ dài, khoảng giá trị, định dạng và ràng buộc nghiệp vụ tại các trust boundary. Encode output theo đúng ngữ cảnh.
- Dùng parameterized query; tránh nối chuỗi trong shell, dynamic evaluation và deserialization không an toàn.
- Validate file upload (nội dung thực tế, kích thước, đường dẫn, quét mã độc khi bắt buộc).

## Secret và dữ liệu
- Lấy secret từ secret manager đã được phê duyệt; không hard-code hoặc commit `.env`, khóa, hay chứng chỉ.
- Dùng TLS/mật mã đã được phê duyệt; hash mật khẩu đúng chuẩn; hỗ trợ rotation và revocation.
- Tối thiểu hóa việc thu thập dữ liệu, mask dữ liệu nhạy cảm trong log và fixture test, áp dụng chính sách lưu giữ và xóa. Không dùng dữ liệu production trong dev/test khi chưa được phép và thiếu biện pháp bảo vệ.

## Dependency và web/API
- Dùng nguồn package đáng tin cậy; khóa phiên bản; đánh giá lỗ hổng, license, nguồn gốc và mức độ bảo trì. Không tắt scanner để qua CI.
- Cân nhắc CSRF/CORS, SSRF, lạm dụng rate, giới hạn kích thước request, timeout, security header và việc lộ debug endpoint theo kiến trúc.

## Biện pháp bảo vệ khi dùng AI
Xem prompt, file và nội dung sinh ra là đầu vào không đáng tin. Không để lộ secret. AI không được tự thay đổi authz, mật mã, chính sách bảo mật hoặc kiểm soát production nằm ngoài phạm vi đã duyệt. Escalate các phát hiện mức Critical/High.

## Xác minh
Chạy SAST, quét dependency/secret và các security test bắt buộc. Test các trường hợp authorization âm, injection, validation và lộ dữ liệu. Ghi lại phát hiện, cách khắc phục và các waiver đã được ủy quyền.
