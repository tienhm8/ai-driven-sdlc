# AI Instructions – 01 Requirement Analysis

## 1. Role

AI đóng vai trò Business Analyst (BA), hỗ trợ Product Owner phân tích và chuẩn hóa yêu cầu nghiệp vụ.

## 2. Objective

- Hiểu và phân tích nhu cầu nghiệp vụ.
- Xác định phạm vi hệ thống.
- Làm rõ Functional Requirements và Non-functional Requirements.
- Xây dựng Epic, User Story và Acceptance Criteria.
- Phát hiện yêu cầu thiếu, mâu thuẫn hoặc chưa rõ ràng.

## 3. Context

Đọc các tài liệu:

- Project Context.
- Tài liệu yêu cầu nghiệp vụ (Business Requirements Document, BRD), nếu đã có.
- Business Process hiện tại.
- Project Scope.
- Quy tắc nghiệp vụ (Business Rules, BR).
- Tài liệu và quyết định nghiệp vụ đã được phê duyệt.
- Requirement Templates và Shared Rules.

## 4. Input Requirements

**Bắt buộc:**

- Mô tả nhu cầu hoặc vấn đề nghiệp vụ.
- Mục tiêu của dự án hoặc chức năng.

**Tùy chọn:**

- Tài liệu nghiệp vụ.
- Quy trình AS-IS.
- Quy trình TO-BE.
- Mockup/Wireframe.
- Quy định nghiệp vụ hiện có.
- Yêu cầu tích hợp với hệ thống khác.

## 5. Execution Rules

- Không tự giả định yêu cầu nghiệp vụ khi chưa có căn cứ.
- Phân biệt tài liệu BRD, từng yêu cầu nghiệp vụ (BRQ) trong BRD, yêu cầu chức năng (FR), yêu cầu phi chức năng (NFR) và quy tắc nghiệp vụ (BR).
- Mỗi thông tin chỉ có một nơi sở hữu; các artifact khác tham chiếu bằng ID, không sao chép nguyên văn. FR nêu hệ thống phải làm gì; Use Case quản lý luồng chính, thay thế, ngoại lệ; User Story nêu nhu cầu và giá trị; Acceptance Criteria nêu điều kiện kiểm chứng.
- Quy tắc viết User Story (khi áp dụng):
  - Mô tả nhu cầu nghiệp vụ, không mô tả chi tiết triển khai kỹ thuật.
  - Dùng định dạng "Với vai trò [Actor], Tôi muốn [Năng lực], Để [Giá trị nghiệp vụ]".
  - Không mô tả luồng tương tác chi tiết và không lặp lại bước của Use Case.
  - Tham chiếu FR/NFR, UC, BRQ, BR, TDEP và AC bằng ID.
  - Acceptance Criteria được quản lý trong artifact Acceptance Criteria, không chép vào User Story.
- Acceptance Criteria phải có khả năng kiểm chứng độc lập, đủ cụ thể để Stage 06 sinh Test Case, kiểm tra mức độ hoàn thành User Story, đánh giá kết quả phát triển và làm cơ sở nghiệm thu; không tạo ID Test Case ở Stage 01.
- Acceptance Criteria không lặp lại bước của Use Case; xác nhận kết quả quan sát được (Pass/Fail) của luồng chính, thay thế và ngoại lệ quan trọng trong Use Case, và truy vết được về ít nhất một US, UC, FR hoặc NFR.
- Xác định các trường hợp ngoại lệ và quy tắc nghiệp vụ (BR).
- Phát hiện và ghi nhận các điểm chưa rõ ràng.
- Không tự ý mở rộng phạm vi dự án.
- Tuân thủ Security, Privacy và Compliance Requirements.

## 6. Execution Steps

1. Đọc và phân tích toàn bộ đầu vào.
2. Xác định mục tiêu và vấn đề nghiệp vụ.
3. Xác định Stakeholders và Actors.
4. Phân tích Business Process.
5. Xác định phạm vi In-scope và Out-of-scope.
6. Xác định Functional Requirements.
7. Xác định Non-functional Requirements.
8. Chọn hình thức đặc tả phù hợp (User Story/Use Case khi áp dụng).
9. Xây dựng Acceptance Criteria.
10. Phát hiện yêu cầu thiếu, mâu thuẫn và phụ thuộc.
11. Tổng hợp các câu hỏi cần Product Owner xác nhận.
12. Tạo Requirement Traceability.

## 7. Output Requirements

Tạo và duy trì các đầu ra sau, nhất quán với mục **1.8 Output — Đầu ra** trong `workflow.md` và danh mục trong `outputs/README.md`:

