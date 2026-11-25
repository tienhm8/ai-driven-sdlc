# Human Review – Code Review

> **Giai đoạn:** 05 – Code Review  
> **Mục đích:** Đánh giá độc lập thay đổi trước khi merge, bảo đảm tính đúng đắn, an toàn, phù hợp thiết kế và đạt các tiêu chuẩn chất lượng.  
> **Review Gate:** G4 – Code Approval  
> **Người phê duyệt chính:** Reviewer được phân quyền / Tech Lead

## 1. Nguyên tắc review

- Code review là đánh giá độc lập; người tạo thay đổi không tự phê duyệt PR của mình.
- AI review là lớp hỗ trợ phát hiện vấn đề, không thay thế reviewer con người.
- Reviewer đánh giá cả correctness và impact, không chỉ style hoặc kết quả static analysis.
- PR phải được review đúng phiên bản commit cuối cùng; thay đổi đáng kể sau approval phải yêu cầu review lại.
- Không merge khi còn finding nghiêm trọng/chặn merge hoặc CI bắt buộc chưa đạt.

## 2. Vai trò và trách nhiệm

| Vai trò | Trách nhiệm review / quyết định |
|---|---|
| Peer Reviewer | Kiểm tra logic, khả năng đọc, test, maintainability và tuân thủ coding convention. |
| Senior Developer / Tech Lead – **Approver G4** | Đánh giá rủi ro kỹ thuật, design conformance, phạm vi PR và quyết định approve/request changes theo quyền được giao. |
| Security Reviewer | Review thay đổi có rủi ro bảo mật, authorization, cryptography, secrets hoặc dữ liệu nhạy cảm. |
| DBA / Data Owner | Review schema/migration/query có tác động lớn đến dữ liệu. |
| QA Reviewer (khi cần) | Đánh giá test adequacy, testability và khả năng tái hiện lỗi. |
| PR Author | Trả lời comment, sửa lỗi, giải thích trade-off và xác nhận các thay đổi đã thực hiện. Không tự approve PR của mình. |

## 3. Trách nhiệm review của con người

1. **Scope & context:** PR liên kết task/requirement; thay đổi đúng mục tiêu, không chứa scope creep.
2. **Functional correctness:** Logic đáp ứng Acceptance Criteria, xử lý đúng luồng chính, ngoại lệ và boundary case.
3. **Design & architecture:** Tuân thủ design baseline, ADR, module boundary, API contract và backward compatibility.
4. **Security:** Kiểm tra authentication/authorization, injection, validation, data exposure, secrets, dependency và cấu hình.
5. **Data integrity:** Kiểm tra transaction, consistency, migration, data loss, locking, rollback và tương thích phiên bản.
6. **Reliability:** Đánh giá timeout, retry, idempotency, concurrency, error handling và failure mode.
7. **Performance:** Xem xét query, memory/CPU, I/O, caching, N+1, algorithmic complexity và tải dự kiến.
8. **Test quality:** Test có ý nghĩa, kiểm tra hành vi mong đợi, có negative/edge cases phù hợp; tránh test chỉ xác nhận implementation hiện tại.
9. **Maintainability:** Code dễ hiểu, abstraction hợp lý, naming, duplication và technical debt được đánh giá.
10. **Observability & operations:** Log, metric, tracing, alert impact và cấu hình vận hành phù hợp.
11. **AI review findings:** Xác minh finding AI nêu; không mặc định đúng hoặc bỏ qua chỉ vì AI không phát hiện lỗi.
12. **CI & policy:** Xác nhận required checks, branch protection, approval count và policy repository đạt.
13. **Review completeness:** Comment đã được giải quyết; unresolved thread và exception được xử lý đúng quy trình.

## 4. Phân loại finding

Thang severity chung cho cả stage (ai-instructions, review report, G4 checklist, security review). Ba trường độc lập: **mức độ ảnh hưởng**, **có chặn merge không**, **trạng thái xử lý**.

| Severity | Ý nghĩa | Chặn merge/G4 | Cách xử lý |
|---|---|---|---|
| Critical | Nguy cơ nghiêm trọng về bảo mật, mất/hỏng dữ liệu, sai nghiệp vụ trọng yếu hoặc hệ thống không vận hành được. | Có | Không approve/merge; sửa và review lại. |
| High | Lỗi correctness, reliability, compatibility hoặc chất lượng ảnh hưởng đáng kể. | Có, trừ ngoại lệ | Sửa trước merge; ngoại lệ chỉ theo policy, có người đủ thẩm quyền và risk acceptance. |
| Medium | Vấn đề có ảnh hưởng vừa/cục bộ. | Không mặc định | Sửa trước merge, hoặc có quyết định xử lý/accepted risk/follow-up có owner và deadline. |
| Low | Vấn đề nhỏ, ít ảnh hưởng. | Không | Sửa hoặc tạo tracked follow-up nếu policy cho phép. |
| Info | Gợi ý cải thiện, không phải lỗi. | Không | Author cân nhắc; ghi rõ không phải blocker. |

