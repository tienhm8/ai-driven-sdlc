---
name: dotnet
description: "Phát triển backend ASP.NET Core."
---

# dotnet

## Cách thực hiện

1. Đọc task, stack, conventions và phạm vi đã duyệt trước khi làm.
2. Đọc target framework; dùng DI lifetime đúng, không giữ scoped dependency trong singleton; truyền CancellationToken xuống I/O.
3. Kiểm tra middleware lỗi, cấu hình và integration test qua host thử nghiệm.

## Bàn giao

Nêu quyết định, bằng chứng đã kiểm tra và điểm chưa xác minh; chuyển mục cần phê duyệt cho người phụ trách.
