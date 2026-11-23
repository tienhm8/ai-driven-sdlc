# Tiêu chuẩn mã nguồn (Coding Standards)

## 1. Mục đích

Định nghĩa các thực hành lập trình chung nhằm đảm bảo mã nguồn dễ đọc, dễ bảo trì, an toàn, dễ kiểm thử và nhất quán giữa các dự án.

## 2. Nguyên tắc cốt lõi

Mọi mã nguồn PHẢI tuân theo các nguyên tắc sau:

- Ưu tiên khả năng đọc hiểu hơn sự "khéo léo" không cần thiết.
- Ưu tiên sự đơn giản hơn độ phức tạp không cần thiết.
- Tái sử dụng khi phù hợp.
- Tách biệt các mối quan tâm (separation of concerns).
- Tính gắn kết cao (high cohesion) và ghép nối thấp (low coupling).
- Hành vi tường minh và thực thi có thể dự đoán.
- Triển khai an toàn.
- Dễ kiểm thử và dễ bảo trì.

## 3. Quy ước đặt tên

Tên PHẢI thể hiện rõ ý định.

Lập trình viên PHẢI tuân theo quy ước đặt tên của ngôn ngữ lập trình và framework đã chọn.

Hướng dẫn chung:

| Thành phần | Khuyến nghị |
|---|---|
| Biến | Danh từ có ý nghĩa |
| Hàm | Tên mô tả hành động |
| Class | Danh từ theo domain hoặc trách nhiệm |
| Hằng số | Đặt tên theo quy ước hằng số của ngôn ngữ |
| Biến boolean | Tên thể hiện ý nghĩa đúng/sai |
| Interface | Vai trò hoặc contract rõ ràng |
| Module | Trách nhiệm rõ ràng |

Cần tránh:

- Viết tắt mơ hồ.
- Tên một ký tự ngoài phạm vi cục bộ ngắn.
- Tên gây hiểu nhầm.
- Tên lộ chi tiết triển khai không cần thiết.

## 4. Cấu trúc mã nguồn

Mã nguồn PHẢI:

- Tuân theo cấu trúc dự án đã được thiết lập.
- Tách logic nghiệp vụ khỏi các mối quan tâm về hạ tầng khi phù hợp.
- Tránh phụ thuộc quá mức giữa các module.
- Giữ trách nhiệm của mỗi thành phần tập trung.
- Tránh phụ thuộc vòng (circular dependency).
- Tái sử dụng các abstraction đã có của dự án khi phù hợp.

Kiến trúc dự án PHẢI định hướng cách tổ chức package, module và component.

## 5. Hàm và phương thức

Hàm và phương thức NÊN:

- Có một trách nhiệm rõ ràng.
- Có kích thước hợp lý.
- Sử dụng tham số có ý nghĩa.
- Tránh số lượng tham số quá nhiều.
- Tránh tác dụng phụ không mong muốn.
- Trả về kết quả có thể dự đoán.
- Xử lý tường minh dữ liệu đầu vào không hợp lệ.

Logic nghiệp vụ phức tạp NÊN được tách thành các phương thức hoặc component có tên phù hợp.

## 6. Xử lý lỗi

Lỗi PHẢI được xử lý tường minh và nhất quán.

Quá trình triển khai PHẢI:

- Phân biệt lỗi nghiệp vụ dự kiến với lỗi kỹ thuật không mong muốn.
- Không nuốt exception một cách âm thầm.
- Cung cấp thông tin chẩn đoán hữu ích.
- Giữ lại ngữ cảnh lỗi khi ném lại (rethrow).
- Không lộ thông tin nội bộ nhạy cảm.
- Sử dụng các mẫu xử lý lỗi nhất quán.

## 7. Logging và khả năng quan sát

Ứng dụng NÊN cung cấp log có cấu trúc khi phù hợp.

Log NÊN bao gồm:

- Timestamp.
- Mức độ nghiêm trọng (severity).
- Service hoặc component.
- Correlation hoặc request identifier.
- Ngữ cảnh sự kiện liên quan.

Log KHÔNG ĐƯỢC chứa mật khẩu, access token, secret hoặc thông tin cá nhân nhạy cảm không cần thiết.

## 8. Quản lý cấu hình

Cấu hình PHẢI được tách khỏi mã nguồn ứng dụng.

Quá trình triển khai PHẢI:

