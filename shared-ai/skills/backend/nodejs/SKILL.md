---
name: nodejs
description: "Phát triển dịch vụ Node.js."
---

# nodejs

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Giữ runtime theo repo; không chặn event loop với I/O đồng bộ; đặt timeout/cancellation ở I/O, dọn kết nối khi shutdown.
3. Chạy lệnh dự án; kiểm tra lỗi async, shutdown và dữ liệu sai.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
