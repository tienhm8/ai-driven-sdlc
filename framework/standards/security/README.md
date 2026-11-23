# Tiêu chuẩn bảo mật (Security Standards)

## 1. Mục đích

Thư mục này định nghĩa các yêu cầu bảo mật chung cho hệ thống phần mềm và vòng đời phát triển của chúng.

## 2. Phạm vi

Tiêu chuẩn bảo mật áp dụng cho:

- Yêu cầu và kiến trúc.
- Phát triển ứng dụng.
- API và tích hợp.
- Cơ sở dữ liệu và quản lý dữ liệu.
- Hạ tầng và triển khai.
- Giám sát và ứng phó sự cố.
- Mã nguồn và cấu hình do AI tạo ra.

## 3. Tiêu chuẩn chính

`security-standards.md` định nghĩa mức bảo mật nền tảng (security baseline) chung.

Dự án CÓ THỂ mở rộng baseline này dựa trên:

- Rủi ro nghiệp vụ.
- Phân loại dữ liệu.
- Yêu cầu pháp lý.
- Tiêu chuẩn ngành.
- Môi trường triển khai.
- Mô hình mối đe dọa (threat model).

Yêu cầu bảo mật riêng của dự án KHÔNG ĐƯỢC làm suy yếu các yêu cầu bắt buộc của framework nếu chưa có ngoại lệ được phê duyệt.

## 4. Trách nhiệm

Trách nhiệm bảo mật được chia sẻ trong toàn bộ dự án.

Security Lead hoặc người có thẩm quyền bảo mật được chỉ định chịu trách nhiệm về chính sách bảo mật và review rủi ro.

Developer, architect, QA engineer và DevOps engineer chịu trách nhiệm triển khai các biện pháp kiểm soát bảo mật phù hợp.
