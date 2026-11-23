---
name: microservices
description: "Đánh giá hoặc thiết kế ranh giới service."
---

# microservices

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Chỉ tách khi có nhu cầu triển khai hoặc mở rộng độc lập; định nghĩa owner dữ liệu, contract và timeout; thiết kế retry có giới hạn và idempotency.
3. Thử downstream lỗi; bàn giao contract, quan sát và phương án tương thích trong rollout.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
