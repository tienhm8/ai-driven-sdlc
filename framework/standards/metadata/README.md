# Tiêu chuẩn metadata (Metadata Standards)

## 1. Mục đích

Thư mục này định nghĩa các tiêu chuẩn metadata chung được sử dụng xuyên suốt AI-Driven SDLC Framework.

Các tiêu chuẩn này đảm bảo tính nhất quán, khả năng truy vết, khả năng tìm kiếm và khả năng kiểm tra tự động đối với artifact của dự án trong suốt vòng đời phát triển phần mềm.

Tiêu chuẩn áp dụng cho:

- Artifact phân tích yêu cầu và nghiệp vụ.
- Tài liệu kiến trúc và thiết kế hệ thống.
- Artifact lập kế hoạch và quản lý task.
- Mã nguồn và artifact phát triển.
- Bản ghi code review.
- Artifact kiểm thử và QA.
- Artifact triển khai và release.
- Bản ghi giám sát và bảo trì.
- Artifact do AI tạo ra và output của agent.
- Tài liệu quản lý dự án.

## 2. Danh sách tiêu chuẩn

| Tiêu chuẩn | Mô tả |
|---|---|
| `id-conventions.md` | Định nghĩa định dạng ID, prefix, tính duy nhất và quan hệ giữa các artifact. |
| `status-conventions.md` | Định nghĩa trạng thái vòng đời chung của artifact và work item. |
| `naming-conventions.md` | Định nghĩa quy tắc đặt tên cho file, folder, tài liệu và định danh. |
| `versioning-conventions.md` | Định nghĩa quy tắc versioning và lịch sử thay đổi. |

## 3. Nguyên tắc cốt lõi

Mọi tiêu chuẩn metadata PHẢI tuân theo các nguyên tắc sau:

1. **Nhất quán (Consistency)**: Dùng cùng một quy ước xuyên suốt mọi giai đoạn SDLC.
2. **Khả năng truy vết (Traceability)**: Mọi artifact liên quan PHẢI có thể nhận diện và truy vết.
3. **Tính duy nhất (Uniqueness)**: ID KHÔNG ĐƯỢC trùng lặp trong phạm vi đã định nghĩa của dự án.
4. **Bất biến (Immutability)**: Sau khi đã gán, ID KHÔNG ĐƯỢC tái sử dụng cho artifact khác.
5. **Khả năng kiểm toán (Auditability)**: Các thay đổi metadata quan trọng PHẢI có thể truy vết.
6. **Thân thiện với tự động hóa (Automation-friendly)**: Định dạng metadata NÊN hỗ trợ kiểm tra tự động.
7. **Độc lập công cụ (Tool independence)**: Tiêu chuẩn KHÔNG ĐƯỢC phụ thuộc vào một công cụ AI hoặc nền tảng quản lý dự án cụ thể.

## 4. Phạm vi và thứ tự ưu tiên

Các tiêu chuẩn này được định nghĩa tập trung tại framework.

Dự án CÓ THỂ mở rộng tiêu chuẩn thông qua cấu hình riêng của dự án, nhưng KHÔNG ĐƯỢC âm thầm ghi đè các quy tắc bắt buộc của framework.

Nếu quy ước riêng của dự án mâu thuẫn với quy ước bắt buộc của framework, quy ước của framework có thứ tự ưu tiên, trừ khi có ngoại lệ được ủy quyền và ghi nhận.

## 5. Tiêu chuẩn liên quan

- `../documentation/`: Tiêu chuẩn tài liệu.
- `../../governance/autonomy-levels/`: Chính sách mức độ tự chủ của AI.
- `../../governance/human-review-gates/`: Chính sách review và phê duyệt của con người.
- `../../project-management/`: Template và bản ghi quản lý dự án.

## 6. Tuân thủ

Mọi artifact áp dụng của dự án NÊN tuân thủ các tiêu chuẩn metadata này.

Nên triển khai kiểm tra tự động khi khả thi, bao gồm:

- Các trường metadata bắt buộc.
- Định dạng ID và tính duy nhất.
- Quy ước đặt tên.
- Các giá trị status được phép.
- Định dạng version.
- Tham chiếu truy vết.

Artifact không tuân thủ PHẢI được báo cáo và sửa theo quy trình governance của dự án.
