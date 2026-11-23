# Tiêu chuẩn kiểm thử phần mềm (Software Testing Standards)

## 1. Mục đích

Định nghĩa các tiêu chuẩn chung cho việc lập kế hoạch, thiết kế, triển khai, thực thi và báo cáo kiểm thử phần mềm.

## 2. Nguyên tắc kiểm thử

Hoạt động kiểm thử PHẢI:

- Bám sát các yêu cầu đã được phê duyệt.
- Kiểm chứng cả hành vi mong đợi và hành vi không mong đợi.
- Bao phủ các kịch bản nghiệp vụ quan trọng.
- Phát hiện lỗi sớm nhất có thể.
- Có khả năng lặp lại khi thực tế cho phép.
- Cung cấp bằng chứng có thể truy vết.
- Xem xét rủi ro về bảo mật, hiệu năng và độ tin cậy.

Kiểm thử là trách nhiệm chung của lập trình viên, QA engineer và các bên liên quan.

## 3. Các cấp độ kiểm thử

Dự án NÊN áp dụng kết hợp phù hợp các cấp độ sau:

| Cấp độ | Mục đích |
|---|---|
| Unit Testing | Kiểm chứng từng hàm, class hoặc component riêng lẻ |
| Integration Testing | Kiểm chứng tương tác giữa các component hoặc service |
| API Testing | Kiểm chứng contract và hành vi của API |
| System Testing | Kiểm chứng hệ thống đã được tích hợp |
| End-to-End Testing | Kiểm chứng toàn bộ luồng nghiệp vụ |
| Acceptance Testing | Xác nhận yêu cầu nghiệp vụ đã được đáp ứng |
| Regression Testing | Phát hiện tác động ngoài ý muốn từ thay đổi |

Chiến lược kiểm thử được chọn PHẢI phản ánh độ phức tạp và mức rủi ro của dự án.

## 4. Thiết kế test

Test case NÊN bao phủ:

- Kịch bản dương tính (positive).
- Kịch bản âm tính (negative).
- Điều kiện biên.
- Dữ liệu đầu vào không hợp lệ.
- Dữ liệu thiếu hoặc không bắt buộc.
- Vi phạm quy tắc nghiệp vụ.
- Phân quyền và kiểm soát truy cập.
- Xử lý lỗi.
- Các thao tác đồng thời khi có liên quan.
- Hành vi nhạy cảm về hiệu năng.

Test case PHẢI có khả năng truy vết đến yêu cầu hoặc mục tiêu kiểm thử đã được phê duyệt khác.

## 5. Đặt tên và tổ chức test

Tên test PHẢI thể hiện rõ hành vi đang được kiểm chứng.

Cấu trúc khuyến nghị:

```text
[Unit/Component]_[Scenario]_[ExpectedResult]
```

Ví dụ:

```text
CreateCustomer_WithValidData_ReturnsCreatedCustomer
CreateCustomer_WithDuplicateEmail_ReturnsConflict
GetCustomer_WithUnknownId_ReturnsNotFound
```

Dự án CÓ THỂ áp dụng quy ước khác nếu được sử dụng nhất quán.

## 6. Quản lý dữ liệu test

Dữ liệu test PHẢI được kiểm soát và có thể tái tạo.

Dữ liệu test NÊN:

- Được tách biệt khỏi dữ liệu production.
- Sử dụng thông tin tổng hợp (synthetic) hoặc đã ẩn danh khi có thể.
- Bao phủ các kịch bản nghiệp vụ liên quan.
- Không làm lộ thông tin cá nhân hoặc thông tin mật.
- Được dọn dẹp khi cần thiết.

Test KHÔNG ĐƯỢC sửa đổi dữ liệu production trừ khi được ủy quyền rõ ràng thông qua quy trình có kiểm soát.

## 7. Độ cô lập và độ tin cậy của test

Test tự động NÊN:

- Có kết quả xác định (deterministic).
- Tránh phụ thuộc không cần thiết vào thứ tự thực thi.
- Dọn dẹp dữ liệu tạm.
- Sử dụng mock hoặc stub một cách phù hợp.
- Tránh chia sẻ trạng thái có thể thay đổi một cách vô ý.
- Có thể chạy trong môi trường CI/CD đã định.

Flaky test PHẢI được điều tra và theo dõi.

## 8. Độ bao phủ test (Test Coverage)

Dự án NÊN định nghĩa mục tiêu độ bao phủ dựa trên rủi ro và mức độ quan trọng của ứng dụng.

Các chỉ số bao phủ có thể bao gồm:

- Line coverage.
- Branch coverage.
- Function hoặc method coverage.
- Requirement coverage.

Tỷ lệ phần trăm bao phủ KHÔNG ĐƯỢC coi là thước đo chất lượng test duy nhất.

