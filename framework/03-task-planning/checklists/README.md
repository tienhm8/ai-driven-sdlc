# Checklists Stage 03

## Kiến trúc
Checklist là điểm kiểm soát chất lượng tại từng bước của planning, theo thứ tự:

1. **Sẵn sàng đầu vào** (`planning-readiness-checklist.md`): trước khi bắt đầu lập kế hoạch.
2. **Review estimate** (`estimation-review-checklist.md`): sau khi AI đề xuất estimate.
3. **Review dependency** (`dependency-review-checklist.md`): sau khi lập dependency matrix.
4. **Phê duyệt G3** (`g3-planning-approval-checklist.md`): gate cuối trước khi Stage 04 được phép code.

Checklist chỉ ghi nhận kết quả kiểm tra. Người review (PM/Tech Lead/PO) quyết định kết quả; AI không tự đánh dấu hoàn thành hay tự phê duyệt.

## Vai trò từng file
| File | Vai trò | Người dùng chính |
|---|---|---|
| `planning-readiness-checklist.md` | Kiểm tra baseline G1/G2, scope, NFR, capacity và open questions trước khi planning. Kết quả: Ready / Ready with conditions / Not ready. | PM, Tech Lead |
| `estimation-review-checklist.md` | Kiểm tra đơn vị, phương pháp, giả định, độ tin cậy và phần dự phòng của estimate. Kết quả: Accepted / Re-estimate / Spike required. | PM, Tech Lead, người ước lượng |
| `dependency-review-checklist.md` | Kiểm tra dependency có owner, lead time, critical path và biện pháp giảm thiểu. Kết quả: Accepted / Changes Requested. | PM, Tech Lead |
| `g3-planning-approval-checklist.md` | Điều kiện của gate G3 và bảng ghi quyết định phê duyệt. Không có `Approved` kèm bằng chứng thì Stage 04 không được bắt đầu. | Tech Lead (phê duyệt), PO/PM (xác nhận scope, priority, lịch) |
