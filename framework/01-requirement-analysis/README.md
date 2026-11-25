# 01 — Requirement Analysis

## 0. Bắt đầu nhanh

> Trang này hướng dẫn thao tác. Quy định chính thức nằm ở [workflow.md](workflow.md), [human-review.md](human-review.md) và [G1](../governance/human-review-gates/G1-requirement-approval.md).

**Lối vào:** **BA — Bắt đầu phân tích** (mục 0.1 và 0.2) · **PO — Duyệt G1** (mục 0.3).

### 0.1 Dành cho ai?

- **BA:** người dùng chính, chịu trách nhiệm bộ hồ sơ yêu cầu.
- **Stakeholder / chuyên gia nghiệp vụ (SME):** xác nhận thông tin chuyên môn.
- **PO:** quyết định phạm vi, ưu tiên và duyệt G1.
- **AI:** hỗ trợ phân tích, soạn nháp, phát hiện thiếu sót. AI không xác nhận nghiệp vụ và không phê duyệt.

**Cần gì để bắt đầu?** Mô tả vấn đề hoặc đề xuất dự án, mục tiêu và phạm vi sơ bộ, danh sách stakeholder và người có quyền quyết định, bối cảnh hệ thống hiện tại (nếu có), các ràng buộc đã biết. Không cần có sẵn BRD hoàn chỉnh. Thiếu thông tin thì BA ghi câu hỏi làm rõ, không để AI tự điền. Xem [hướng dẫn chuẩn bị input](inputs/README.md).

### 0.2 Bốn bước

| Bước | Ai làm? | Việc cần làm | Kết quả |
|---|---|---|---|
| **1. Tiếp nhận** | BA, bên đề xuất | Ghi vấn đề, mục tiêu, nguồn tài liệu và người có thẩm quyền. | Danh sách input và câu hỏi làm rõ. |
| **2. Phân tích và soạn nháp** | BA chủ trì, AI hỗ trợ | Tách yêu cầu nghiệp vụ, quy tắc, FR/NFR; viết User Story và tiêu chí nghiệm thu; gắn ID và nguồn. | Bộ yêu cầu nháp và ma trận truy vết. |
| **3. Xác nhận và kiểm tra** | BA, SME, PO; mời kỹ thuật/bảo mật khi cần | SME xác nhận quy tắc và ngoại lệ; PO chốt phạm vi và ưu tiên; BA chạy [checklist G1](checklists/06-G1-approval-checklist.md). | Hồ sơ sẵn sàng trình duyệt, hoặc danh sách nội dung phải sửa. |
| **4. Duyệt và bàn giao** | PO duyệt, BA bàn giao | PO ghi quyết định cho đúng phiên bản hồ sơ. Cần sửa thì BA cập nhật và trình lại. Chỉ bàn giao sang giai đoạn 02 khi G1 đã được duyệt. | Bộ yêu cầu đã duyệt, ma trận truy vết và hồ sơ G1. |

### 0.3 PO cần đọc gì để duyệt G1?

Bắt đầu từ [báo cáo tổng hợp](outputs/requirement-analysis-report.md), rồi đối chiếu phạm vi, tiêu chí nghiệm thu và các vấn đề còn mở với [điều kiện G1](../governance/human-review-gates/G1-requirement-approval.md). AI có thể chuẩn bị [bản ghi review](outputs/12-requirement-review/requirement-review-record.md) và [hồ sơ G1](outputs/12-requirement-review/G1-approval.md), nhưng **PO ghi quyết định**. Hồ sơ thật lưu trong project, không điền vào bản mẫu dùng chung.

---

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

| # | Công việc (theo [workflow.md](workflow.md#14-workflow-steps--các-bước-thực-hiện)) | Action AI thực hiện | Level | Người duyệt/kiểm soát |
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
| 9b | Đánh giá NFR và rủi ro | Trình bày các phương án và đánh đổi về mục tiêu bảo mật, tuân thủ | L4 | Người có thẩm quyền về bảo mật và tuân thủ quyết định; AI chỉ tư vấn |
| 10 | Thiết lập traceability | Tạo RTM, kiểm tra liên kết thiếu | L2 | BA review theo checklist |
| 11 | Review với stakeholder | Tổng hợp điểm cần thống nhất | L2 | PO/stakeholder ra quyết định |
| 12 | Đóng baseline, trình G1 | Chuẩn bị gói review | L3 | PO approve trước khi chuyển bước |
| 12b | Đóng baseline, G1 | Phê duyệt G1 | L4 | AI không được phê duyệt; PO quyết định |
| — | Quản lý thay đổi sau baseline | Phân tích tác động sơ bộ | L2 | BA quản lý thay đổi |

Cột "Action AI thực hiện" và "Người duyệt" chưa đủ theo chính sách, vốn yêu cầu thêm allowed tools, scope và evidence cho từng action. Các bổ sung này cần PO xác nhận trước khi dùng.
