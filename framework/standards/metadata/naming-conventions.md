# Quy ước đặt tên (Naming Conventions)

## 1. Mục đích

Tài liệu này định nghĩa quy ước đặt tên cho thư mục, file, tài liệu và các artifact có tên khác trong AI-Driven SDLC Framework.

Mục tiêu:

- Đảm bảo tên gọi nhất quán giữa các dự án.
- Cải thiện khả năng đọc và tìm kiếm.
- Đơn giản hóa việc xử lý tự động.
- Tránh tên gọi mơ hồ hoặc xung đột.
- Hỗ trợ tương thích đa nền tảng.

## 2. Nguyên tắc đặt tên chung

Mọi tên gọi PHẢI tuân theo các nguyên tắc sau:

1. Dùng tên mô tả rõ ràng và có ý nghĩa.
2. Ưu tiên chữ thường cho thư mục và tên file.
3. Dùng kebab-case cho thư mục và file Markdown.
4. Tránh dấu cách và ký tự đặc biệt trong tên file.
5. Tránh viết tắt mơ hồ trừ khi đã được chuẩn hóa.
6. Giữ tên file ngắn gọn nhưng đủ dễ hiểu.
7. Sử dụng thuật ngữ nhất quán trong toàn bộ framework.
8. Không đưa thông tin có thể thay đổi như trạng thái hoặc người phụ trách vào tên file.

## 3. Đặt tên thư mục

Dùng lowercase kebab-case.

Ví dụ:

- `requirement-analysis/`
- `system-design/`
- `task-planning/`
- `human-review-gates/`
- `coding-guidelines/`

Tránh:

- `RequirementAnalysis/`
- `requirement_analysis/`
- `Requirement Analysis/`

## 4. Đặt tên file

### 4.1 File Markdown

Dùng lowercase kebab-case với phần mở rộng `.md`.

Ví dụ:

- `business-requirement.md`
- `user-story.md`
- `acceptance-criteria.md`
- `requirement-traceability.md`
- `human-review.md`

### 4.2 File cấu hình

Dùng tên viết thường, mô tả rõ ràng và theo định dạng mà công cụ liên quan yêu cầu.

Ví dụ:

- `framework-config.yaml`
- `autonomy-config.yaml`
- `model-routing.yaml`
- `project-context.yaml`

### 4.3 Script

Dùng lowercase kebab-case hoặc quy ước đặt tên của ngôn ngữ lập trình được sử dụng.

Ví dụ:

- `init-project.py`
- `validate-project.py`
- `sync-framework.py`

## 5. Đặt tên artifact

Artifact chính thức NÊN dùng ID đã được gán trong tên file khi thực tế cho phép.

Định dạng khuyến nghị:

`{ARTIFACT-ID}-{mô-tả-ngắn}.{phần-mở-rộng}`

Ví dụ:

- `BR-0001-customer-registration.md`
- `US-0001-create-customer.md`
- `AC-0001-validate-customer-email.md`
- `TASK-0001-implement-customer-api.md`
- `TC-0001-create-customer-successfully.md`

ID là định danh chính. Phần mô tả phục vụ việc đọc hiểu và CÓ THỂ thay đổi khi tiêu đề thay đổi.

Khi một tài liệu chứa nhiều artifact, dùng ID ở cấp tài liệu hoặc tên file mô tả theo chính sách của template liên quan.

## 6. Đặt tên template

File template NÊN mô tả loại artifact, KHÔNG chứa ID của một instance cụ thể.

Ví dụ:

- `business-requirement.md`
- `user-story.md`
- `acceptance-criteria.md`
- `test-case.md`

Template KHÔNG ĐƯỢC nhầm lẫn với artifact thực tế của dự án.

## 7. Đặt tên tài nguyên AI

Dùng tên nhất quán cho rules, skills và agents của AI.

Ví dụ:

- `rules/core/`
- `skills/solution-architecture/`
- `agents/code-reviewer/`

Tên gọi NÊN mô tả năng lực hoặc trách nhiệm, KHÔNG mô tả nhà cung cấp model.

## 8. Đặt tên cho phiên bản và tài liệu lịch sử

KHÔNG tạo nhiều file đang hoạt động chỉ khác nhau ở các hậu tố như:

- `final.md`
- `final-v2.md`
- `final-latest.md`
- `final-updated.md`

Hãy dùng metadata phiên bản và lịch sử thay đổi thay thế.

Bản snapshot lịch sử CÓ THỂ chứa phiên bản hoặc ngày khi chính sách lưu trữ của dự án yêu cầu.

## 9. Các mẫu đặt tên bị cấm

Tránh:

- Dấu cách trong tên file.
- Ký tự đặc biệt không cần thiết.
- Tên mơ hồ như `misc.md`, `temp.md` hoặc `new-file.md` cho artifact chính thức.
- Tên dựa trên cá nhân thành viên trong nhóm.
- Nhãn trạng thái trong tên file, ví dụ `approved-user-story.md`.
- Nhãn phiên bản có thể thay đổi như `latest` hoặc `final` làm định danh phiên bản duy nhất.

## 10. Kiểm tra (Validation)

Công cụ kiểm tra tự động NÊN kiểm tra:

- Định dạng tên thư mục.
- Định dạng tên file.
- Phần mở rộng file bắt buộc.
- Tên artifact bị trùng lặp ở nơi yêu cầu tính duy nhất.
- Sự có mặt của ID artifact trong tên file khi áp dụng.
- Các mẫu đặt tên bị cấm.
