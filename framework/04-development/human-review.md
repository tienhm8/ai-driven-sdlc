# Human Review – Development

> **Giai đoạn:** 04 – Development  
> **Mục đích:** Bảo đảm thay đổi mã nguồn đúng yêu cầu và thiết kế, an toàn, có thể kiểm thử, bảo trì được và tuân thủ chuẩn kỹ thuật.  
> **Review Gate liên quan:** Stage 04 xác minh G1/G2/G3 trước coding, không phê duyệt lại; G4 được quyết định tại Stage 05 trước merge.  
> **Người chịu trách nhiệm chính:** Developer thực hiện; Tech Lead chịu trách nhiệm giám sát kỹ thuật

## 1. Nguyên tắc review

- Developer là người chịu trách nhiệm đối với code được commit dưới danh tính của mình, kể cả code do AI sinh hoặc chỉnh sửa.
- AI-generated code phải được đọc, hiểu và kiểm chứng; không merge code mà người chịu trách nhiệm không thể giải thích hành vi và rủi ro chính.
- Không đưa secrets, dữ liệu cá nhân hoặc mã nguồn hạn chế vào công cụ AI không được phê duyệt.
- Không cho AI tự mở rộng phạm vi, thay đổi contract, schema, authorization hoặc kiến trúc ngoài task đã duyệt.
- Thay đổi phải có test phù hợp và được đưa qua quy trình Code Review/G4 độc lập.

## 2. Vai trò và trách nhiệm

| Vai trò | Trách nhiệm review / quyết định |
|---|---|
| Developer / Implementer | Review thay đổi của chính mình trước commit; xác nhận logic, test, tài liệu, phạm vi và tính an toàn. |
| Tech Lead | Hướng dẫn kỹ thuật, giải quyết vấn đề vượt phạm vi task, kiểm soát design deviation và quyết định escalation. |
| Pair / Supporting Developer | Review chéo khi task phức tạp hoặc có rủi ro; kiểm tra giả định và khả năng bảo trì. |
| Security Champion / Security Engineer | Tham gia review thay đổi liên quan authentication, authorization, cryptography, input handling, secrets hoặc dữ liệu nhạy cảm. |
| DBA / Data Owner | Review migration và thay đổi dữ liệu có ảnh hưởng schema, integrity, hiệu năng hoặc khả năng khôi phục. |
| QA Engineer | Tư vấn testability, test data và các trường hợp kiểm thử; không thay developer chịu trách nhiệm chất lượng code. |

## 3. Trách nhiệm review của con người

1. **Task alignment:** Code giải quyết đúng task đã được G3 xác nhận; không có thay đổi ngoài phạm vi không được giải thích.
2. **Business logic:** Developer hiểu và xác nhận logic, validation, boundary case, error path và quy tắc nghiệp vụ.
3. **Design conformance:** Tuân thủ architecture, API contract, data model, ADR và coding standards đã duyệt.
4. **Correctness:** Kiểm tra null/empty, concurrency, transaction, idempotency, timezone, precision, retry và các edge case phù hợp.
5. **Security:** Kiểm tra input validation, output encoding, authentication, authorization, secret handling, injection, dependency và data exposure.
6. **Data safety:** Migration có đánh giá backward compatibility, data loss, locking, rollback/recovery và thứ tự triển khai.
7. **Testing:** Có unit/integration test phù hợp; test không chỉ phản ánh implementation mà phải kiểm chứng hành vi mong đợi.
8. **Maintainability:** Code dễ đọc, module boundary hợp lý, không tạo abstraction/complexity không cần thiết.
9. **Performance & resilience:** Tránh query/API không hiệu quả, resource leak, unbounded operation và failure handling không an toàn.
10. **Observability:** Log/metric/trace đủ hỗ trợ vận hành nhưng không làm lộ secrets hoặc dữ liệu nhạy cảm.
11. **Dependencies & licensing:** Dependency mới được đánh giá về bảo mật, license, nguồn gốc và mức độ cần thiết.
12. **Documentation:** Cập nhật API docs, migration notes, config, runbook hoặc tài liệu liên quan khi có thay đổi.
13. **AI contribution verification:** Xác minh các API, thư viện, method, config và giả định do AI đề xuất có thật, đúng phiên bản và tương thích codebase.

