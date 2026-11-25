# Project Management

Quản lý hồ sơ xuyên suốt SDLC: khởi tạo, baseline, theo dõi, thay đổi, rủi ro, issue, quyết định, phê duyệt và đóng dự án. PM điều phối; người có thẩm quyền ra quyết định. AI có thể soạn nháp nhưng không phê duyệt thay người.

## Nguồn chuẩn

| Nội dung | Nguồn chuẩn |
|---|---|
| ID, tên dự án, cấu hình platform và AI | Manifest `.ai-sdlc/project.yaml` của dự án; xem [ví dụ manifest](#ví-dụ-manifest). Không duy trì thêm `structure.yml`. |
| Trạng thái vòng đời hiện tại | README PM của dự án, mục **Trạng thái dự án**. PM cập nhật và dẫn tới phê duyệt làm căn cứ; không sửa charter đã duyệt chỉ để đổi trạng thái. |
| Phạm vi, KPI, baseline và thẩm quyền | Charter đã duyệt hoặc hồ sơ baseline được charter dẫn tới, có phiên bản và bằng chứng phê duyệt. |
| Human Review Gates | [Gate Policy](../governance/human-review-gates/gate-policy.md) và yêu cầu riêng của từng Gate. [Approval Register](approval-register.md) chỉ dẫn đến hồ sơ review/audit, không cấp quyền. |
| Quyết định kiến trúc và dependency | [ADR của System Design](../02-system-design/templates/architecture-decision-record.md) và [Dependency Matrix của Task Planning](../03-task-planning/templates/dependency-matrix.md); không lập sổ PM song song. |
| Định danh | [ID Conventions](../standards/metadata/id-conventions.md). Giữ nguyên ID đã cấp; dùng chuẩn mới cho hồ sơ mới. |

## Mẫu hồ sơ

[Danh mục mẫu chuẩn](templates/README.md). Charter, Status và Closeout mỗi loại có một mẫu. Các sổ ở đây là mẫu chỉ mục; chi tiết nằm trong hồ sơ gốc được dẫn bằng ID/link.

## Khởi tạo và sử dụng

Từ gốc repo, dùng Python 3.10 trở lên và cài platform trước khi khởi tạo:

```bash
python3 -m pip install -e ./platform
python3 platform/scripts/init-project.py --name "Project CRM" --slug Project-CRM
```

Lệnh tạo `projects/Project-CRM/`; bên trong, `docs/project-management/` mặc định gồm:

- `README.md`: ghi trạng thái ban đầu `proposed` và dẫn tới nguồn chuẩn, mẫu hồ sơ.
- [workflow.md](workflow.md): hướng dẫn quản lý dự án, gồm thủ tục tạm dừng (`on_hold`) và tiếp tục (`active`).
- `project-charter.md`: bản làm việc `Draft` từ mẫu charter. PM bổ sung scope, KPI, baseline, người có thẩm quyền và ngưỡng escalation trước khi trình duyệt.
- Các chỉ mục `No entries`: [change](change-log.md), [risk](risk-register.md), [issue](issue-log.md), [decision](decision-log.md), [approval](approval-register.md), [meeting notes](meeting-notes.md). Bỏ dòng `No entries` khi ghi mục đầu tiên, không tạo bản ghi giả.
- `_templates/`: bản sao các mẫu; tạo báo cáo theo kỳ trong `project-status/`, hồ sơ đóng trong `project-closeout/` và bản ghi chi tiết trong thư mục tương ứng.

Risk là sự kiện có thể xảy ra; issue là vấn đề đã xảy ra. Nếu risk trở thành issue, liên kết hai ID. Báo cáo trạng thái, biên bản họp và closeout chỉ tóm tắt và dẫn về hồ sơ gốc. Biên bản họp không thay phê duyệt.

### Ví dụ manifest

Init tạo `.ai-sdlc/project.yaml` đầy đủ. Ví dụ dưới đây chỉ trích các trường liên quan đến định danh và PM; không dùng đoạn này để thay cả manifest:

```yaml
project:
  id: Project-CRM
  name: Project CRM
project_management:
  enabled: true
  path: docs/project-management
```

### Bổ sung hồ sơ cho dự án đã khởi tạo

Không chạy lại init trên thư mục dự án cũ: lệnh từ chối nếu dự án đã tồn tại. Các bước sau áp dụng cả khi **không có** `structure.yml`. Thực hiện trong `docs/project-management/` của dự án (hoặc đường dẫn PM đã cấu hình trong manifest):

1. Giữ nguyên hồ sơ đã duyệt và ID đã cấp. Trong `README.md`, thêm ba mục `## Trạng thái dự án`, `## Nguồn chuẩn` và `## Mẫu hồ sơ` để các liên kết trong workflow và register hoạt động. Ghi trạng thái hiện tại và ID/link phê duyệt làm căn cứ từ hồ sơ thực tế; nếu chưa xác minh được, ghi rõ cần xác minh thay vì đặt lại thành `proposed`. Ở hai mục còn lại, dẫn đến manifest, charter, Gate Policy, ID Conventions và danh mục mẫu `_templates/README.md` bằng đường dẫn tính từ README dự án.
2. Bổ sung `workflow.md` nếu chưa có; nếu đã có, đối chiếu [workflow framework](workflow.md) và tích hợp quy tắc mới vào bản dự án thay vì ghi đè. Nếu chưa có charter, sao chép [mẫu charter](templates/project-charter-template.md) thành `project-charter.md`, điền dữ liệu đã xác minh và trình duyệt theo workflow. Nếu charter đã tồn tại, dùng lại và liên kết đúng phiên bản.
3. Bổ sung các register còn thiếu bằng các mẫu `No entries` ở trên; nếu đã có dữ liệu, giữ register hoặc liên kết tới nguồn hiện có và không thêm `No entries` giả. Bổ sung từng mẫu còn thiếu từ [danh mục mẫu](templates/README.md) vào `_templates/`. Với `_templates/approval-record-template.md`, dùng nội dung [mẫu approval chung](../templates/review/approval-record.md), không sao chép file chỉ dẫn của framework. Kiểm tra các link từ README, workflow và register sau khi bổ sung.
4. Nếu từng dùng `structure.yml`, giữ bản cũ để đối chiếu rồi ngừng cập nhật như nguồn song song. Đưa cấu hình platform vào manifest, scope/KPI/baseline/thẩm quyền vào charter hoặc hồ sơ được charter dẫn tới, và trạng thái hiện tại vào README PM.
