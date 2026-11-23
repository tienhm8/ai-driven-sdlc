# Hợp đồng Đầu ra Planning
## Gói bàn giao
Stage 03 phải cung cấp: Product Backlog đã duyệt; Task Breakdown đã duyệt; Estimate đã review; Dependency Matrix đã review; DoD áp dụng được; Sprint/Delivery Plan đã duyệt khi có áp dụng; bản ghi phê duyệt G3.

## Trường tối thiểu của task
- ID/tiêu đề task duy nhất và Story/Epic cha.
- Requirement/AC và tham chiếu thiết kế liên quan.
- Mô tả, deliverable kỳ vọng, phương pháp nghiệm thu/kiểm chứng.
- Estimate, đơn vị, độ tin cậy, hoặc `Not estimated` kèm lý do.
- Dependency/blocker, vai trò owner, priority, tham chiếu DoD, trạng thái.

## Trạng thái
`Draft → In Review → Approved → Baselined → In Progress`
`Changes Requested` và `Rejected` là kết quả review. Chỉ artifact Approved/Baselined mới là baseline để thực thi.

## Truy vết
`Requirement/User Story → Thành phần Design/ADR → Backlog item → Task → Sprint/Milestone → Test/PR`

## Bàn giao cho Stage 04
Cung cấp danh sách task, priority, nghiệm thu/kiểm chứng, tham chiếu thiết kế, ràng buộc, dependency, estimate, sprint/milestone mục tiêu, DoD và bằng chứng phê duyệt G3. Stage 04 không được âm thầm mở rộng scope hoặc thay đổi thiết kế đã duyệt; phải gửi yêu cầu thay đổi tới owner/gate phù hợp.