- Tránh hardcode các giá trị phụ thuộc môi trường.
- Sử dụng cơ chế quản lý cấu hình đã được phê duyệt.
- Lưu secret trong hệ thống quản lý secret an toàn.
- Định nghĩa giá trị mặc định an toàn khi phù hợp.
- Kiểm tra các cấu hình quan trọng khi ứng dụng khởi động.

## 9. Quản lý dependency

Dependency PHẢI:

- Được khai báo tường minh.
- Sử dụng nguồn package đã được phê duyệt.
- Được rà soát rủi ro bảo mật.
- Tránh trùng lặp không cần thiết.
- Tuân theo chính sách versioning của dự án.

Lockfile NÊN được commit khi công nghệ hỗ trợ và phù hợp với stack.

Dependency không còn được bảo trì hoặc có lỗ hổng bảo mật NÊN được thay thế hoặc giảm thiểu rủi ro.

## 10. Chất lượng mã nguồn

Mã nguồn PHẢI:

- Tuân theo quy ước của ngôn ngữ và framework.
- Vượt qua static analysis áp dụng được.
- Tránh trùng lặp code rõ ràng.
- Tránh dead code.
- Tránh độ phức tạp không cần thiết.
- Không tắt các kiểm tra chất lượng mà không có lý do chính đáng.

Dự án NÊN sử dụng công cụ tự động cho format, linting và static analysis.

## 11. Yêu cầu bảo mật

Mã nguồn PHẢI tuân theo thực hành lập trình an toàn.

Tối thiểu:

- Kiểm tra dữ liệu đầu vào không đáng tin cậy.
- Thực hiện kiểm tra phân quyền.
- Ngăn chặn lỗ hổng injection.
- Xử lý dữ liệu nhạy cảm một cách an toàn.
- Tránh deserialization không an toàn.
- Tránh thao tác file không an toàn.
- Sử dụng thư viện mật mã an toàn.
- Phòng chống các lỗ hổng ứng dụng phổ biến.

Tham khảo `../security/security-standards.md`.

## 12. Yêu cầu code review

Thay đổi mã nguồn PHẢI được review theo quy trình governance của dự án.

Review NÊN xem xét:

- Tính đúng đắn.
- Logic nghiệp vụ.
- Tuân thủ kiến trúc.
- Bảo mật.
- Hiệu năng.
- Khả năng bảo trì.
- Độ bao phủ test.
- Ảnh hưởng đến tài liệu.

Mã do AI tạo ra PHẢI tuân theo cùng yêu cầu review và chất lượng như mã do con người tạo ra.

## 13. Quy tắc lập trình cho AI

AI coding agent PHẢI:

1. Kiểm tra mã nguồn liên quan hiện có trước khi chỉnh sửa.
2. Tuân theo quy ước hiện có của dự án.
3. Tránh refactor không cần thiết ngoài phạm vi tác vụ.
4. Giữ nguyên hành vi hiện có trừ khi thay đổi là bắt buộc.
5. Tạo test phù hợp.
6. Chạy các kiểm tra format, linting và test có sẵn.
7. Giải thích các quyết định triển khai quan trọng.
8. Báo cáo giả định và các vấn đề chưa được giải quyết.
9. Nhận diện các thay đổi nhạy cảm về bảo mật.
10. Không khẳng định kiểm tra đã pass nếu chưa thực sự chạy.

AI KHÔNG ĐƯỢC:

- Đưa vào dependency chưa được phê duyệt.
- Hardcode secret.
- Tắt test để build pass.
- Bỏ qua lỗi mà không có lý do chính đáng.
- Sửa các file không liên quan một cách không cần thiết.
- Khẳng định đã có review hoặc phê duyệt của con người.

## 14. Definition of Done

Một thay đổi mã nguồn được coi là hoàn thành về mặt kỹ thuật khi các tiêu chí áp dụng được đều thỏa mãn:

- Triển khai đáp ứng yêu cầu đã được phê duyệt.
- Tuân theo tiêu chuẩn lập trình.
- Các test tự động liên quan đều pass.
- Static analysis và linting pass nếu đã được cấu hình.
- Các vấn đề bảo mật đã được xử lý.
- Tài liệu được cập nhật khi cần.
- Code review đã hoàn thành.
- Các phê duyệt bắt buộc đã được thu thập.

## 15. Tài liệu tham chiếu

- `testing-standards.md`
- `../architecture/api-standards.md`
- `../architecture/database-standards.md`
- `../security/security-standards.md`
- `../documentation/documentation-standards.md`
