# G2 – System Design Approval

**Thời điểm:** Sau System Design, trước bàn giao chính thức sang Stage 03 Task Planning. Luồng: G2 → Stage 03 Task Planning → G3 → coding tại Stage 04.

**Approver G2:** Solution Architect được ủy quyền. Tech Lead và chuyên gia ghi kết luận, phạm vi và bằng chứng review; họ không mặc nhiên là approver G2. Phê duyệt chuyên môn bắt buộc theo policy hoặc phạm vi (như Security/Data) phải đầy đủ trước khi G2 Approved. Approval engine hiện chỉ yêu cầu vai trò `solution_architect` cho G2 và không tự kiểm tra các phê duyệt chuyên môn; Solution Architect phải xác minh và ghi bằng chứng trước khi quyết định.

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

## Quyết định và bàn giao

- Áp dụng [policy chung về quyết định và trạng thái gate](gate-policy.md#reviewer-decision). Chỉ hoàn tất G2 khi đã đủ điều kiện gate, có các xác nhận chuyên môn bắt buộc và Solution Architect đã phê duyệt.
- Nếu còn điều kiện cần đóng, ghi `changes_requested` thay vì phê duyệt có điều kiện. Nếu thiếu đầu vào, bằng chứng hoặc xác nhận chuyên môn bắt buộc, ghi `blocked`. Khi đã xử lý, lưu bằng chứng và trình Solution Architect duyệt đúng phiên bản gói; thay đổi vượt phạm vi điều kiện phải review lại theo G2.
- Khi G2 `Approved`, Solution Architect chốt đúng phiên bản design package đã duyệt làm baseline. Stage 03 chỉ tiếp nhận phiên bản đã chốt cùng bằng chứng G2 hợp lệ cho phiên bản đó. Baseline là vai trò của phiên bản gói, không phải trạng thái artifact riêng.
- Thay đổi sau phê duyệt phải tăng phiên bản, đánh giá tác động và review/phê duyệt lại; phiên bản mới không tự kế thừa G2 cũ.

**Bằng chứng riêng của G2:** Trong [mẫu approval record chung](../../templates/review/approval-record.md), dẫn phiên bản design package, ADR liên quan và các xác nhận chuyên môn bắt buộc. Ghi riêng action không chặn và waiver hợp lệ theo policy; không dùng action mở để thay thế điều kiện gate. [Checklist G2](../../02-system-design/checklists/g2-design-approval-checklist.md) lưu tiêu chí và bằng chứng; package index tham chiếu approval record.
