# Human Review – System Design

> **Giai đoạn:** 02 – System Design  
> **Mục đích:** Bảo đảm giải pháp kỹ thuật đáp ứng yêu cầu đã duyệt, an toàn, khả thi, vận hành được và có các quyết định kiến trúc minh bạch.  
> **Review Gate:** G2 – Design Approval  
> **Người phê duyệt chính:** Solution Architect / người được chỉ định có thẩm quyền kiến trúc

## 1. Nguyên tắc review

- Review thiết kế dựa trên requirement baseline đã qua G1; mọi sai khác hoặc giả định mới phải được ghi nhận.
- Đánh giá trade-off và rủi ro, không chỉ kiểm tra sơ đồ hoặc tài liệu có đủ mục.
- AI có thể đề xuất kiến trúc, schema, API và phương án; con người quyết định lựa chọn kiến trúc và chấp nhận rủi ro.
- Thiết kế có ảnh hưởng lớn đến bảo mật, dữ liệu, tích hợp hoặc khả năng vận hành phải có chuyên gia phù hợp tham gia.
- Quyết định kiến trúc quan trọng phải được ghi thành Architecture Decision Record (ADR).

## 2. Vai trò và trách nhiệm

| Vai trò | Trách nhiệm review / quyết định |
|---|---|
| Solution Architect – **Approver G2** | Đánh giá tổng thể, trade-off, nguyên tắc kiến trúc, lựa chọn công nghệ và phê duyệt thiết kế trong phạm vi thẩm quyền. |
| Tech Lead | Review khả năng triển khai, phân rã thành phần, tính nhất quán kỹ thuật và tác động đến codebase hiện tại. |
| Security Architect / Security Engineer | Review threat model, trust boundaries, authentication, authorization, secrets, mã hóa và rủi ro bảo mật. |
| DBA / Data Architect | Review data model, integrity, indexing, transaction, backup/restore, retention, migration và hiệu năng dữ liệu. |
| API / Integration Owner | Review contract, versioning, backward compatibility, rate limit, error model và tích hợp hệ thống ngoài. |
| SRE / DevOps | Review deployability, observability, resilience, capacity, recovery và yêu cầu vận hành. |
| Product Owner / BA | Xác nhận thiết kế không làm sai lệch yêu cầu và trải nghiệm nghiệp vụ trọng yếu. |

## 3. Trách nhiệm review của con người

1. **Requirement coverage:** Các yêu cầu chức năng và phi chức năng quan trọng được ánh xạ tới thành phần thiết kế.
2. **Architecture fitness:** Kiến trúc phù hợp quy mô, tải, độ phức tạp, vòng đời và năng lực đội ngũ; không over-engineer hoặc under-engineer rõ rệt.
3. **Architecture decisions:** Các lựa chọn quan trọng, phương án thay thế, hệ quả và lý do lựa chọn được ghi trong ADR.
4. **Security & privacy:** Trust boundary, threat model, identity, authorization, secret management, encryption, data minimization và audit được xem xét.
5. **Data architecture:** Schema, quan hệ, constraint, transaction, consistency, partitioning, migration, backup, retention và data ownership phù hợp.
6. **API & integration:** Contract, validation, error handling, idempotency, timeout, retry, versioning và compatibility được định nghĩa.
7. **Reliability & performance:** Failure mode, bottleneck, caching, scaling, availability, recovery objectives và graceful degradation được đánh giá.
8. **Operability:** Logging, metrics, tracing, alerting, health check, deployment, rollback và runbook có thể triển khai.
9. **Maintainability:** Ranh giới module, dependency, coding pattern, testability và khả năng thay đổi trong tương lai hợp lý.
10. **Cost & constraints:** Chi phí hạ tầng/dịch vụ, license, giới hạn nền tảng, vendor lock-in và năng lực vận hành được cân nhắc.
11. **Design completeness:** Sơ đồ, data model, API spec, sequence/flow và các interface cần thiết nhất quán với nhau.
12. **Residual risks:** Rủi ro còn lại được phân loại, có biện pháp giảm thiểu, owner và chấp thuận phù hợp.

## 4. Review theo Autonomy Level

