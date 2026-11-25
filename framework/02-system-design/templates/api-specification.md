# Mẫu Đặc tả API

## 1. Kiểm soát tài liệu
| Trường | Giá trị |
|---|---|
| Tên API / miền nghiệp vụ | |
| ID / phiên bản API | `API-XXX / v1` |
| Trạng thái | `Draft / In Review / Approved / Deprecated` |
| Chủ sở hữu | |
| Yêu cầu liên quan | |
| Base URL / service | |

## 2. Tổng quan API
- Mục đích và đối tượng sử dụng (consumer):
- Kiểu API: `[REST / GraphQL / gRPC / ...]`
- Giao thức / content type:
- Versioning và tương thích:
- Cơ chế xác thực:

## 3. Quy ước chung
- Đặt tên resource:
- Phân trang / lọc / sắp xếp:
- Ngày giờ và múi giờ:
- Idempotency:
- Correlation / request ID:
- Rate limit / quota:
- Timeout / retry:
- Định dạng lỗi chuẩn:

## 4. Đặc tả endpoint
### `[METHOD] [PATH]` — `[Tóm tắt]`
| Trường | Giá trị |
|---|---|
| ID endpoint | `API-EP-XXX` |
| Requirement / Story | |
| Mục đích | |
| Xác thực | |
| Phân quyền | Quyền/vai trò cần cho endpoint này; tham chiếu `SEC-DES-XXX §…` |
| Idempotent? | |
| Rate limit | |

**Path parameters**
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---:|---|

**Query parameters**
| Tên | Kiểu | Bắt buộc | Validation / mặc định | Mô tả |
|---|---|---:|---|---|

**Request body**
```json
{
  "exampleField": "value"
}
```

**Response thành công**
```json
{
  "data": {},
  "requestId": "example-request-id"
}
```

**Response lỗi**
| HTTP status | Mã lỗi | Điều kiện | Cách client xử lý |
|---|---|---|---|

**Quy tắc validation / nghiệp vụ**
1.

**Bảo mật / quyền riêng tư**
- Phân loại dữ liệu:
- Phân quyền mức field: theo `SEC-DES-XXX §…`; chỉ ghi phần riêng của endpoint.
- Trường nhạy cảm bị loại bỏ/che:

## 5. Mô hình lỗi dùng chung của API
| Mã lỗi | HTTP status | Ý nghĩa | Có thể retry? |
|---|---:|---|---|

## 6. Sự kiện / Webhook (nếu có)
| Sự kiện | Trigger | Schema payload | Gửi lại / retry | Chữ ký / xác minh |
|---|---|---|---|---|

**Với tích hợp bất đồng bộ, chốt thêm** (ghi `N/A` kèm lý do nếu không áp dụng):
| Sự kiện | Ngữ nghĩa giao nhận | Thứ tự (phạm vi bảo đảm) | Xử lý trùng (ID/khóa idempotency) | Phiên bản & thay đổi schema |
|---|---|---|---|---|
| | `at-most-once / at-least-once / exactly-once (điều kiện)` | | | |

## 7. Observability & Hợp đồng
- Trường log / metric / tracing:
- Sự kiện audit:
- Che dữ liệu PII/secret:
- Vị trí OpenAPI/schema:
- Contract test / mock / sandbox:

## 8. Truy vết & Phê duyệt
| ID Requirement / AC | Endpoint / schema | Test case |
|---|---|---|

| Người review | Vai trò | Quyết định | Ngày |
|---|---|---|---|
| | Chủ API / Tech Lead | | |
| | Reviewer bảo mật (nếu cần) | | |
