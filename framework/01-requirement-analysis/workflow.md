# Workflow — Requirement Analysis

> Tài liệu workflow cấp framework cho giai đoạn này. Tuân thủ governance, standards và template dùng chung trong `framework/`; các cấu hình riêng của dự án được kế thừa từ `projects/<Project>/.ai-sdlc/`.

# 1. Giai đoạn 01 — Requirement Analysis

## 1.1 Purpose — Mục đích

Làm rõ vấn đề cần giải quyết, mục tiêu kinh doanh, đối tượng sử dụng, phạm vi, yêu cầu chức năng (FR), yêu cầu phi chức năng (NFR), quy tắc nghiệp vụ, ràng buộc và tiêu chí nghiệm thu. Tạo baseline yêu cầu đủ rõ, có thể truy vết và kiểm chứng để làm đầu vào cho System Design.

## 1.2 Workflow Overview — Tổng quan luồng xử lý

```text
Business Need / Project Charter
        ↓
Discovery & Stakeholder Analysis
        ↓
Elicit Requirements
        ↓
Analyze, Model & Prioritize
        ↓
Define Acceptance Criteria & Traceability
        ↓
Validate with Stakeholders
        ↓
G1 — Approve Requirement Baseline
        ↓
Handoff to System Design
```

## 1.3 Entry Criteria — Điều kiện bắt đầu

- Có Project Charter, business request hoặc problem statement tối thiểu.
- Xác định được sponsor/business owner hoặc người có quyền quyết định yêu cầu.
- Có thông tin ban đầu về phạm vi, bối cảnh, hệ thống liên quan và ràng buộc.
- Dự án đã xác định nơi lưu tài liệu, quy tắc đặt tên và quyền truy cập.
- Nếu đầu vào chưa đầy đủ, BA lập danh sách câu hỏi và đánh dấu phần chưa xác minh; không tự suy diễn thành yêu cầu đã xác nhận.

## 1.4 Workflow Steps — Các bước thực hiện

1. **Tiếp nhận và phân loại yêu cầu:** ghi nhận nguồn yêu cầu, vấn đề, mục tiêu, lý do kinh doanh, mức ưu tiên ban đầu và người đề xuất.
2. **Phân tích stakeholder:** xác định nhóm người dùng, người ảnh hưởng, người phê duyệt, nhu cầu và xung đột lợi ích.
3. **Khảo sát hiện trạng:** thu thập quy trình hiện tại, hệ thống liên quan, dữ liệu, tích hợp, pain points và các giới hạn.
4. **Khai thác yêu cầu:** tổ chức workshop/interview hoặc phân tích tài liệu; ghi nhận FR, NFR, business rules, assumptions và constraints.
5. **Mô hình hóa:** xây dựng use case/user story, process flow, domain concepts, context diagram hoặc mô hình phù hợp.
6. **Phân tích và làm rõ:** phát hiện trùng lặp, mâu thuẫn, thiếu trường hợp biên, yêu cầu không khả thi hoặc không đo lường được.
7. **Ưu tiên:** thống nhất phương pháp ưu tiên (ví dụ MoSCoW hoặc value/risk); ghi rõ lý do và người quyết định.
8. **Xác định acceptance criteria:** mô tả điều kiện nghiệm thu có thể kiểm chứng; bổ sung ví dụ và dữ liệu kiểm thử khi cần.
9. **Đánh giá NFR và rủi ro:** định lượng mục tiêu hiệu năng, availability, security, privacy, scalability, usability, maintainability và compliance khi áp dụng.
10. **Thiết lập traceability:** liên kết business objective → requirement → acceptance criteria; gắn ID ổn định cho từng yêu cầu.
11. **Review với stakeholder:** trình bày phạm vi, ngoại lệ, giả định, phụ thuộc và nội dung chưa thống nhất; ghi nhận quyết định.
12. **Đóng baseline:** cập nhật trạng thái, version, owner, change history và trình G1 phê duyệt.

## 1.5 Input — Đầu vào

