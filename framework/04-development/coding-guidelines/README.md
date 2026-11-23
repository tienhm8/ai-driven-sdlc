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

Quan hệ giữa các file:

- `general-guidelines.md` là nền tảng. Ba file còn lại là chuyên đề, bổ sung chi tiết cho các khía cạnh cụ thể.
- Khi có xung đột, thứ tự ưu tiên được quy định trong `general-guidelines.md`: security/governance trước, sau đó kiến trúc đã duyệt và quy định của project, rồi đến coding standard của framework. Xung đột phải escalate lên Tech Lead, không tự chọn.

## Vai trò từng file

| File | Vai trò | Nội dung chính |
|---|---|---|
| `general-guidelines.md` | Quy tắc nền cho mọi code | Thứ tự ưu tiên; ranh giới module; đặt tên, validate, xử lý edge case; test; hiệu năng; quy tắc riêng cho code do AI sinh ra |
| `error-handling.md` | Cách xử lý và trả về lỗi | Phân loại lỗi (validation, domain, auth, dependency, unexpected); không nuốt exception; retry có giới hạn và idempotency; format lỗi API |
| `logging-guidelines.md` | Cách ghi log | Structured log và correlation ID; bảng mức TRACE–FATAL; cấm log dữ liệu nhạy cảm; chống log injection; retention |
| `secure-coding.md` | Yêu cầu bảo mật khi viết code | Authorization phía server; chống injection; quản lý secret; dependency; giới hạn AI không tự đổi authz/crypto; yêu cầu quét SAST và secret |

## Quan hệ với các thành phần khác

- Yêu cầu trong các file này được kiểm tra qua `checklists/implementation-dod.md` và `checklists/ai-safety-checklist.md`.
- Tiêu chuẩn bảo mật và coding cấp framework nằm trong `framework/standards/` và `framework/governance/`; các file này có ưu tiên cao hơn tài liệu tại đây.

## Quy tắc sử dụng

- Đọc `general-guidelines.md` trước, sau đó đọc chuyên đề liên quan đến thay đổi đang thực hiện.
- Đây là chuẩn tối thiểu. Project có thể quy định chặt hơn nhưng không được nới lỏng.
