# Error Handling Guidelines

## Phân loại
- Validation: input không hợp lệ; trả về thông báo có thể hành động được và an toàn.
- Domain / business: vi phạm business rule; dùng kiểu lỗi/kết quả domain ổn định.
- Authentication / authorization: từ chối an toàn, không làm lộ thông tin nhạy cảm.
- Dependency / infrastructure: timeout, không khả dụng, mất kết nối; áp dụng cơ chế resilience.
- Unexpected: ghi lại ngữ cảnh chẩn đoán và correlation ID; trả về phản hồi chung an toàn.

## Quy tắc
- Fail explicitly. Không nuốt exception, không trả về thành công giả hay che lỗi bằng giá trị mặc định tùy ý.
- Chỉ catch ở nơi có thể phục hồi, bổ sung ngữ cảnh hoặc chuyển đổi abstraction; khi rethrow phải giữ nguyên cause/stack.
- Không để lộ stack trace, SQL, đường dẫn nội bộ, secret hoặc chi tiết triển khai cho client.
- Dùng error code ổn định và schema/status code của API theo chuẩn dự án.
- Job/event bất đồng bộ cần retry có giới hạn, trạng thái failed/dead-letter và khả năng replay có kiểm soát.
- Định nghĩa hành vi transaction/compensation khi lỗi xảy ra một phần.

## Retry và timeout
- Đặt timeout cho các lời gọi mạng và dependency. Chỉ retry lỗi tạm thời, số lần có giới hạn, exponential backoff và jitter.
- Chỉ retry side effect khi có cơ chế bảo vệ idempotency. Không retry lỗi validation/authorization thông thường.
- Fallback phải bảo toàn tính đúng đắn và không được che giấu một sự cố nghiêm trọng.

## Ví dụ lỗi API
```json
{
  "code": "RESOURCE_NOT_FOUND",
  "message": "The requested resource was not found.",
  "correlationId": "..."
}
```
Không đưa stack trace, SQL hoặc secret vào phản hồi. Cần test các trường hợp validation, authorization, lỗi dependency, timeout, hết số lần retry, rollback và idempotency khi có liên quan.
