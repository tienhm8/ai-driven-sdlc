# General Coding Guidelines

## Thứ tự ưu tiên
Security/privacy/pháp lý và governance của framework → kiến trúc và contract đã duyệt cùng quy định của project → coding standard của framework → tài liệu này. Khi có xung đột, escalate lên Tech Lead; không tự chọn một cách âm thầm.

## Thiết kế và cấu trúc
- Tuân theo kiến trúc đã duyệt và ranh giới module. Giữ trách nhiệm gắn kết, interface nhỏ gọn.
- Tránh circular dependency, abstraction không cần thiết và coupling chặt. Ưu tiên pattern đã được project sử dụng.
- Đánh giá khả năng bảo trì, license, bảo mật và tương thích trước khi thêm dependency.

## Dễ đọc và đúng đắn
- Dùng tên miền nghiệp vụ có ý nghĩa; giữ hàm tập trung và side effect được thể hiện rõ. Tránh magic value và code chết/code debug.
- Validate dữ liệu tại các trust boundary. Xử lý null/empty, giá trị biên, timezone, locale, độ chính xác và tràn số theo quy tắc nghiệp vụ.
- Định nghĩa ranh giới transaction, tính nhất quán và idempotency cho side effect. Không nuốt lỗi hoặc trả về thành công giả.
- Comment giải thích lý do và ràng buộc, không mô tả những gì code đã thể hiện rõ.

## Test và hiệu năng
- Test hành vi: happy path, negative, biên và regression theo mức rủi ro. Test phải deterministic.
- Không xóa hoặc làm yếu test để che lỗi. Không khẳng định test đã pass khi chưa thực thi.
- Tránh N+1, query không giới hạn, blocking I/O và rò rỉ tài nguyên. Hỗ trợ cancellation khi phù hợp. Với lời gọi dependency, xem [quy tắc retry và timeout](error-handling.md#retry-và-timeout).
- Cân nhắc concurrency/race condition; đo lường trước khi tối ưu.

## Vệ sinh thay đổi
- Giữ PR tập trung và giải thích mục đích. Không commit secret hoặc file sinh ra/file cục bộ không cần thiết.
- Ghi tài liệu cho thay đổi API/schema/config và tính tương thích ngược. Không tự merge hoặc deploy; tuân theo G4 và các release gate.

## Code do AI sinh ra
Developer phải đọc và hiểu code được sinh ra; kiểm tra API, phiên bản thư viện, import, default không an toàn, license và nguồn gốc dependency. Output của AI không đáng tin chỉ vì nó biên dịch được.
