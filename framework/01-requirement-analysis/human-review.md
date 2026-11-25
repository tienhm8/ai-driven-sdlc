# Human Review – Requirement Analysis

> **Giai đoạn:** 01 – Requirement Analysis  
> **Mục đích:** Bảo đảm yêu cầu phản ánh đúng nhu cầu nghiệp vụ, có thể kiểm chứng, không mâu thuẫn và đủ rõ trước khi chuyển sang thiết kế.  
> **Review Gate:** G1 – Requirement Approval  
> **Người phê duyệt chính:** Product Owner (PO)

## 1. Nguyên tắc review

- Con người xác nhận **đúng vấn đề cần giải quyết**, không chỉ kiểm tra tài liệu có đầy đủ hình thức.
- AI có thể phân tích, đặt câu hỏi, đề xuất và soạn tài liệu; AI không được tự xác nhận yêu cầu nghiệp vụ hoặc tự phê duyệt G1 (xem [ai-instructions.md](ai-instructions.md#11-review-gate)).
- Không suy diễn nội dung còn thiếu thành sự thật. Giả định phải được đánh dấu, nêu tác động và có người chịu trách nhiệm xác nhận.
- Yêu cầu chưa rõ, mâu thuẫn hoặc chưa có chủ sở hữu phải được làm rõ trước khi baseline.
- Mọi yêu cầu được duyệt phải có ID ổn định. Dùng ID này để nối thiết kế, task, code và test ở các stage sau, không yêu cầu các liên kết đó tại G1.

## 2. Vai trò và trách nhiệm

| Vai trò | Trách nhiệm review / quyết định |
|---|---|
| Product Owner (PO) – **Approver G1** | Xác nhận mục tiêu, phạm vi, ưu tiên, quy tắc nghiệp vụ, User Story, Acceptance Criteria và quyết định cuối cùng về yêu cầu sản phẩm. |
| Business Analyst (BA) | Kiểm tra tính đầy đủ, nhất quán, khả năng kiểm thử; điều phối làm rõ với stakeholder; quản lý requirement baseline và traceability. |
| Business Stakeholder / Subject Matter Expert (SME) | Xác nhận quy trình thực tế, thuật ngữ, quy tắc chuyên ngành, ngoại lệ và tính đúng đắn của nghiệp vụ thuộc phạm vi chuyên môn. |
| UX/UI Designer (khi áp dụng) | Review luồng người dùng, trạng thái giao diện, khả năng tiếp cận và tính phù hợp của trải nghiệm với yêu cầu. |
| Security / Privacy / Compliance (khi áp dụng) | Xác định và review yêu cầu bảo mật, quyền riêng tư, lưu giữ dữ liệu, kiểm toán và tuân thủ. |
| Tech Lead / Architect (tham vấn) | Nêu ràng buộc, rủi ro khả thi và câu hỏi kỹ thuật; không thay PO quyết định mục tiêu nghiệp vụ. |

Một người có thể kiêm nhiều vai trò nếu dự án cho phép, nhưng phải ghi rõ vai trò đang thực hiện khi review và bảo đảm người phê duyệt có thẩm quyền.

## 3. Trách nhiệm review của con người

Người review cần xác nhận tối thiểu:

1. **Business alignment:** Vấn đề, mục tiêu, đối tượng sử dụng và kết quả mong đợi có đúng với nhu cầu đã thống nhất.
2. **Scope:** Phạm vi bao gồm/không bao gồm, MVP, ưu tiên và ranh giới hệ thống được nêu rõ.
3. **Completeness:** Có đủ luồng chính, luồng thay thế, ngoại lệ, trạng thái, quy tắc nghiệp vụ và điều kiện biên quan trọng.
4. **Clarity & consistency:** Thuật ngữ được dùng nhất quán; yêu cầu không mơ hồ, trùng lặp hoặc mâu thuẫn.
5. **Acceptance Criteria:** Tiêu chí nghiệm thu cụ thể, quan sát/kiểm chứng được; không chỉ dùng từ chủ quan như “nhanh”, “thân thiện”, “dễ dùng”.
6. **Non-functional requirements:** Hiệu năng, khả dụng, bảo mật, quyền riêng tư, khả năng mở rộng, accessibility, logging và vận hành được xem xét theo mức độ phù hợp.
7. **Data & authorization:** Loại dữ liệu, phân loại dữ liệu, chủ thể dữ liệu, quyền truy cập và yêu cầu lưu/xóa dữ liệu được xác định khi liên quan.
8. **Assumptions & dependencies:** Giả định, phụ thuộc bên ngoài, giới hạn và câu hỏi mở có owner cùng hạn xử lý.
9. **Testability & traceability:** Mỗi yêu cầu có ID; có thể liên kết với thiết kế và kiểm thử; tiêu chí nghiệm thu có thể chuyển thành test.
10. **Stakeholder validation:** Các stakeholder cần thiết đã được tham vấn; bất đồng chưa giải quyết được ghi nhận.

## 4. Review theo Autonomy Level

| Level | Cách con người tham gia |
|---|---|
| L1 | Có thể áp dụng cho việc định dạng, phân loại hoặc tạo bản nháp không làm thay đổi baseline. Kiểm soát bằng log, kiểm tra tự động và khả năng khôi phục. |
| L2 | BA/PO review theo mẫu hoặc theo điều kiện đối với bản nháp, nhóm yêu cầu rủi ro thấp hoặc thay đổi không ảnh hưởng phạm vi đã duyệt. |
| L3 | Bắt buộc người có chuyên môn review và phê duyệt trước khi chấp nhận thay đổi yêu cầu có ảnh hưởng đến logic nghiệp vụ, phạm vi, dữ liệu, quyền hoặc Acceptance Criteria. |
| L4 | PO/stakeholder có thẩm quyền quyết định mục tiêu, ưu tiên, trade-off nghiệp vụ, chính sách và ngoại lệ quan trọng; AI chỉ phân tích và tư vấn. |

**Quy tắc:** G1 là phê duyệt bắt buộc đối với requirement baseline. Không dùng mức L1/L2 để bỏ qua G1.

## 5. Checklist review

- [ ] Mục tiêu nghiệp vụ và vấn đề cần giải quyết đã được xác nhận.
- [ ] In-scope / out-of-scope và ưu tiên đã rõ.
- [ ] US/UC khi áp dụng mô tả actor, nhu cầu và mục tiêu phù hợp; trường hợp không áp dụng có lý do được chấp nhận trong RTM.
- [ ] Acceptance Criteria rõ ràng, đo/kiểm chứng được.
- [ ] Luồng chính, ngoại lệ và business rules quan trọng đã được xem xét.
- [ ] NFR, bảo mật, quyền riêng tư và yêu cầu tuân thủ đã được xem xét khi áp dụng.
- [ ] Giả định, câu hỏi mở, rủi ro và phụ thuộc có owner.
- [ ] Không còn mâu thuẫn nghiêm trọng hoặc yêu cầu chưa rõ ảnh hưởng đến thiết kế.
- [ ] RTM `PASS` ở từng chiều theo [checklist G1](checklists/06-G1-approval-checklist.md#4-kiểm-tra-rtm-trước-g1) trên đúng phiên bản baseline; không yêu cầu liên kết downstream.
- [ ] Stakeholder cần thiết đã xác nhận.

## 6. Điều kiện quyết định G1

Người review chỉ xem xét quyết định khi kết quả checklist sẵn sàng trình duyệt tại [checklists/06-G1-approval-checklist.md](checklists/06-G1-approval-checklist.md) đã có PASS hoặc ngoại lệ được ghi rõ. Tiêu chí kiểm tra do checklist quản lý; mục này chỉ nêu cơ sở để con người quyết định.

**Approve** khi các yêu cầu trong phạm vi đã đủ rõ, nhất quán, có thể kiểm chứng; các rủi ro/câu hỏi còn lại đã được chấp nhận rõ ràng và có owner; PO xác nhận baseline.

**Changes requested / Reject** khi có mâu thuẫn nghiệp vụ, thiếu quyết định quan trọng, tiêu chí nghiệm thu không thể kiểm chứng, phạm vi chưa thống nhất hoặc có rủi ro chưa được xử lý.

Không được chuyển sang thiết kế như thể yêu cầu đã được duyệt nếu G1 đang `pending`, `in_review`, `rejected` hoặc `changes_requested`. Có thể thực hiện hoạt động discovery không cam kết trong thời gian chờ, nhưng phải đánh dấu là chưa baseline.

## 7. Khi yêu cầu AI làm lại

Người review cần ghi rõ:
- Requirement ID hoặc phần tài liệu cần sửa.
- Vấn đề phát hiện và bằng chứng/ngữ cảnh.
- Kết quả mong đợi hoặc câu hỏi cần stakeholder trả lời.
- Mức độ ưu tiên và người chịu trách nhiệm cung cấp thông tin.

AI chỉ được cập nhật bản nháp/đề xuất. BA kiểm tra thay đổi và PO phê duyệt lại nếu nội dung thuộc phạm vi G1.

## 8. Bằng chứng và hồ sơ review

Lưu trong project instance, không lưu dữ liệu dự án cụ thể vào framework dùng chung:

- Requirement baseline và phiên bản tài liệu được review.
- Danh sách reviewer, vai trò, quyết định và timestamp.
- Comment, câu hỏi mở, giả định được chấp nhận và action owner.
- G1 approval record, liên kết tới phiên bản/commit tài liệu.
- Lịch sử thay đổi sau phê duyệt và lý do mở lại baseline.

## 9. Trách nhiệm cuối cùng

PO chịu trách nhiệm quyết định chấp nhận yêu cầu nghiệp vụ và phạm vi sản phẩm. BA chịu trách nhiệm về chất lượng phân tích và truy vết. SME chịu trách nhiệm xác nhận nội dung chuyên môn được giao. Việc AI tạo hoặc phân tích tài liệu không thay thế các trách nhiệm này.
