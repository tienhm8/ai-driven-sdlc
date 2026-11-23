---
name: authorization
description: "Thiết kế hoặc review phân quyền phòng thủ."
---

# authorization

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Deny mặc định; kiểm tra action, chủ sở hữu và tenant trên server ở từng tài nguyên; lọc danh sách theo scope.
3. Fixture có hai tenant, kiểm tra từ chối chéo và cấp đúng quyền tối thiểu.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
