# Tiêu chuẩn thiết kế API (API Design Standards)

## 1. Mục đích

Định nghĩa các tiêu chuẩn chung cho việc thiết kế, triển khai, tài liệu hóa và bảo trì API trong các dự án áp dụng framework.

## 2. Nguyên tắc chung

API PHẢI tuân theo các nguyên tắc sau:

- Nhất quán: Sử dụng quy ước đặt tên, cấu trúc và quy tắc thống nhất.
- Đơn giản: Giữ giao diện dễ hiểu và có thể dự đoán.
- Bảo mật: Áp dụng xác thực, phân quyền và kiểm tra dữ liệu đầu vào.
- Tin cậy: Xử lý lỗi và đầu vào bất thường một cách nhất quán.
- Tương thích: Tránh làm hỏng các consumer hiện có nếu không có quy trình migration được kiểm soát.
- Khả năng quan sát: Cung cấp đủ thông tin cho giám sát và xử lý sự cố.
- Tài liệu: Giữ tài liệu API đồng bộ với triển khai thực tế.

## 3. Kiểu API

Dự án NÊN chọn kiểu API phù hợp với kiến trúc và trường hợp sử dụng, ví dụ:

- REST.
- GraphQL.
- gRPC.
- Giao diện hướng sự kiện (event-driven).

Kiểu API được chọn PHẢI được ghi nhận trong tài liệu kiến trúc hoặc cấu hình công nghệ của dự án.

Một dự án CÓ THỂ hỗ trợ nhiều kiểu API khi yêu cầu kiến trúc có lý do chính đáng.

## 4. Quy ước REST API

Đối với REST API:

### 4.1 Đặt tên tài nguyên

- Tên tài nguyên PHẢI là danh từ.
- Tên tài nguyên NÊN ở dạng số nhiều.
- Tên tài nguyên NÊN dùng lowercase kebab-case.
- Cấu trúc phân cấp tài nguyên PHẢI thể hiện mối quan hệ có ý nghĩa.
- NÊN tránh các endpoint hướng hành động (action-oriented) trừ khi thao tác không thể biểu diễn tự nhiên dưới dạng tài nguyên.

Ví dụ:

```text
GET    /api/v1/customers
GET    /api/v1/customers/{customerId}
POST   /api/v1/customers
PUT    /api/v1/customers/{customerId}
PATCH  /api/v1/customers/{customerId}
DELETE /api/v1/customers/{customerId}
```

### 4.2 HTTP Methods

| Method | Mục đích |
|---|---|
| GET | Lấy tài nguyên |
| POST | Tạo tài nguyên hoặc thực thi một thao tác |
| PUT | Thay thế toàn bộ tài nguyên |
| PATCH | Cập nhật một phần tài nguyên |
| DELETE | Xóa tài nguyên |

Quá trình triển khai PHẢI tôn trọng đúng ngữ nghĩa dự kiến của các HTTP method.

### 4.3 HTTP Status Codes

| Code | Ý nghĩa |
|---|---|
| 200 | Yêu cầu thành công |
| 201 | Tài nguyên đã được tạo |
| 202 | Yêu cầu đã được chấp nhận để xử lý bất đồng bộ |
| 204 | Yêu cầu thành công nhưng không có response body |
| 400 | Yêu cầu không hợp lệ |
| 401 | Cần xác thực hoặc xác thực thất bại |
| 403 | Truy cập bị từ chối |
| 404 | Không tìm thấy tài nguyên |
| 409 | Xung đột tài nguyên |
| 422 | Dữ liệu đầu vào không hợp lệ về ngữ nghĩa, khi dự án áp dụng |
| 429 | Vượt quá giới hạn tần suất (rate limit) |
| 500 | Lỗi máy chủ nội bộ |
| 502 | Bad gateway |
| 503 | Dịch vụ không khả dụng |
| 504 | Gateway timeout |

Dự án PHẢI sử dụng status code một cách nhất quán.

### 4.4 Request và Response

Cấu trúc request và response của API PHẢI:

- Sử dụng định dạng serialization nhất quán.
- Định nghĩa tên trường và kiểu dữ liệu.
- Phân biệt trường bắt buộc và trường tùy chọn.
- Định nghĩa ràng buộc kiểm tra dữ liệu.
- Tránh lộ chi tiết triển khai nội bộ.
- Tránh trả về thông tin nhạy cảm khi không cần thiết.

Ví dụ:

```json
{
  "data": {
    "id": "CUS-001",
    "name": "Example Customer"
  },
  "meta": {
    "requestId": "req-123"
  }
}
```

Cấu trúc envelope của response có thể do từng dự án quy định, nhưng PHẢI nhất quán trong cùng một API.

### 4.5 Error Response

Error response PHẢI cung cấp đủ thông tin để client hiểu và xử lý lỗi.

Ví dụ:

```json
{
  "error": {
    "code": "CUSTOMER_NOT_FOUND",
    "message": "Customer was not found",
    "requestId": "req-123"
  }
}
```

Error response KHÔNG ĐƯỢC lộ:

- Stack trace trên môi trường production.
- Thông tin đăng nhập cơ sở dữ liệu.
- Secret nội bộ.
- Thông tin cá nhân nhạy cảm.
- Chi tiết hạ tầng nội bộ có thể làm tăng rủi ro bảo mật.

## 5. Versioning API

API có hợp đồng (contract) được sử dụng bởi bên ngoài PHẢI có chiến lược tương thích và versioning được định nghĩa rõ ràng.

Với REST API, có thể sử dụng versioning theo số phiên bản lớn trong URL:

```text
/api/v1/customers
/api/v2/customers
```

Các thay đổi gây lỗi tương thích (breaking change) PHẢI tuân theo quy trình migration và deprecation đã được phê duyệt.

Các thay đổi không gây lỗi tương thích NÊN giữ được khả năng tương thích với consumer hiện có.

## 6. Phân trang, lọc và sắp xếp

Endpoint dạng danh sách NÊN hỗ trợ phân trang khi tập kết quả có thể lớn.

Dự án PHẢI định nghĩa cách tiếp cận nhất quán cho:

- Kích thước trang (page size).
- Kích thước trang tối đa.
- Điều hướng theo trang hoặc theo cursor.
- Sắp xếp.
- Lọc.
- Tham số tìm kiếm.

Ví dụ:

```text
GET /api/v1/customers?page=1&pageSize=20&sortBy=createdAt&sortOrder=desc
```

## 7. Kiểm tra dữ liệu đầu vào (Validation)

Mọi dữ liệu đầu vào từ bên ngoài PHẢI được kiểm tra ở phía server.

Việc kiểm tra PHẢI bao gồm:

- Kiểu dữ liệu.
- Các trường bắt buộc.
- Ràng buộc độ dài.
- Ràng buộc định dạng.
- Giá trị được phép.
- Quy tắc nghiệp vụ.
- Phân quyền và quyền sở hữu tài nguyên.

Kiểm tra ở phía client KHÔNG ĐƯỢC thay thế kiểm tra ở phía server.

## 8. Xác thực và phân quyền

API PHẢI:

- Yêu cầu xác thực khi phù hợp.
- Thực thi phân quyền cho các thao tác được bảo vệ.
- Áp dụng nguyên tắc quyền tối thiểu (least privilege).
- Kiểm tra access token hoặc thông tin xác thực.
- Không tin tưởng định danh hoặc quyền do client cung cấp khi chưa được xác minh.
- Bảo vệ các thao tác nhạy cảm khỏi truy cập trái phép.

Việc triển khai bảo mật cũng PHẢI tuân theo `../security/security-standards.md`.

## 9. Giới hạn tần suất và độ tin cậy

API công khai và API có thể truy cập từ bên ngoài NÊN triển khai rate limiting.

API NÊN định nghĩa:

- Hành vi timeout.
- Hành vi retry.
- Yêu cầu idempotency.
- Hành vi xử lý đồng thời (concurrency).
- Cách xử lý lỗi.
- Chiến lược circuit breaker khi phù hợp.

Các thao tác có thể bị retry PHẢI xem xét khả năng thực thi trùng lặp và các tác dụng phụ.

## 10. Tài liệu API

API NÊN sử dụng OpenAPI hoặc đặc tả machine-readable tương đương khi phù hợp.

Tài liệu PHẢI mô tả:

- Endpoint và HTTP method.
- Tham số request.
- Request body.
- Schema của response.
- Status code.
- Yêu cầu xác thực.
- Quy tắc kiểm tra dữ liệu.
- Ví dụ request và response.

## 11. Yêu cầu kiểm thử

Triển khai API PHẢI có kiểm thử phù hợp cho:

- Request thành công.
- Request không hợp lệ.
- Xác thực thất bại.
- Phân quyền thất bại.
- Tài nguyên không tồn tại.
- Các điều kiện biên.
- Xử lý lỗi.
- Tính tương thích.

## 12. Quy tắc triển khai cho AI

AI Agent PHẢI:

- Tuân theo quy ước API hiện có của dự án.
- Tái sử dụng cấu trúc response và error đã được thiết lập.
- Tránh đặt tên endpoint không nhất quán.
- Tránh thay đổi gây lỗi tương thích mà không được tài liệu hóa.
- Tạo hoặc cập nhật đặc tả API khi cần.
- Nhận diện rủi ro bảo mật và tương thích.
- Yêu cầu con người review đối với các thay đổi đáng kể về hợp đồng API.

## 13. Tài liệu tham chiếu

- `database-standards.md`
- `../coding/testing-standards.md`
- `../security/security-standards.md`
- `../documentation/documentation-standards.md`
