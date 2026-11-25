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

## Thay đổi sau G3

Không sửa trực tiếp baseline đã duyệt. **Tech Lead** ghi phân loại và đánh giá tác động trong [planning change log](../templates/planning-change-log.md), kèm phiên bản liên quan và tham chiếu bản ghi G3 hiện hành.

- **Trọng yếu:** thay đổi phạm vi task, tiêu chí nghiệm thu/DoR/DoD áp dụng, ưu tiên, baseline nguồn, hoặc estimate/dependency làm thay đổi lịch, nguồn lực hay rủi ro đã duyệt. Mọi thay đổi nội dung không đáp ứng điều kiện đính chính bên dưới đều phải qua G3 lại nếu muốn áp dụng, kể cả thay đổi estimate không làm đổi lịch. Nếu chưa đủ bằng chứng để phân loại, xử lý như thay đổi trọng yếu. Tạo phiên bản kế hoạch mới và duyệt lại G3 trước khi bàn giao phiên bản mới; chặn các task bị ảnh hưởng cho đến khi có quyết định hợp lệ.
- **Không trọng yếu:** sửa lỗi chính tả, định dạng hoặc liên kết trỏ tới cùng artifact/phiên bản, không đổi nghĩa hay quyết định đã duyệt. Lập [bản đính chính](../templates/planning-correction.md) có ID và phiên bản riêng, ghi nội dung thay đổi, lý do Tech Lead xác nhận không trọng yếu và link đến G3 hiện hành; gửi kèm gói bàn giao để Stage 04 sử dụng. Không cần quyết định G3 mới cho bản đính chính vì baseline thực thi và phạm vi vẫn giữ nguyên. Nếu muốn thay baseline bằng một phiên bản kế hoạch khác, phiên bản đó phải có G3 `Approved` riêng theo gate policy.
- **Chỉ cập nhật tiến độ:** ghi trong tracker riêng, không đổi baseline và không cần duyệt lại.

## Truy vết
`Requirement/User Story → Thành phần Design/ADR → Backlog item → Task → Sprint/Milestone`; mỗi task nêu cách kiểm chứng cần thực hiện. Liên kết PR và test case được bổ sung ở Stage 04–06.

## Bàn giao cho Stage 04
Gói bàn giao ghi: ID và phiên bản baseline kế hoạch đã chốt, bằng chứng G3 `Approved` cho đúng phiên bản, **phạm vi task được G3 duyệt**, danh sách task kèm priority, nghiệm thu/kiểm chứng, tham chiếu thiết kế, ràng buộc, dependency, estimate, sprint/milestone mục tiêu, DoR và DoD áp dụng.
Nếu có bản đính chính không trọng yếu, ghi link và phiên bản bản đính chính riêng với phiên bản baseline.

Stage 04 xác minh (không duyệt lại) phiên bản, phạm vi và DoR bằng [development readiness checklist](../../04-development/checklists/development-readiness.md). Stage 04 không âm thầm mở rộng scope hoặc thay đổi thiết kế đã duyệt; phải gửi yêu cầu thay đổi tới owner/gate phù hợp.
