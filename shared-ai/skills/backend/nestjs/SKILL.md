---
name: nestjs
description: "Thiết kế, triển khai và review module NestJS, gồm DTO, DI, lỗi, xác thực và kiểm thử."
---

# NestJS

1. Đọc package manifest, phiên bản Nest, thiết lập validation, module hiện có và lệnh test. Theo convention dự án trước khi áp dụng mẫu.
2. Dùng controller cho HTTP, service cho use case và repository/adapter cho I/O nếu dự án có lớp này. Chỉ export provider cần chia sẻ.
3. DTO/validation: tách DTO khỏi entity, kiểm tra input tại biên và loại hoặc từ chối field thừa theo policy dự án.
4. Xác minh quyền theo tài nguyên và xử lý lỗi tại biên. Không đưa secret hoặc dữ liệu persistence nhạy cảm vào response.
5. Kiểm thử service và HTTP contract; ghi phiên bản, lệnh đã chạy và điều chưa xác minh.

## Tài nguyên

- [Cấu trúc](references/project-structure.md), [module](references/module-design.md), [các lớp](references/controller-service-repository.md), [DI](references/dependency-injection.md)
- [DTO và validation](references/dto-validation.md), [xác thực](references/authentication.md), [xử lý lỗi](references/exception-handling.md), [kiểm thử](references/testing.md)
- [Ví dụ module](examples/module-example.md), [ví dụ Jest](examples/testing-example.md)
- [Mẫu module](templates/module-template/README.md), [mẫu service](templates/service-template/README.md)
- Kiểm tra cấu trúc tối thiểu: `bash scripts/validate-structure.sh /path/to/project`. Script không thay cho type check hoặc test.