## 4. Review theo Autonomy Level

| Level | Cách con người tham gia |
|---|---|
| L1 | AI có thể format, tạo comment/doc nháp hoặc chạy kiểm tra không làm thay đổi hành vi. Thay đổi phải nằm trong phạm vi cho phép, có log và có thể hoàn nguyên. |
| L2 | Developer review theo mẫu/điều kiện đối với unit test, refactor nhỏ hoặc sửa lỗi giới hạn; kiểm tra test và diff trước khi gửi PR. |
| L3 | Bắt buộc người có chuyên môn review trước khi chấp nhận thay đổi business logic, API, schema, authorization, dữ liệu hoặc kiến trúc. |
| L4 | Con người quyết định các thay đổi có rủi ro đặc biệt cao, ngoại lệ bảo mật/tuân thủ hoặc hành động không thể đảo ngược; AI chỉ tư vấn. |

**Quy tắc:** L1/L2 không tự động cấp quyền merge. Mọi thay đổi phải tuân thủ branch protection, CI và G4 theo policy repository.

## 5. Checklist review trước khi gửi PR

- [ ] [Development readiness checklist](checklists/development-readiness.md) = `Ready`.
- [ ] Diff nằm trong phạm vi task; thay đổi ngoài phạm vi được tách hoặc giải trình.
- [ ] Developer hiểu và có thể giải thích code do AI tạo.
- [ ] Logic nghiệp vụ, edge case và error handling đã được kiểm tra.
- [ ] Không vi phạm kiến trúc, API contract, schema hoặc coding standards.
- [ ] Test phù hợp đã được tạo/cập nhật; kết quả thực thi thực tế đã được ghi vào test evidence.
- [ ] Không chứa secrets, dữ liệu nhạy cảm hoặc thông tin không được phép.
- [ ] Dependency, license và security impact đã được xem xét.
- [ ] Migration và rollback/recovery được xem xét nếu có thay đổi dữ liệu.
- [ ] Logging/metrics/docs được cập nhật khi cần.
- [ ] Self-review diff đã hoàn tất; PR mô tả rõ thay đổi và cách test.

## 6. PR Readiness Check — bàn giao 04 → 05

Developer có thể mở PR `Draft` để xin phản hồi sớm. Chỉ bàn giao chính thức khi đủ [điều kiện PR Readiness Check](workflow.md#410-pr-readiness-check--bàn-giao-04--05); nêu lý do cho check bắt buộc `Fail` hoặc `Not run` không đủ để bàn giao.

Developer ghi kết quả vào [handover checklist](checklists/handover-checklist.md); Tech Lead/maintainer xác nhận thêm nếu policy dự án yêu cầu. Self-review và kiểm tra bàn giao không thay thế reviewer độc lập và quyết định G4 ở 05.

## 7. Khi yêu cầu AI làm lại

Developer cung cấp task context, lỗi/test failure, coding convention và giới hạn thay đổi. AI chỉ sửa trong phạm vi được giao. Developer phải xem lại toàn bộ diff sau mỗi lần AI chỉnh sửa, không chỉ xem phần AI báo cáo đã thay đổi.

## 8. Bằng chứng và hồ sơ review

Lưu task link, commit/PR, danh tính người thực hiện, công cụ/AI contribution theo policy, kết quả test/CI, dependency/migration/security findings, self-review và các thay đổi sau review. Không ghi secrets hoặc dữ liệu nhạy cảm vào audit log.

## 9. Trách nhiệm cuối cùng

Developer chịu trách nhiệm về thay đổi mình gửi review. Tech Lead chịu trách nhiệm giải quyết sai lệch kỹ thuật và escalation. Reviewer độc lập thực hiện quyết định G4 tại giai đoạn Code Review. AI không phải tác giả chịu trách nhiệm pháp lý/nghiệp vụ và không được tự phê duyệt code của mình.
