---
name: clean-architecture
description: "Tách logic nghiệp vụ khỏi infrastructure."
---

# clean-architecture

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Giữ dependency hướng vào trong; định nghĩa port tại phía use case, adapter tại biên, wiring ở composition root.
3. Kiểm thử use case không cần framework và kiểm tra import không đảo chiều.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