| Level | Cách con người tham gia |
|---|---|
| L1 | AI có thể tạo sơ đồ nháp, format tài liệu hoặc kiểm tra tính nhất quán cơ bản; kết quả không tự trở thành thiết kế được phê duyệt. |
| L2 | Tech Lead/chuyên gia review theo mẫu đối với thay đổi thiết kế nhỏ, nội bộ, không làm thay đổi contract, security boundary hoặc data model quan trọng. |
| L3 | Bắt buộc review và phê duyệt trước khi chấp nhận thay đổi API contract, schema, kiến trúc thành phần, tích hợp, phân quyền hoặc luồng dữ liệu nhạy cảm. |
| L4 | Architect và các chủ sở hữu rủi ro quyết định kiến trúc nền tảng, lựa chọn có tác động lớn, ngoại lệ bảo mật/tuân thủ và trade-off trọng yếu; AI chỉ tư vấn. |

**Quy tắc:** Không dùng kết quả kiểm tra tự động hoặc đánh giá của AI thay cho G2.

## 5. Checklist review

- [ ] Thiết kế dựa trên requirement baseline đã duyệt.
- [ ] Các yêu cầu quan trọng có liên kết tới thành phần thiết kế.
- [ ] Sơ đồ kiến trúc và ranh giới hệ thống rõ ràng.
- [ ] ADR ghi nhận các quyết định kiến trúc quan trọng.
- [ ] Security, privacy và threat model đã được xem xét.
- [ ] Data model, migration, backup và recovery được review.
- [ ] API/interface, versioning và compatibility được xác định.
- [ ] Hiệu năng, khả năng mở rộng, resilience và failure mode được đánh giá.
- [ ] Logging, monitoring, deployment và rollback có phương án.
- [ ] Rủi ro, giả định, chi phí và phụ thuộc được ghi nhận.
- [ ] Các reviewer chuyên môn đã phản hồi.
- [ ] Tài liệu thiết kế có phiên bản và trạng thái rõ ràng.

## 6. Điều kiện quyết định G2

**Approved** khi thiết kế đáp ứng yêu cầu đã duyệt, các rủi ro trọng yếu được xử lý hoặc chấp nhận đúng thẩm quyền, đã có đủ phê duyệt chuyên môn bắt buộc theo phạm vi và Solution Architect phê duyệt. Chỉ quyết định này mới cho phép G2 `Approved` và chốt baseline.

**Changes Requested** khi còn điều kiện cần đóng; **Blocked** khi thiếu đầu vào, bằng chứng hoặc phê duyệt bắt buộc. Cả hai đều chặn bàn giao chính thức sang Stage 03. Sau khi xử lý và lưu bằng chứng, trình Solution Architect phê duyệt lại.

**Changes requested / Reject** khi thiết kế không đáp ứng yêu cầu, có lỗ hổng/rủi ro không thể chấp nhận, thiếu phương án vận hành hoặc các thành phần thiết kế mâu thuẫn.

Các vấn đề chưa ảnh hưởng đến quyết định có thể được ghi thành action có owner và deadline; không được dùng action mở để che giấu rủi ro nghiêm trọng.

## 7. Khi yêu cầu AI làm lại

Reviewer chỉ rõ thành phần/ADR liên quan, vấn đề, ràng buộc cần giữ, tiêu chí chấp nhận và chuyên gia cần tham vấn. AI cập nhật đề xuất; Tech Lead/chuyên gia kiểm tra lại. Thay đổi ảnh hưởng đến quyết định kiến trúc phải được cập nhật ADR và trình G2 lại theo quy định.

## 8. Bằng chứng và hồ sơ review

Lưu design baseline, sơ đồ và spec theo phiên bản; ADR; threat model/risk assessment; comment của reviewer; quyết định G2; danh tính và timestamp người phê duyệt; các ngoại lệ được chấp thuận và ngày hết hạn (nếu có).

## 9. Trách nhiệm cuối cùng

Solution Architect chịu trách nhiệm phê duyệt thiết kế trong phạm vi được giao. Chủ sở hữu bảo mật, dữ liệu và vận hành chịu trách nhiệm đối với đánh giá chuyên môn của mình. Tech Lead chịu trách nhiệm xác nhận khả năng triển khai. AI không có thẩm quyền phê duyệt kiến trúc.
