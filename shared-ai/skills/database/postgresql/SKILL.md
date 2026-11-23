---
name: postgresql
description: "Thiết kế hoặc tối ưu PostgreSQL."
---

# postgresql

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Đưa invariant vào constraints; đánh giá index theo truy vấn, nợ vacuum và khóa DDL; tách index concurrently khỏi transaction khi cần.
3. So sánh query plan trên staging; kiểm tra contention và migration tương thích.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
