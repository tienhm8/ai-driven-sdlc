---
name: kubernetes
description: "Chuẩn bị manifest hoặc rollout Kubernetes."
---

# kubernetes

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Khai báo requests/limits, probes đúng nghĩa, quyền tối thiểu và strategy rollout; kiểm tra namespace và context trước thao tác.
3. Render/dry-run ở môi trường được duyệt; ghi tiêu chí health và rollback.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
