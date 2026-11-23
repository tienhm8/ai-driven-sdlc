# Outputs Stage 03
Thư mục framework chỉ lưu output contract; artifact dự án thực tế nằm tại `projects/<Project>/docs/03-task-planning/`.

| Output artifact | Nguồn | Bắt buộc | Người dùng |
|---|---|---|---|
| Product Backlog | templates/product-backlog.md | Có | PO, PM, Stage 04 |
| Task Breakdown/WBS | templates/task-breakdown.md | Có | Tech Lead, Developer |
| Effort Estimation | templates/effort-estimation.md | Có | PM, Tech Lead |
| Dependency Matrix | templates/dependency-matrix.md | Có | PM, Tech Lead |
| Definition of Done | templates/definition-of-done.md hoặc tham chiếu chuẩn của tổ chức | Có | Dev, Review, QA |
| Sprint/Delivery Plan | templates/sprint-plan.md | Nếu áp dụng mô hình sprint; nếu không thì dùng kế hoạch giao hàng tương đương | Team |
| Bản ghi phê duyệt G3 | checklists/g3-planning-approval-checklist.md | Có | Workflow/approval engine |

Cấu trúc thư mục dự án đề xuất:
```text
docs/03-task-planning/
  README.md
  input-register.md
  product-backlog.md
  task-breakdown.md
  effort-estimation.md
  dependency-matrix.md
  definition-of-done.md
  sprint-plan.md
  planning-review.md
  g3-approval.md
```
Mỗi artifact cần có project, ID, version, trạng thái, owner, ngày cập nhật và baseline nguồn. Bản nháp do AI tạo không phải là baseline đã duyệt. Mọi thay đổi sau G3 cần version mới và change log.

## Kiến trúc
Thư mục outputs định nghĩa **những gì Stage 03 phải bàn giao** và **ai nhận**:

```text
Templates (soạn) → Artifact dự án (docs/03-task-planning/)
                 → Review bằng Checklists
                 → G3 Approval → Gói bàn giao → Stage 04
```

Artifact chỉ trở thành baseline thực thi khi đạt trạng thái Approved/Baselined. Thay đổi sau G3 cần version mới và change log.

## Vai trò từng file
| File | Vai trò |
|---|---|
| `README.md` | Bảng artifact bắt buộc/tùy chọn, template nguồn, người dùng và cấu trúc thư mục dự án đề xuất. |
| `planning-output-contract.md` | Hợp đồng đầu ra: gói bàn giao, trường tối thiểu của task, vòng đời trạng thái, chuỗi truy vết và quy tắc bàn giao cho Stage 04. |
