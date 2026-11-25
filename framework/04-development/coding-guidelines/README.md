# Development Coding Guidelines

`coding-guidelines/` chứa các quy tắc viết code áp dụng cho mọi task trong giai đoạn 04 Development. Tài liệu chung đặt nền tảng; ba tài liệu chuyên đề đi sâu vào error handling, logging và bảo mật.

## Kiến trúc

```text
coding-guidelines/
├── general-guidelines.md    # Nguyên tắc chung: thiết kế, đúng đắn, test, vệ sinh thay đổi
├── error-handling.md        # Phân loại lỗi, retry, timeout, lỗi trả về client
├── logging-guidelines.md    # Structured log, mức độ, dữ liệu nhạy cảm, vận hành
└── secure-coding.md         # Authz, injection, secret, dependency, biện pháp an toàn khi dùng AI
```

## Tài liệu áp dụng

| Hướng dẫn thực hành | Chuẩn liên quan |
|---|---|
| [General guidelines](general-guidelines.md) — triển khai, review diff và kiểm chứng thay đổi do AI hỗ trợ | [Coding standards](../../standards/coding/coding-standards.md), [Testing standards](../../standards/coding/testing-standards.md) |
| [Error handling](error-handling.md) — phân loại lỗi, retry/timeout và lỗi trả về client | [Coding standards](../../standards/coding/coding-standards.md), [API standards](../../standards/architecture/api-standards.md) |
| [Logging guidelines](logging-guidelines.md) — log có cấu trúc, mức log và truy vết | [Coding standards](../../standards/coding/coding-standards.md), [Security standards](../../standards/security/security-standards.md) |
| [Secure coding](secure-coding.md) — hướng dẫn áp dụng kiểm soát bảo mật trong code | [Security standards](../../standards/security/security-standards.md) |

Đối chiếu qua [Implementation DoD](../checklists/implementation-dod.md) và [AI safety checklist](../checklists/ai-safety-checklist.md). Xử lý xung đột theo [thứ tự ưu tiên](general-guidelines.md).

## Quy tắc sử dụng

- Đọc `general-guidelines.md` trước, sau đó đọc chuyên đề liên quan đến thay đổi đang thực hiện.
- Đây là chuẩn tối thiểu. Project có thể quy định chặt hơn nhưng không được nới lỏng.
