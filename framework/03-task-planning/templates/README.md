# Templates Stage 03

## Kiến trúc
Templates là biểu mẫu để tạo artifact planning cho từng dự án. Artifact thực tế được lưu tại `projects/<Project>/docs/03-task-planning/`; thư mục framework chỉ giữ biểu mẫu.

Luồng dữ liệu giữa các template:

```text
Requirement/Design baseline (inputs)
  → Product Backlog → Task Breakdown/WBS → Effort Estimation
  → Dependency Matrix → Definition of Done
  → Sprint Plan → (checklists review) → G3 → Stage 04
```

## Vai trò từng file
| File | Vai trò | Đầu ra cho |
|---|---|---|
| `product-backlog.md` | Danh sách Epic/Story/Task đã ưu tiên, kèm trạng thái Ready và nhật ký thay đổi. Priority tách biệt với estimate. | PO, PM, Stage 04 |
| `task-breakdown.md` | WBS phân rã Story thành task có thể kiểm chứng, truy vết về requirement và design. | Tech Lead, Developer |
| `effort-estimation.md` | Ước lượng effort theo task, đơn vị, độ tin cậy và giả định; tổng hợp theo hạng mục. | PM, Tech Lead |
| `dependency-matrix.md` | Dependency nội bộ và bên ngoài, critical path, rủi ro và owner xử lý. | PM, Tech Lead |
| `definition-of-done.md` | Tiêu chí hoàn thành áp dụng cho task/story/sprint/release, kèm ghi nhận ngoại lệ. | Dev, Review, QA |
| [Definition of Ready](definition-of-ready.md) | Tiêu chí tối thiểu để chuẩn bị và xác minh readiness từng task; không thay G3. | Tech Lead, Developer |
| `sprint-plan.md` | Sprint goal, capacity, cam kết, cột mốc, rủi ro và xác nhận của PO/PM/Tech Lead hoặc team. | Team |

## Quy ước dùng chung
- Mọi file có ID, phiên bản, trạng thái, owner và ngày cập nhật.
- Không cộng story points với giờ/ngày.
- Dữ liệu trong ngoặc như `Yes/No`, `Open/Resolved` là giá trị chọn sẵn; giữ nguyên để dễ tổng hợp.
