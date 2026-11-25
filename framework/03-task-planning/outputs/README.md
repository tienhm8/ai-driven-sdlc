# Outputs Stage 03
Thư mục framework chỉ lưu output contract; artifact dự án thực tế nằm tại `projects/<Project>/docs/03-task-planning/`.

Danh mục đầu ra chuẩn, mức bắt buộc/khi áp dụng/tham chiếu, trạng thái và bàn giao: xem [Output Contract](planning-output-contract.md). Bảng dưới chỉ ánh xạ artifact sang template.

| Artifact | Template nguồn | Người dùng |
|---|---|---|
| Product Backlog | templates/product-backlog.md | PO, PM, Stage 04 |
| Task Breakdown/WBS | templates/task-breakdown.md | Tech Lead, Developer |
| Effort Estimation | templates/effort-estimation.md | PM, Tech Lead |
| Dependency Matrix | templates/dependency-matrix.md | PM, Tech Lead |
| Definition of Done | templates/definition-of-done.md hoặc chuẩn tổ chức | Dev, Review, QA |
| Sprint/Delivery Plan (khi áp dụng) | templates/sprint-plan.md | Team |
| Bản ghi phê duyệt G3 | [Mẫu approval record chung](../../templates/review/approval-record.md); checklist G3 là bằng chứng | Workflow/approval engine |

Cấu trúc thư mục dự án đề xuất:
```text
docs/03-task-planning/
  README.md
  input-register.md
  product-backlog.md
  task-breakdown.md
  effort-estimation.md
  dependency-matrix.md
  definition-of-ready.md  # Tiêu chí tham chiếu
  definition-of-done.md
  sprint-plan.md
  planning-review.md
  g3-approval.md
```
Mỗi artifact cần có project, ID, version, trạng thái, owner, ngày cập nhật và baseline nguồn. Bản nháp do AI tạo không phải là baseline đã duyệt.

## Kiến trúc
Thư mục outputs định nghĩa **những gì Stage 03 phải bàn giao** và **ai nhận**:

```text
Templates (soạn) → Artifact dự án (docs/03-task-planning/)
                 → Review bằng Checklists
                 → G3 Approval → Gói bàn giao → Stage 04
```

Quy tắc trạng thái, version và thay đổi sau G3: xem Output Contract.

## Vai trò từng file
| File | Vai trò |
|---|---|
| `README.md` | Bảng artifact bắt buộc/tùy chọn, template nguồn, người dùng và cấu trúc thư mục dự án đề xuất. |
| `planning-output-contract.md` | Hợp đồng đầu ra: gói bàn giao, trường tối thiểu của task, vòng đời trạng thái, chuỗi truy vết và quy tắc bàn giao cho Stage 04. |
