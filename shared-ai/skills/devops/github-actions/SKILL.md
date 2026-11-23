---
name: github-actions
description: "Xây dựng workflow CI GitHub Actions."
---

# github-actions

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Cấp quyền tối thiểu, pin action bên ngoài theo SHA đáng tin, không đánh giá input không tin cậy trong shell và không cấp secret cho job PR không tin cậy.
3. Xác minh YAML và chạy CI không triển khai; gate cho environment release.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
