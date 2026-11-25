# G2 – System Design Approval

**Thời điểm:** Sau System Design, trước bàn giao chính thức sang Stage 03 Task Planning. Luồng: G2 → Stage 03 Task Planning → G3 → coding tại Stage 04.

**Approver:** Solution Architect; các phê duyệt chuyên môn bắt buộc theo phạm vi (như Security/Data) phải đầy đủ trước khi G2 Passed.

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

- **Decision:** `Approved / Approved with conditions / Changes requested / Rejected`; gate status: `Passed / Failed / Pending`.
- Chỉ `Approved`, sau khi đủ điều kiện gate và phê duyệt chuyên môn bắt buộc, mới cho phép G2 `Passed`. `Approved with conditions` giữ gate ở `Pending`, không cho phép bàn giao chính thức. Đóng điều kiện, lưu bằng chứng và trình Solution Architect xác nhận lại `Approved` cho phiên bản gói sau khi đóng điều kiện; thay đổi vượt phạm vi điều kiện phải review lại theo G2.
- Khi G2 `Passed`, Solution Architect chốt đúng phiên bản design package đã duyệt làm baseline. Stage 03 chỉ tiếp nhận phiên bản đã chốt cùng bằng chứng G2 hợp lệ cho phiên bản đó. Baseline là vai trò của phiên bản gói, không phải trạng thái artifact riêng.
- Thay đổi sau phê duyệt phải tăng phiên bản, đánh giá tác động và review/phê duyệt lại; phiên bản mới không tự kế thừa G2 cũ.

**Audit:** ID/phiên bản gói và artifact, quyết định và gate status, approver và các phê duyệt chuyên môn bắt buộc, bằng chứng review, điều kiện đã đóng hoặc waiver hợp lệ (nếu có), timestamp và tham chiếu hồ sơ G2. Xem checklist chi tiết tại `framework/02-system-design/checklists/g2-design-approval-checklist.md`.
