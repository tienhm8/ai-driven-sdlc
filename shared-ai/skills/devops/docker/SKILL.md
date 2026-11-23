---
name: docker
description: "Đóng gói ứng dụng bằng Docker."
---

# docker

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Dùng multi-stage, base image đã kiểm chứng, user không phải root và .dockerignore; không đưa secret vào build layer.
3. Build và smoke test cục bộ; kiểm tra startup/shutdown và kích thước image.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
