# Quy ước phiên bản (Versioning Conventions)

## 1. Mục đích

Tài liệu này định nghĩa quy tắc versioning cho các thành phần của framework, artifact của dự án, template, cấu hình và các tài nguyên được quản lý khác.

Mục tiêu:

- Theo dõi thay đổi theo thời gian.
- Xác định chính xác phiên bản được dùng để review và phê duyệt.
- Duy trì khả năng tương thích giữa framework và các dự án.
- Hỗ trợ kiểm toán và khôi phục (rollback).
- Phân biệt thay đổi lớn với cập nhật nhỏ.

## 2. Nguyên tắc versioning

1. Mọi artifact được quản lý phiên bản PHẢI có phiên bản được xác định rõ ràng.
2. Lịch sử phiên bản PHẢI có thể truy vết.
3. Các phiên bản đã được phê duyệt PHẢI được giữ nguyên.
4. Mọi thay đổi đáng kể đối với artifact đã được phê duyệt PHẢI kích hoạt review phù hợp.
5. Số phiên bản KHÔNG ĐƯỢC thay thế ID của artifact.
6. Quy tắc versioning PHẢI nhất quán trong từng nhóm artifact.

## 3. Định dạng phiên bản

Dùng Semantic Versioning cho các bản phát hành framework và thành phần tái sử dụng:

`MAJOR.MINOR.PATCH`

| Thành phần | Ý nghĩa |
|---|---|
| MAJOR | Thay đổi không tương thích hoặc gây lỗi ngược (breaking change). |
| MINOR | Bổ sung chức năng hoặc tiêu chuẩn tương thích ngược. |
| PATCH | Sửa lỗi và làm rõ nội dung tương thích ngược. |

Ví dụ:

- `1.0.0`
- `1.1.0`
- `1.1.1`
- `2.0.0`

Phiên bản pre-release có thể dùng:

- `1.0.0-alpha.1`
- `1.0.0-beta.1`
- `1.0.0-rc.1`

## 4. Versioning của framework

AI-Driven SDLC Framework tổng thể PHẢI có một phiên bản rõ ràng.

Ví dụ:

- `framework-version: 1.0.0`
- `framework-version: 1.1.0`

Quy tắc tăng phiên bản:

- MAJOR: Thay đổi không tương thích về cấu trúc framework, chính sách bắt buộc hoặc giao diện.
- MINOR: Bổ sung giai đoạn, tiêu chuẩn, template hoặc năng lực mới tương thích ngược.
- PATCH: Sửa lỗi, làm rõ nội dung và cải tiến không gây lỗi ngược.

Mỗi dự án PHẢI ghi nhận phiên bản framework mà dự án đang sử dụng.

## 5. Versioning của artifact

Artifact chính thức của dự án NÊN dùng số phiên bản tăng dần.

Định dạng khuyến nghị:

`vMAJOR.MINOR`

Ví dụ:

- `v1.0`
- `v1.1`
- `v2.0`

Quy tắc tăng phiên bản:

- MAJOR: Thay đổi đáng kể về phạm vi, yêu cầu, kiến trúc hoặc ý nghĩa.
- MINOR: Làm rõ, tinh chỉnh và thay đổi không gây lỗi ngược.

Phiên bản PHẢI được lưu trong metadata của artifact, KHÔNG chỉ được mã hóa làm định danh duy nhất.

Ví dụ:

| Trường | Giá trị |
|---|---|
| ID | BR-0001 |
| Title | Customer Registration |
| Version | v1.2 |
| Status | Approved |

## 6. Versioning template và tài nguyên dùng chung

Template tái sử dụng, rules, skills của AI và cấu hình dùng chung NÊN tuân theo chính sách versioning của package sở hữu chúng.

Khi một template dùng chung thay đổi:

- Ghi nhận thay đổi trong lịch sử phiên bản.
- Xác định thay đổi có gây lỗi ngược hay không.
- Thông báo cho các dự án bị ảnh hưởng khi cần.
- Lưu thông tin tương thích khi áp dụng được.

Dự án NÊN ghi nhận phiên bản của các tài nguyên dùng chung mà mình sử dụng khi cần tính tái lập (reproducibility).

## 7. Quan hệ giữa phiên bản và phê duyệt

Phê duyệt áp dụng cho một phiên bản cụ thể của artifact.

Ví dụ:

- `BR-0001 v1.0` có thể ở trạng thái Approved.
- `BR-0001 v1.1` có thể đang ở trạng thái Draft hoặc In Review.

Việc phê duyệt phiên bản cũ KHÔNG tự động phê duyệt phiên bản mới hơn.

Bản ghi phê duyệt PHẢI tham chiếu đến:

- ID của artifact
- Phiên bản của artifact
- Người review
- Quyết định phê duyệt
- Thời điểm phê duyệt
- Human Review Gate liên quan, nếu có

## 8. Lịch sử thay đổi

Mọi artifact chính thức NÊN duy trì lịch sử thay đổi.

Các trường khuyến nghị:

| Trường | Mô tả |
|---|---|
| Version | Phiên bản của artifact. |
| Date | Ngày thay đổi. |
| Author | Người hoặc AI Agent thực hiện thay đổi. |
| Change Summary | Mô tả nội dung thay đổi. |
| Change Reference | ID của yêu cầu thay đổi hoặc quyết định liên quan. |
| Review Reference | Bản ghi review hoặc phê duyệt liên quan, nếu có. |

Ví dụ:

| Version | Date | Author | Change Summary | Reference |
|---|---|---|---|---|
| v1.0 | 2026-01-10 | BA | Phiên bản khởi tạo | CHG-0001 |
| v1.1 | 2026-01-15 | BA | Cập nhật tiêu chí nghiệm thu | CHG-0002 |

## 9. Trách nhiệm của AI

AI Agent PHẢI:

- Giữ nguyên ID hiện có của artifact.
- Cập nhật phiên bản artifact theo đúng quy tắc đã định nghĩa.
- Ghi nhận các thay đổi có ý nghĩa.
- Tránh sửa đổi phiên bản đã được phê duyệt một cách âm thầm.
- Tham chiếu đến yêu cầu thay đổi liên quan.
- Phân biệt phiên bản nháp với phiên bản đã phê duyệt.
- KHÔNG BAO GIỜ khẳng định một phiên bản đã được phê duyệt khi không có bản ghi phê duyệt hợp lệ từ con người.

## 10. Kiểm tra (Validation)

Công cụ kiểm tra tự động NÊN kiểm tra:

- Định dạng phiên bản.
- Lịch sử phiên bản đầy đủ.
- Tăng phiên bản đúng quy tắc.
- Tính nhất quán giữa phê duyệt và phiên bản.
- Tương thích với phiên bản framework.
- Tham chiếu đến các phiên bản đã bị thay thế.