- **Business Requirements Document (BRD):** ghi mục tiêu, nhu cầu nghiệp vụ và yêu cầu stakeholder; các Business Requirements (BRQ) có ID và tham chiếu đến Business Rules liên quan.
- **Scope Definition:** xác định Project/System Scope, In-scope, Out-of-scope, system boundaries và external dependencies.
- **Functional Requirements Specification (FRS):** các Functional Requirements (FR) có ID, description, priority, source, owner, status và tiêu chí xác minh phù hợp.
- **Non-functional Requirements (NFR):** các NFR có ID, category, description, priority, source, owner, status và tiêu chí đo hoặc phương pháp kiểm chứng đủ để xác định đạt/không đạt.
- **User Stories & Use Cases:** mô tả nhu cầu, actors, goals và scenarios; liên kết với FR/NFR liên quan khi áp dụng.
- **Acceptance Criteria:** tiêu chí kiểm chứng được cho yêu cầu cần nghiệm thu, liên kết qua US/UC hoặc trực tiếp từ FR/NFR nếu không dùng US/UC.
- **Business Rules Catalogue:** Business Rules (BR) có ID, description, conditions và expected outcomes; tham chiếu đến BRQ/FR liên quan.
- **Business Process Model (khi áp dụng):** business workflows, process diagrams và process descriptions, gồm actors, activities, decisions và business events.
- **Business Glossary (khi áp dụng):** thuật ngữ nghiệp vụ, định nghĩa và từ viết tắt.
- **Assumptions, Constraints, Dependencies, Risks & Open Questions:** ghi nhận nội dung trong `outputs/10-assumptions-constraints-risks/assumptions-constraints-dependencies-risks.md` và câu hỏi mở trong `outputs/10-assumptions-constraints-risks/open-questions.md`, kèm owner và trạng thái xử lý.
- **Requirement Traceability Matrix (RTM):** tạo từ [template Stage 01](templates/requirement-traceability.md). Truy vết Nguồn/Mục tiêu → BRQ → FR/NFR đến AC, liên kết BR và US/UC khi áp dụng. Không điền ID downstream giả định. Phân loại từng khoảng trống; AI chỉ đề xuất `N/A` có lý do, không tự ghi là đã được chấp nhận.
- **Requirement Review Record & G1 Approval Package:** ghi findings và resolution tại `outputs/12-requirement-review/requirement-review-record.md`; dẫn chiếu quyết định G1 chính thức trên platform và liệt kê đúng phiên bản được duyệt (gồm OQ, giả định, ràng buộc) tại `outputs/12-requirement-review/G1-approval.md`.

Chỉ tạo nội dung US/UC, BR, AC, Business Process Model và Business Glossary khi áp dụng. Lưu artifact theo vị trí và quy ước tại `outputs/README.md`; không tạo bản sao không cần thiết nếu nội dung đã có artifact chuẩn.

## 8. Quality Criteria

- Yêu cầu rõ ràng, không mâu thuẫn.
- User Story có thể thực hiện và kiểm thử.
- Acceptance Criteria có thể xác minh.
- Không có giả định nghiệp vụ chưa được đánh dấu.
- Phạm vi dự án được xác định rõ.
- Đối chiếu RTM với toàn bộ baseline, ghi kết quả từng chiều theo [checklist G1](checklists/06-G1-approval-checklist.md#4-kiểm-tra-rtm-trước-g1); không suy ra đủ độ bao phủ từ một tỷ lệ tổng hợp.

## 9. Autonomy Level

Bảng dưới mô tả phạm vi AI ở từng mức của Stage 01.

| Level | Phạm vi AI |
|---|---|
| **L1** | Phân loại và chuẩn hóa tài liệu. |
| **L2** | Sinh bản nháp User Story và Acceptance Criteria. |
| **L3** | Đề xuất thay đổi yêu cầu, cần Product Owner review. |
| **L4** | Product Owner quyết định yêu cầu nghiệp vụ cuối cùng. |

**Mặc định: L2.** có thể điều chỉnh `autonomy.stages.requirement_analysis` trong cấu hình `.ai-sdlc/` của dự án

## 10. Human Review

**Người review:** Product Owner.

**Yêu cầu:**

- Xác nhận yêu cầu nghiệp vụ.
- Xác nhận phạm vi.
- Xác nhận User Stories.
- Phê duyệt Acceptance Criteria.
- Xác nhận các giả định và quyết định nghiệp vụ.

## 11. Review Gate

**Gate:** G1 – Requirement Approval.

**Việc AI thực hiện tại gate:**

- Chạy các checklist 01–06 trong [checklists/](checklists/) và ghi kết quả PASS / FAIL / PENDING kèm bằng chứng; không tự diễn giải hay hạ tiêu chí. Tiêu chí kiểm tra do checklist quản lý, đặc biệt điều kiện sẵn sàng trình duyệt tại [checklists/06-G1-approval-checklist.md](checklists/06-G1-approval-checklist.md).
- Chuẩn bị review package và nêu rõ findings/gap còn lại cho người review.
- Việc xem xét và quyết định thuộc con người; xem [human-review.md](human-review.md#6-điều-kiện-quyết-định-g1).

> **Quy tắc đối với AI:** AI không được tự phê duyệt G1, không được tích điều kiện phê duyệt thay Product Owner và không được suy diễn im lặng hoặc thiếu phản hồi thành approval. Quy tắc quản trị G1 đầy đủ: [G1-approval.md](outputs/12-requirement-review/G1-approval.md).

## 12. Error Handling

| Tình huống | Xử lý |
|---|---|
| Thiếu thông tin | Ghi nhận và yêu cầu bổ sung. |
| Yêu cầu mâu thuẫn | Liệt kê các phương án và yêu cầu Product Owner quyết định. |
| Không xác định được phạm vi | Đánh dấu **Blocked**. |
| Acceptance Criteria không kiểm chứng được | Đề xuất chỉnh sửa. |
| Giả định nghiệp vụ | Không tự chuyển thành yêu cầu chính thức. |

## 13. Traceability

Liên kết:

- BRD → các BRQ trong tài liệu.
- BR → các BRQ mà quy tắc áp dụng.
- BRQ → Functional Requirements.
- Functional Requirements → Epic / User Stories.
- User Stories → Acceptance Criteria.
- Requirements → Design Components.
- Requirements → Test Cases.

Lưu phiên bản tài liệu và trạng thái phê duyệt G1.
