# Hợp đồng Đầu ra Planning
Nguồn chuẩn cho **đầu ra và bàn giao** của Stage 03. Trình tự xem [workflow](../workflow.md); thẩm quyền và bằng chứng G3 xem [gate policy](../../governance/human-review-gates/gate-policy.md).

## Danh mục đầu ra
| Mục | Mức | Ghi chú |
|---|---|---|
| Product Backlog | Bắt buộc | |
| Task Breakdown/WBS | Bắt buộc | Gồm task kỹ thuật, test, security, migration, tài liệu, rollout khi cần |
| Estimate | Bắt buộc | Đã review |
| Dependency Matrix | Bắt buộc | |
| DoD áp dụng được | Bắt buộc | Có thể tham chiếu chuẩn tổ chức |
| Bản ghi phê duyệt G3 | Bắt buộc | Theo checklist G3 và mẫu approval record chung |
| Sprint/Delivery Plan | Khi áp dụng | Chứa capacity, milestone, roadmap; không cần file riêng cho từng mục |
| Technical Backlog | Khi áp dụng | Có thể nằm trong Task Breakdown |
| Risk Register | Tham chiếu | Dùng sổ rủi ro của dự án; chỉ ghi rủi ro delivery mới và liên kết |
| DoR | Tham chiếu | Chuẩn dự án/tổ chức; Stage 04 xác minh từng task |
| Test case / PR | Ngoài Stage 03 | Liên kết ở các stage thực hiện; Stage 03 chỉ lập task kiểm chứng |

## Trường tối thiểu của task
- ID/tiêu đề task duy nhất (ví dụ `TASK-0001`) và Story/Epic cha.
- Requirement/AC và tham chiếu thiết kế liên quan.
- Mô tả, deliverable kỳ vọng, phương pháp nghiệm thu/kiểm chứng.
- Estimate, đơn vị, độ tin cậy, hoặc `Not estimated` kèm lý do.
- Dependency/blocker, vai trò owner, priority, tham chiếu DoD, trạng thái.

## Trạng thái
Artifact planning: `Draft → In Review → Approved → Baselined → Superseded`.
- `Approved`: đã có quyết định phê duyệt G3 cho đúng phiên bản.
- `Baselined`: phiên bản đã chốt để bàn giao sang Stage 04; handoff ghi rõ phiên bản này.
- Chỉ phiên bản `Baselined` (đã `Approved`) là baseline thực thi.
- `Changes Requested` và `Rejected` là kết quả review, không phải trạng thái vòng đời.

Trạng thái thực thi của task (`Planned / Blocked / In Progress / Done`) theo dõi riêng trong backlog; không phải trạng thái artifact planning.

Thay đổi sau G3 cần version mới và change log; thay đổi trọng yếu cần phê duyệt G3 mới cho phiên bản đó.

## Truy vết
`Requirement/User Story → Thành phần Design/ADR → Backlog item → Task → Sprint/Milestone`; mỗi task nêu cách kiểm chứng cần thực hiện. Liên kết PR và test case được bổ sung ở Stage 04–06.

## Bàn giao cho Stage 04
Gói bàn giao ghi: ID và version kế hoạch `Baselined`, **phạm vi task được G3 duyệt**, danh sách task kèm priority, nghiệm thu/kiểm chứng, tham chiếu thiết kế, ràng buộc, dependency, estimate, sprint/milestone mục tiêu, DoD và bằng chứng G3.
Stage 04 xác minh (không duyệt lại) phiên bản, phạm vi và DoR bằng [development readiness checklist](../../04-development/checklists/development-readiness.md). Stage 04 không âm thầm mở rộng scope hoặc thay đổi thiết kế đã duyệt; phải gửi yêu cầu thay đổi tới owner/gate phù hợp.
