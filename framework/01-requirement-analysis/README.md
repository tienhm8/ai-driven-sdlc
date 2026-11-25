# 01 — Requirement Analysis

## 1. Kiến trúc

Giai đoạn Requirement Analysis tuân theo cấu trúc chung của framework:

| Thành phần | Vai trò |
|---|---|
| `README.md` | Mục tiêu, phạm vi và cấu trúc giai đoạn |
| `workflow.md` | Các bước thực hiện, đầu ra, quality check, G1 và điều kiện bàn giao |
| `ai-instructions.md` | Hướng dẫn AI thực hiện |
| `human-review.md` | Trách nhiệm review của con người |
| `inputs/` | Tài liệu và thông tin đầu vào |
| `templates/` | Template chuẩn ánh xạ tới outputs |
| `checklists/` | Kiểm tra tính đầy đủ, chất lượng và điều kiện G1 |
| `outputs/` | Danh mục và cấu trúc artifact đầu ra |

Các đầu ra chuẩn, phân loại bắt buộc/tùy chọn và vị trí lưu được định nghĩa tại [outputs/README.md](outputs/README.md); danh sách template và ánh xạ nằm tại [templates/README.md](templates/README.md).

## 2. Nội dung các folder

### 2.1 Inputs — Tài liệu đầu vào

| File | Nội dung |
|---|---|
| `inputs/README.md` | Hướng dẫn chuẩn bị tài liệu đầu vào |
| `inputs/input-document-register.md` | Danh sách tài liệu đầu vào và trạng thái |
| `inputs/business-context.md` | Bối cảnh, mục tiêu và vấn đề nghiệp vụ |
| `inputs/stakeholder-information.md` | Bên liên quan, trách nhiệm và thẩm quyền |
| `inputs/existing-system-context.md` | Hệ thống hiện tại, tích hợp và hạn chế |
| `inputs/constraints-and-assumptions.md` | Ràng buộc và giả định ban đầu |

### 2.2 Checklists — Danh sách kiểm tra

| File | Nội dung |
|---|---|
| `checklists/README.md` | Hướng dẫn sử dụng checklist |
| `checklists/01-input-completeness-checklist.md` | Tính đầy đủ đầu vào |
| `checklists/02-requirement-analysis-checklist.md` | Bao phủ hoạt động phân tích |
| `checklists/03-requirement-quality-checklist.md` | Chất lượng yêu cầu |
| `checklists/04-ambiguity-and-conflict-checklist.md` | Mơ hồ và mâu thuẫn |
| `checklists/05-non-functional-requirement-checklist.md` | Xem xét NFR |
| `checklists/06-G1-approval-checklist.md` | Điều kiện trước khi trình duyệt G1 |

### 2.3 Outputs — Kết quả đầu ra

`outputs/README.md` là nguồn chuẩn cho danh mục, đường dẫn, đầu ra bắt buộc/tùy chọn và quy tắc sử dụng. Cấu trúc chuẩn có 12 nhóm deliverables; Business Process Model và Business Glossary là tùy chọn nhưng template vẫn được giữ để project cần thì dùng. `requirement-analysis-report.md` là báo cáo tổng hợp bổ sung, không thay thế artifact nguồn.

#### Quy trình sử dụng

Inputs, templates, checklists và outputs liên kết theo quy trình:

![Quy trình Requirement Analysis](../assets/requirement-analysis-flow.png)

Nếu checklist không đạt:

- Ghi nhận các mục FAIL và artifact/ID bị ảnh hưởng.
- Cập nhật câu hỏi mở trong `outputs/10-assumptions-constraints-risks/open-questions.md`.
- Sửa artifact nguồn trong đúng thư mục output; tránh duy trì bản sao cùng nội dung.
- Chạy lại checklist liên quan và ghi bằng chứng/kết quả review.
- Trình Product Owner review lại; chỉ G1 Approved mới cho phép bàn giao sang System Design.

## 3. Phân bổ Autonomy Level theo công việc

> **Đề xuất, chờ Product Owner xác nhận.** Level gắn với từng action, không gắn cho cả giai đoạn. Định nghĩa L1–L4 tại [ai-instructions.md](ai-instructions.md#9-autonomy-level). G1 luôn bắt buộc, độc lập với level.

| # | Công việc (theo [workflow.md](workflow.md#14-workflow-steps)) | Action AI thực hiện | Level | Người duyệt/kiểm soát |
|---|---|---|---|---|
| 1 | Tiếp nhận và phân loại yêu cầu | Phân loại, tóm tắt tài liệu đầu vào | L1 | Log và kiểm tra tự động; BA xác minh nguồn |
| 2 | Phân tích stakeholder | Đề xuất stakeholder map | L2 | BA review theo checklist |
| 3 | Khảo sát hiện trạng | Tóm tắt quy trình, hệ thống từ tài liệu | L2 | BA kiểm chứng nguồn |
| 4 | Khai thác yêu cầu | Trích xuất yêu cầu có nguồn, đề xuất câu hỏi discovery | L2 | BA kiểm tra nguồn |
| 5 | Mô hình hóa | Đề xuất US/UC, process flow | L2 | BA/PO review theo mẫu |
| 5b | Mô hình hóa | Soạn business rule (logic nghiệp vụ) | L3 | PO approve trước khi đưa vào baseline |
| 6 | Phân tích và làm rõ | Phát hiện mơ hồ, mâu thuẫn, thiếu AC | L2 | BA xử lý; PO quyết định phương án |
| 7 | Xác định ưu tiên | Đề xuất ưu tiên sơ bộ kèm lý do | L4 | PO quyết định cuối cùng |
| 8 | Xác định acceptance criteria | Soạn bản nháp AC | L2 | Stakeholder xác nhận |
| 8b | Xác định acceptance criteria | Đưa AC vào baseline | L3 | PO approve trước khi áp dụng |
| 9 | Đánh giá NFR và rủi ro | Đề xuất NFR checklist | L2 | SA/Security/Compliance xác định |
| 9b | Đánh giá NFR và rủi ro | Quyết định mục tiêu bảo mật, compliance | L4 | Con người quyết định; AI chỉ tư vấn |
| 10 | Thiết lập traceability | Tạo RTM, kiểm tra liên kết thiếu | L2 | BA review theo checklist |
| 11 | Review với stakeholder | Tổng hợp điểm cần thống nhất | L2 | PO/stakeholder ra quyết định |
| 12 | Đóng baseline, trình G1 | Chuẩn bị gói review | L3 | PO approve trước khi chuyển bước |
| 12b | Đóng baseline, G1 | Phê duyệt G1 | L4 | AI không được phê duyệt; PO quyết định |
| — | Quản lý thay đổi sau baseline | Phân tích tác động sơ bộ | L2 | BA quản lý thay đổi |

Cột "Action AI thực hiện" và "Người duyệt" chưa đủ theo chính sách, vốn yêu cầu thêm allowed tools, scope và evidence cho từng action. Các bổ sung này cần PO xác nhận trước khi dùng.
