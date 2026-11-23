---
name: authentication
description: "Thiết kế hoặc review xác thực phòng thủ."
---

# authentication

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Dùng thư viện/IdP đã duyệt; xác minh issuer, audience, hạn và thuật toán theo cấu hình; quản lý session và thu hồi theo rủi ro.
3. Kiểm thử token thiếu/hết hạn hoặc sai cấu hình bằng fixture; không ghi token vào log.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
