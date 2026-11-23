---
name: redis
description: "Dùng Redis cho cache hoặc dữ liệu ngắn hạn."
---

# redis

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Đặt TTL, giới hạn dung lượng và chính sách eviction; xác định cache invalidation và hành vi khi Redis lỗi.
3. Kiểm tra expiry, cache miss, phục hồi và không coi cache là nguồn chuẩn nếu chưa có thiết kế durability.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