Tương ứng với cách gọi cũ: Blocker→Critical, Major→High, Minor→Medium/Low, Suggestion→Info.

**Trạng thái xử lý:** Open / Addressed / Accepted Risk / Rejected / Need Clarification (xem review report).

**Recommendation của AI** (Approve / Request Changes / Comment / Blocked) chỉ là khuyến nghị; **quyết định G4** do người có thẩm quyền đưa ra và ghi riêng.

Không hạ mức độ finding chỉ để đạt tiến độ. Finding bảo mật, dữ liệu hoặc tuân thủ phải theo quy trình escalation tương ứng.

## 5. Review theo Autonomy Level

Mức áp dụng theo từng hành động. L1/L2 không miễn G4; quyền merge không đồng nghĩa quyền duyệt G4.

| Level | Cách con người tham gia |
|---|---|
| L1 | AI có thể chạy lint, format, static checks và phân loại finding. Kết quả được lưu log; không tự approve hoặc merge. |
| L2 | AI hỗ trợ review sơ bộ; reviewer lấy mẫu/kiểm tra theo điều kiện đối với thay đổi rủi ro thấp. Required checks vẫn phải đạt. |
| L3 | Reviewer có thẩm quyền bắt buộc đọc diff, đánh giá finding và approve trước merge. Áp dụng cho thay đổi logic, API, schema, quyền và dữ liệu. |
| L4 | Tech Lead/owner (người có thẩm quyền theo policy) quyết định đối với thay đổi rủi ro đặc biệt cao, security exception hoặc thay đổi khó đảo ngược; AI chỉ tư vấn. |

## 6. Checklist G4

- [ ] PR liên kết task/requirement và có mô tả đầy đủ.
- [ ] Reviewer không phải author và có chuyên môn phù hợp.
- [ ] Diff được review trên đúng commit/version.
- [ ] Logic, edge cases và error handling được đánh giá.
- [ ] Thiết kế, API, schema và compatibility phù hợp.
- [ ] Security/data/privacy impact được xem xét.
- [ ] Test phù hợp đã chạy và kết quả có thể truy vết.
- [ ] Required CI checks và policy branch protection đạt.
- [ ] Không còn Critical/High finding chưa xử lý; Medium còn lại có quyết định xử lý theo policy.
- [ ] Comment và thread cần giải quyết đã được xử lý.
- [ ] Approval được ghi nhận bởi đúng người có quyền.
- [ ] Thay đổi sau approval đã được review lại nếu ảnh hưởng nội dung được duyệt.

## 7. Điều kiện quyết định G4

**Approve** khi reviewer xác nhận PR đạt yêu cầu, CI bắt buộc đạt, không còn finding chặn merge và các approval bắt buộc đã có.

**Request changes / Reject** khi phát hiện lỗi cần sửa, thiếu bằng chứng test, rủi ro chưa xử lý hoặc thay đổi không đúng phạm vi.

**Phân biệt quyền:** quyền merge không đồng nghĩa quyền duyệt G4; AI chỉ khuyến nghị. Stage 05 hoàn tất khi merge đã được xác minh (merge commit SHA + link bằng chứng), không chỉ khi PR được approve.

**Merge** chỉ được thực hiện bởi người/quy trình có quyền theo repository policy. Approval không tự động cho phép bỏ qua branch protection. Nếu PR có commit mới sau approval, hệ thống phải xác định approval còn hiệu lực hay cần review lại theo policy.

## 8. Khi yêu cầu AI/author làm lại

Reviewer ghi finding có vị trí cụ thể, mức độ, tác động, điều kiện tái hiện (nếu có) và hướng xác minh. Author/AI sửa; author kiểm tra diff; reviewer xác nhận finding đã được xử lý. Không chấp nhận câu trả lời “đã sửa” nếu không có thay đổi hoặc bằng chứng phù hợp.

## 9. Bằng chứng và hồ sơ review

Lưu PR URL/ID, commit SHA được duyệt, reviewer identity, approval timestamp, review comments, finding/severity, CI run/version, exception, merge identity, merge commit SHA và link bằng chứng merge (build của G5 phải truy vết về commit này).

## 10. Trách nhiệm cuối cùng

Reviewer chịu trách nhiệm đối với quyết định review trong phạm vi chuyên môn và quyền được giao. Tech Lead chịu trách nhiệm đối với approval kỹ thuật theo policy. Author chịu trách nhiệm phản hồi và chất lượng thay đổi. AI finding là tín hiệu hỗ trợ, không phải quyết định cuối cùng.