- Project Charter / business case / problem statement.
- Business request, hợp đồng hoặc tài liệu sản phẩm hiện có.
- Quy trình nghiệp vụ hiện tại, tài liệu hệ thống legacy và phản hồi người dùng.
- Stakeholder list, chính sách, quy định pháp lý và tiêu chuẩn ngành.
- Project context, technology constraints và các quyết định đã có.

## 1.6 AI Activities — Hoạt động AI

- Tóm tắt và phân loại tài liệu đầu vào; trích xuất yêu cầu và nguồn tham chiếu.
- Đề xuất câu hỏi discovery, stakeholder map và các điểm cần xác minh.
- Phát hiện yêu cầu mơ hồ, trùng lặp, mâu thuẫn, thiếu acceptance criteria.
- Đề xuất user story, use case, business rule, process flow và NFR checklist.
- Đề xuất phân nhóm/ưu tiên sơ bộ kèm lý do; không tự quyết định ưu tiên cuối cùng.
- Tạo requirement traceability matrix và kiểm tra liên kết bị thiếu.
- Phân tích tác động sơ bộ khi yêu cầu thay đổi.
- Gắn nhãn nội dung do AI suy luận và không trình bày suy luận như sự thật đã xác nhận.

## 1.7 Human Activities — Hoạt động con người

- BA dẫn dắt discovery, xác minh nguồn và làm rõ ngữ cảnh.
- Product Owner/Business Owner quyết định mục tiêu, phạm vi, ưu tiên và trade-off.
- Stakeholder xác nhận quy trình, quy tắc nghiệp vụ và acceptance criteria.
- SA/Security/Compliance tham gia xác định NFR, ràng buộc và rủi ro chuyên môn.
- BA chịu trách nhiệm chất lượng tài liệu, traceability và quản lý thay đổi.

## 1.8 Output — Đầu ra

Giai đoạn Requirement Analysis tạo ra các đầu ra sau:

- **Tài liệu yêu cầu nghiệp vụ (Business Requirements Document — BRD):** mục tiêu và nhu cầu nghiệp vụ, yêu cầu của stakeholder; các yêu cầu nghiệp vụ (BRQ) có ID và tham chiếu đến quy tắc nghiệp vụ liên quan.
- **Định nghĩa phạm vi (Scope Definition):** phạm vi dự án/hệ thống, nội dung trong và ngoài phạm vi, ranh giới hệ thống và các phụ thuộc bên ngoài.
- **Đặc tả yêu cầu chức năng (Functional Requirements Specification — FRS):** các yêu cầu chức năng (FR) có ID, mô tả, mức ưu tiên, nguồn, owner và trạng thái; mỗi yêu cầu có tiêu chí xác minh phù hợp.
- **Yêu cầu phi chức năng (Non-functional Requirements — NFR):** các NFR có ID, hạng mục, mô tả, mức ưu tiên, nguồn, owner và trạng thái; có tiêu chí đo lường hoặc phương pháp kiểm chứng khi phù hợp.
- **User Story và Use Case:** mô tả nhu cầu, actor, mục tiêu và kịch bản; liên kết với các FR/NFR liên quan.
- **Tiêu chí nghiệm thu (Acceptance Criteria):** tiêu chí cho từng User Story/Use Case, có thể kiểm thử và xác định kết quả đạt/không đạt.
- **Danh mục quy tắc nghiệp vụ (Business Rules Catalogue):** các quy tắc nghiệp vụ (BR) có ID, mô tả, điều kiện và kết quả mong đợi; tham chiếu đến BRQ/FR liên quan.
- **Mô hình quy trình nghiệp vụ (Business Process Model, khi áp dụng):** quy trình, sơ đồ và mô tả; xác định actor, hoạt động, quyết định và sự kiện nghiệp vụ.
- **Bảng thuật ngữ nghiệp vụ (Business Glossary, khi áp dụng):** thuật ngữ, định nghĩa và từ viết tắt.
- **Giả định, ràng buộc, phụ thuộc, rủi ro và câu hỏi mở:** ghi nhận nội dung, owner và trạng thái xử lý.
- **Ma trận truy vết yêu cầu (Requirement Traceability Matrix — RTM):** truy vết BRQ → FR/NFR → User Story/Use Case → Acceptance Criteria; làm cơ sở liên kết với Test Case ở giai đoạn Testing & QA.
- **Hồ sơ review yêu cầu và phê duyệt G1:** ghi nhận phát hiện review và cách xử lý, ý kiến của Product Owner, quyết định G1, người phê duyệt, thời điểm, tài liệu và phiên bản được phê duyệt.

