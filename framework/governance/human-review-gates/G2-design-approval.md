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

- **Decision:** `Approved / Changes Requested / Rejected / Blocked`, theo lifecycle trong `gate-policy.md`. Chỉ `Approved`, sau khi đủ điều kiện gate và phê duyệt chuyên môn bắt buộc, mới hoàn tất G2.
- Nếu còn điều kiện cần đóng, ghi `Changes Requested` thay vì `Approved with conditions`; thiếu đầu vào, bằng chứng hoặc phê duyệt bắt buộc thì ghi `Blocked`. Cả hai chặn bàn giao chính thức. Trong approval engine, quyết định được lưu lần lượt là `changes_requested` hoặc `blocked`; kết quả tổng hợp có thể hiển thị `blocked` với bất kỳ quyết định không phê duyệt nào, còn khi chưa đủ approval engine có thể hiển thị `awaiting_approval`. Đóng điều kiện, lưu bằng chứng và trình Solution Architect phê duyệt lại phiên bản gói sau khi đóng điều kiện; thay đổi vượt phạm vi điều kiện phải review lại theo G2.
- Khi G2 `Approved`, Solution Architect chốt đúng phiên bản design package đã duyệt làm baseline. Stage 03 chỉ tiếp nhận phiên bản đã chốt cùng bằng chứng G2 hợp lệ cho phiên bản đó. Baseline là vai trò của phiên bản gói, không phải trạng thái artifact riêng.
- Thay đổi sau phê duyệt phải tăng phiên bản, đánh giá tác động và review/phê duyệt lại; phiên bản mới không tự kế thừa G2 cũ.

**Audit:** Dùng `framework/templates/review/approval-record.md` theo gate policy để ghi ID/phiên bản gói và artifact, quyết định và gate status, approver và các phê duyệt chuyên môn bắt buộc, bằng chứng review và timestamp. Ghi riêng action không chặn và waiver hợp lệ theo policy; không dùng action mở để thay thế điều kiện gate. Checklist `framework/02-system-design/checklists/g2-design-approval-checklist.md` lưu tiêu chí và bằng chứng; package index tham chiếu approval record.