Các quy tắc nghiệp vụ quan trọng và hành vi nhạy cảm về bảo mật NÊN được kiểm thử kỹ hơn.

## 9. Kiểm thử API và tích hợp

Test API và test tích hợp NÊN kiểm chứng:

- Contract của request và response.
- Xác thực.
- Phân quyền.
- Kiểm tra dữ liệu đầu vào.
- Response lỗi.
- Lưu trữ dữ liệu.
- Tương tác giữa các service.
- Hành vi khi timeout và khi lỗi.

Contract testing NÊN được cân nhắc đối với các service được phát triển độc lập.

## 10. Kiểm thử phi chức năng

Tùy theo yêu cầu của dự án, kiểm thử phi chức năng CÓ THỂ bao gồm:

- Performance testing.
- Load testing.
- Stress testing.
- Security testing.
- Accessibility testing.
- Compatibility testing.
- Reliability testing.
- Resilience testing.
- Recovery testing.

Các tiêu chí nghiệm thu phi chức năng áp dụng PHẢI có thể đo lường được.

## 11. Kiểm thử hồi quy (Regression Testing)

Mọi thay đổi PHẢI được đánh giá rủi ro hồi quy.

Kiểm thử hồi quy NÊN ưu tiên:

- Các tính năng bị ảnh hưởng.
- Các module phụ thuộc.
- Các component dùng chung.
- Các luồng nghiệp vụ quan trọng.
- Các khu vực nhạy cảm về bảo mật.
- Các lỗi đã được báo cáo trước đó.

## 12. Quản lý lỗi (Defect Management)

Lỗi PHẢI được ghi nhận với đủ thông tin để tái hiện và điều tra.

Bản ghi lỗi NÊN chứa:

- Mã lỗi (Defect ID).
- Tóm tắt.
- Môi trường.
- Điều kiện tiên quyết.
- Các bước tái hiện.
- Kết quả mong đợi.
- Kết quả thực tế.
- Mức độ nghiêm trọng (severity).
- Mức độ ưu tiên (priority).
- Bằng chứng.
- Yêu cầu hoặc test case liên quan.
- Trạng thái hiện tại.

Phải phân biệt severity và priority:

- Severity thể hiện mức độ tác động.
- Priority thể hiện mức độ khẩn cấp cần xử lý.

## 13. Bằng chứng thực thi test

Quá trình thực thi test NÊN lưu giữ bằng chứng như:

- Kết quả test.
- Log.
- Ảnh chụp màn hình.
- Báo cáo.
- Tham chiếu đến build hoặc bản triển khai.
- Thông tin môi trường.

Bằng chứng KHÔNG ĐƯỢC làm lộ secret hoặc dữ liệu nhạy cảm.

## 14. Kiểm thử trong CI/CD

Test tự động NÊN được tích hợp vào pipeline CI/CD.

Dự án PHẢI xác định những test nào bắt buộc phải pass trước khi:

- Merge code.
- Tạo release candidate.
- Triển khai lên production.

Khi test quan trọng thất bại và quality gate của dự án yêu cầu, quy trình PHẢI bị chặn lại.

## 15. Quy tắc kiểm thử cho AI

AI testing agent PHẢI:

- Suy ra test từ yêu cầu và tiêu chí nghiệm thu đã được phê duyệt.
- Bao gồm các kịch bản âm tính và điều kiện biên.
- Tránh chỉ kiểm thử hành vi hiện tại của triển khai.
- Nhận diện phần thiếu độ bao phủ test.
- Báo cáo chính xác kết quả thực thi.
- Phân biệt test đã được sinh ra với test đã được thực thi.
- Nhận diện flaky test hoặc test không đáng tin cậy.
- Duy trì khả năng truy vết giữa yêu cầu và test.

AI KHÔNG ĐƯỢC tự ý đánh dấu test thất bại thành đạt hoặc bỏ qua quality gate bắt buộc.

## 16. Tiêu chí kết thúc (Exit Criteria)

Mỗi giai đoạn kiểm thử NÊN định nghĩa tiêu chí kết thúc rõ ràng, bao gồm:

- Các bộ test bắt buộc đã hoàn thành.
- Lỗi nghiêm trọng đã được xử lý hoặc được chấp nhận chính thức.
- Các test bắt buộc đã pass.
- Đạt các ngưỡng độ bao phủ hoặc chất lượng yêu cầu.
- Bằng chứng test đã được ghi nhận.
- Các rủi ro còn lại đã được tài liệu hóa.
- Đã có phê duyệt QA cần thiết.

## 17. Tài liệu tham chiếu

- `coding-standards.md`
- `../architecture/api-standards.md`
- `../security/security-standards.md`
- `../documentation/documentation-standards.md`
