---
name: terraform
description: "Thay đổi hạ tầng bằng Terraform."
---

# terraform

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Khóa version, review backend/state và plan; kiểm tra tài nguyên bị replace và dữ liệu nhạy cảm trong state.
3. Chạy fmt/validate, review plan; không apply khi chưa có phê duyệt.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
