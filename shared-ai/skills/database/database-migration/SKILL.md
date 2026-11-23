---
name: database-migration
description: "Thay đổi schema hoặc backfill an toàn."
---

# database-migration

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Thiết kế expand → backfill lặp lại được → chuyển traffic → contract ở release sau; ước lượng lock và đặt điều kiện dừng.
3. Thử trên môi trường cô lập, xác nhận ứng dụng cũ/mới và kế hoạch phục hồi.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
