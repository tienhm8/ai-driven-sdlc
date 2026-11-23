# G2 – System Design Approval

**Thời điểm:** Sau System Design, trước coding theo quy trình dự án.  
**Approver:** Solution Architect; Security/Data Architect tham gia khi thuộc phạm vi.

## AI chuẩn bị
Architecture proposal, component/deployment view, data model, API contract, integration flow, security considerations, ADR và trade-offs.

## Điều kiện thông qua
- [ ] Thiết kế đáp ứng requirement đã qua G1.
- [ ] Architecture, boundaries và integration được mô tả.
- [ ] Data model, lifecycle và migration strategy được xem xét.
- [ ] API contract, error handling và compatibility được xác định.
- [ ] Authentication, authorization, threat/risk và privacy được xem xét.
- [ ] NFR performance, scalability, availability, reliability, observability được đề cập.
- [ ] ADR/trade-off quan trọng có quyết định và owner.
- [ ] Rủi ro chưa xử lý có owner và phương án.

**Decision:** Approve / Reject / Blocked. Thay đổi kiến trúc trọng yếu sau G2 phải đánh giá lại.  
**Audit:** Approver, design/ADR version, security evidence, timestamp và decision.
