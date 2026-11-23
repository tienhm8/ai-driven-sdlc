# 03 — Task Planning
Mục đích: chuyển requirement/design baseline đã duyệt thành backlog, task breakdown, estimate, dependency và delivery plan. AI đề xuất; PM/Tech Lead review; G3 do con người phê duyệt.

## Cấu trúc
- `inputs/`: tham chiếu baseline từ Stage 01 và 02, không mặc định sao chép tài liệu gốc.
- `templates/`: biểu mẫu để tạo planning artifacts cho từng dự án.
- `checklists/`: kiểm tra readiness, estimate, dependency và G3.
- `outputs/`: hợp đồng đầu ra và quy tắc bàn giao cho Stage 04.

## Inputs
1. Stage 01: scope, Epic/User Story, FR/NFR, business rules, Acceptance Criteria, assumptions/open questions; trạng thái Approved và có bằng chứng G1.
2. Stage 02: architecture, components, API, database, data flow, ADR, technical constraints; trạng thái Approved và có bằng chứng G2.
3. Project context: team/roles, capacity, calendar, release target, estimation policy.

Thiếu baseline hoặc blocker thì dừng phần kế hoạch bị ảnh hưởng, ghi owner và hạn xử lý. Không biến giả định AI thành fact.

## Workflow
1. Validate inputs và G1/G2.
2. Phân rã Epic/Story thành deliverable/task.
3. Ước lượng effort, unit, confidence, assumptions.
4. Xác định dependency, sequencing, risk.
5. Sắp xếp backlog theo value/risk/priority.
6. Lập sprint/release plan theo capacity.
7. Chạy checklist, PM/Tech Lead review.
8. Lưu version, change log và approval G3.
9. Bàn giao outputs đã duyệt cho Stage 04.

## Quy ước
- ID: `EPIC-xxx`, `US-xxx`, `TASK-xxx`, `DEP-xxx`, `SPRINT-xxx`.
- Không trộn giờ/ngày/story point trong cùng một tổng.
- Priority khác estimate.
- Task phải trace về Requirement/Story và Design khi phù hợp.
- G3 là human gate; AI không tự approve hoặc tự cho phép coding.
- L1: format/validate; L2: đề xuất breakdown/estimate; L3: human review bắt buộc; L4: con người quyết định scope, resource trade-off và release commitment.

## Project artifacts
Lưu tại `projects/<Project>/docs/03-task-planning/`; framework dùng chung chỉ chứa templates, checklist và output contract.
