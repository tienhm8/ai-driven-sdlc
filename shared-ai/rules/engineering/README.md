# Rules: engineering

- Ưu tiên thay đổi nhỏ, tương thích; không chỉnh ngoài phạm vi. Kiểm tra chuẩn hiện hành tại [Standards](../../../framework/standards/README.md).
- Kiểm tra dữ liệu ở biên, quyền ở máy chủ, lỗi không lộ dữ liệu, và rollback cho thay đổi liên quan trạng thái.
- Thêm kiểm thử cho hành vi đổi, kể cả trường hợp lỗi; chạy lệnh dự án và ghi chính xác bài kiểm tra bị bỏ qua.
