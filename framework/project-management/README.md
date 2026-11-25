# Project Management

Quản lý hồ sơ xuyên suốt SDLC: khởi tạo, baseline, theo dõi, thay đổi, rủi ro, issue, quyết định, phê duyệt và đóng dự án. PM điều phối; người có thẩm quyền ra quyết định. AI có thể soạn nháp nhưng không phê duyệt thay người.

## Nguồn chuẩn

| Nội dung | Nguồn chuẩn |
|---|---|
| ID, tên dự án, cấu hình platform và AI | Manifest `.ai-sdlc/project.yaml` của dự án; xem [mẫu manifest](../../platform/config-examples/project.yaml). Không duy trì thêm `structure.yml`. |
| Trạng thái vòng đời hiện tại | README PM của dự án, mục **Trạng thái dự án**. PM cập nhật và dẫn tới phê duyệt làm căn cứ; không sửa charter đã duyệt chỉ để đổi trạng thái. |
| Phạm vi, KPI, baseline và thẩm quyền | Charter đã duyệt hoặc hồ sơ baseline được charter dẫn tới, có phiên bản và bằng chứng phê duyệt. |
| Human Review Gates | [Gate Policy](../governance/human-review-gates/gate-policy.md) và yêu cầu riêng của từng Gate. [Approval Register](approval-register.md) chỉ dẫn đến hồ sơ review/audit, không cấp quyền. |
| Quyết định kiến trúc và dependency | [ADR của System Design](../02-system-design/templates/architecture-decision-record.md) và [Dependency Matrix của Task Planning](../03-task-planning/templates/dependency-matrix.md); không lập sổ PM song song. |
| Định danh | [ID Conventions](../standards/metadata/id-conventions.md). Giữ nguyên ID đã cấp; dùng chuẩn mới cho hồ sơ mới. |

## Mẫu hồ sơ

[Danh mục mẫu chuẩn](templates/README.md). Charter, Status và Closeout mỗi loại có một mẫu. Các sổ ở đây là mẫu chỉ mục; chi tiết nằm trong hồ sơ gốc được dẫn bằng ID/link.

## Khởi tạo và sử dụng

[`init-project.py`](../../platform/scripts/README.md) mặc định tạo `docs/project-management/` gồm:

- `README.md`: ghi trạng thái ban đầu `proposed` và dẫn tới nguồn chuẩn, mẫu hồ sơ.
- [workflow.md](workflow.md): hướng dẫn quản lý dự án, gồm thủ tục tạm dừng (`on_hold`) và tiếp tục (`active`).
- `project-charter.md`: bản làm việc `Draft` từ mẫu charter. PM bổ sung scope, KPI, baseline, người có thẩm quyền và ngưỡng escalation trước khi trình duyệt.
- Các chỉ mục `No entries`: [change](change-log.md), [risk](risk-register.md), [issue](issue-log.md), [decision](decision-log.md), [approval](approval-register.md), [meeting notes](meeting-notes.md). Bỏ dòng `No entries` khi ghi mục đầu tiên, không tạo bản ghi giả.
- `_templates/`: bản sao các mẫu; tạo báo cáo theo kỳ trong `project-status/`, hồ sơ đóng trong `project-closeout/` và bản ghi chi tiết trong thư mục tương ứng.

Risk là sự kiện có thể xảy ra; issue là vấn đề đã xảy ra. Nếu risk trở thành issue, liên kết hai ID. Báo cáo trạng thái, biên bản họp và closeout chỉ tóm tắt và dẫn về hồ sơ gốc. Biên bản họp không thay phê duyệt.

**Dự án đã khởi tạo:** init không sửa hồ sơ đang có. Khi chuyển từ `structure.yml`, giữ cấu hình platform trong manifest và chuyển dữ liệu quản trị còn dùng (scope, KPI, baseline, thẩm quyền) sang charter hoặc hồ sơ được charter dẫn tới. Chuyển trạng thái hiện tại và căn cứ phê duyệt sang README PM của dự án. Giữ bản đã duyệt và ID cũ để đối chiếu; ngừng cập nhật `structure.yml` như nguồn song song.
