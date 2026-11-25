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
| DoR | Tham chiếu | [Tiêu chí tối thiểu của framework](../templates/definition-of-ready.md), kèm yêu cầu bổ sung của dự án/tổ chức nếu có |
| Test case / PR | Ngoài Stage 03 | Liên kết ở các stage thực hiện; Stage 03 chỉ lập task kiểm chứng |

## Trường tối thiểu của task
- ID/tiêu đề task duy nhất (ví dụ `TASK-0001`) và Story/Epic cha.
- Requirement/AC và tham chiếu thiết kế liên quan.
- Mô tả, deliverable kỳ vọng, phương pháp nghiệm thu/kiểm chứng.
- Estimate, đơn vị, độ tin cậy, hoặc `Not estimated` kèm lý do.
- Dependency/blocker, vai trò owner, priority, tham chiếu DoD, trạng thái.

## Trạng thái
Artifact planning: `Draft → In Review → Approved → Superseded`.
- `Approved`: đã có quyết định phê duyệt G3 cho đúng phiên bản.
- **Baseline** là phiên bản kế hoạch đã chốt để thực thi: PM/Delivery Lead ghi đúng phiên bản có G3 `Approved` và phạm vi task tương ứng vào gói bàn giao. Baseline không phải trạng thái của artifact.
- `Changes Requested`, `Rejected` và `Blocked` là kết quả tại gate, không phải trạng thái vòng đời của artifact.

Theo dõi trạng thái của từng backlog item (`Proposed / Ready / Committed / Done`) riêng với trạng thái artifact planning; `Ready` trong backlog không thay kết quả Development Readiness.

Không sửa trực tiếp baseline đã duyệt. Thay đổi nội dung kế hoạch cần phiên bản mới, changelog và đánh giá tác động. Thay đổi trọng yếu cần review/phê duyệt lại G3; phiên bản mới không tự kế thừa approval. Với sửa đổi không trọng yếu, tiếp tục dùng baseline hiện hành nếu vẫn áp dụng; không thay phiên bản bàn giao bằng bản sửa chưa được G3 duyệt. Cập nhật trạng thái thực thi trong tracker riêng không đổi baseline và không cần duyệt lại.

## Truy vết
`Requirement/User Story → Thành phần Design/ADR → Backlog item → Task → Sprint/Milestone`; mỗi task nêu cách kiểm chứng cần thực hiện. Liên kết PR và test case được bổ sung ở Stage 04–06.

## Bàn giao cho Stage 04
Gói bàn giao ghi: ID và phiên bản baseline kế hoạch đã chốt, bằng chứng G3 `Approved` cho đúng phiên bản, **phạm vi task được G3 duyệt**, danh sách task kèm priority, nghiệm thu/kiểm chứng, tham chiếu thiết kế, ràng buộc, dependency, estimate, sprint/milestone mục tiêu, DoR và DoD áp dụng.
Stage 04 xác minh (không duyệt lại) phiên bản, phạm vi và DoR bằng [development readiness checklist](../../04-development/checklists/development-readiness.md). Stage 04 không âm thầm mở rộng scope hoặc thay đổi thiết kế đã duyệt; phải gửi yêu cầu thay đổi tới owner/gate phù hợp.