Business Process Model và Business Glossary chỉ cần tạo khi phù hợp với phạm vi dự án; các đầu ra còn lại là bắt buộc.


## 1.9 Quality Check — Kiểm tra chất lượng

- Mỗi yêu cầu có ID, nguồn, mô tả rõ, owner và mức ưu tiên.
- Yêu cầu có thể kiểm chứng; tránh từ mơ hồ như “nhanh”, “thân thiện” nếu không có ngưỡng.
- FR/NFR không mâu thuẫn; NFR có metric/target hoặc ghi rõ cách xác định.
- Acceptance criteria bao phủ luồng chính, luồng lỗi và trường hợp biên quan trọng.
- Phạm vi in-scope/out-of-scope, giả định và phụ thuộc được công khai.
- Có traceability tới mục tiêu kinh doanh; không có yêu cầu orphan quan trọng.
- Dữ liệu nhạy cảm và yêu cầu tuân thủ được nhận diện đúng mức.

## 1.10 Human Review Gate — Điểm phê duyệt bắt buộc

**G1 — Requirement Baseline Approval**

Người phê duyệt: Product Owner; BA chịu trách nhiệm chuẩn bị. SA, Security/Compliance tham vấn khi có yêu cầu kỹ thuật hoặc tuân thủ liên quan.

Điều kiện duyệt:
- Phạm vi và mục tiêu được thống nhất.
- Các yêu cầu quan trọng và acceptance criteria đủ rõ.
- NFR, rủi ro, giả định và phụ thuộc đã được xem xét.
- Các open issues còn lại có owner và kế hoạch xử lý; không có vấn đề critical bị che giấu.

Bằng chứng: approval record, phiên bản tài liệu, người duyệt, thời điểm và điều kiện/ngoại lệ.

## 1.11 Exit Criteria — Điều kiện hoàn thành

Giai đoạn chỉ được xem là hoàn thành khi đáp ứng đầy đủ các điều kiện sau:

- Các đầu ra bắt buộc đã được kiểm tra.
- Các vấn đề trọng yếu đã được xử lý; không còn câu hỏi critical ngăn cản thiết kế. Các mục còn lại có owner và thời hạn xử lý.
- Requirement baseline được lưu đúng vị trí, có version; RTM và danh sách câu hỏi mở được cập nhật.
- G1 được Product Owner phê duyệt (Approved).

## 1.12 Exception Handling — Xử lý ngoại lệ

- **Thiếu stakeholder:** ghi nhận giả định, đánh dấu provisional và không baseline phần chưa được người có thẩm quyền xác nhận.
- **Yêu cầu mâu thuẫn:** lập decision log; chuyển Product Owner/Business Owner quyết định.
- **Phạm vi thay đổi:** tạo change request, phân tích tác động tới chi phí/tiến độ/kiến trúc/test; đánh giá có cần mở lại G1.
- **NFR chưa định lượng:** tổ chức phiên làm rõ với SA/ops/business; không tự đặt ngưỡng tùy tiện.
- **AI tạo thông tin không có nguồn:** loại bỏ hoặc xác minh độc lập trước khi đưa vào baseline.

## 1.13 Next Stage — Chuyển sang giai đoạn tiếp theo

Bàn giao requirement baseline, RTM, NFR, business rules, constraints, risks và quyết định G1 cho **02 — System Design**.

---
