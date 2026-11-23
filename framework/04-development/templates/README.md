# Development Templates

`templates/` chứa các mẫu tài liệu dùng chung cho công việc viết code trong giai đoạn 04 Development. Mẫu quyết định cách AI cấu trúc công việc và cách trình bày kết quả trung gian.

## Kiến trúc

```text
templates/
├── development-task.md        # Mô tả task đã được chuẩn bị để code
├── implementation-plan.md     # Kế hoạch triển khai trước khi sửa code
└── code-documentation.md      # Tài liệu cho module/component/API
```

Luồng sử dụng: `development-task` → `implementation-plan` → code và test → `code-documentation` (nếu có thay đổi về interface, behavior hoặc vận hành). Kết quả cuối cùng được ghi vào `outputs/` theo các template ở đó.

## Vai trò từng file

| File | Vai trò | Khi nào dùng | Ai điền |
|---|---|---|---|
| `development-task.md` | Chuyển task đã duyệt ở G3 thành đơn vị công việc có metadata, tham chiếu G1/G2/G3, AC, ràng buộc kỹ thuật, DoD và phần AI hỗ trợ. | Khi bắt đầu một task | Developer, với sự hỗ trợ của AI |
| `implementation-plan.md` | Trình bày cách tiếp cận, phân rã bước, kế hoạch test, đánh giá tác động, rủi ro và ranh giới thực thi của AI. Được Developer (và Tech Lead nếu cần) review trước khi code. | Sau khi nhận task, trước khi sửa code | AI soạn; Developer review |
| `code-documentation.md` | Tài liệu cho module/component/API: mục đích, public interface, hành vi, cấu hình (không có giá trị secret), vận hành, lịch sử thay đổi. | Khi thêm mới hoặc thay đổi interface/behavior | Developer, AI hỗ trợ |

## Quy tắc sử dụng

- Điền các trường bắt buộc; mục không áp dụng ghi N/A kèm lý do.
- `code-documentation.md` không cần lập cho mọi function nếu code và docstring đã đủ rõ theo chuẩn dự án.
- Không ghi giá trị secret thực tế trong bất kỳ mẫu nào.
- Mẫu test evidence, implementation summary và handover nằm trong `outputs/`, không nằm ở đây.
