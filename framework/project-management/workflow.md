# Project Management Workflow

## 1. Initiate
Sponsor bảo trợ và chỉ định PM; PO xác nhận nhu cầu nghiệp vụ. PM lập charter ở trạng thái `Draft`, tham chiếu manifest thay vì sao chép cấu hình. Sponsor **và** PO đều phê duyệt đúng phiên bản charter trước khi PM chuyển trạng thái từ `proposed` sang `active` trong mục **Trạng thái dự án** của README PM và dẫn tới phê duyệt charter. Không sửa bản charter đã duyệt để cập nhật trạng thái.

## 2. Establish baseline
PM đề xuất baseline (scope, KPI, deliverables, milestones, lịch, ngân sách) và liên kết requirement, design, backlog, repository. Sponsor **và** PO duyệt baseline ban đầu, trong charter hoặc hồ sơ có phiên bản được charter dẫn tới. Điền ma trận thẩm quyền và ngưỡng escalation trước khi duyệt charter; nếu một ngưỡng chưa được duyệt thì không suy diễn quyền ủy nhiệm.

## 3. Execute and monitor
PM cập nhật báo cáo theo kỳ bằng [mẫu trạng thái](README.md#mẫu-hồ-sơ). Milestone lấy từ baseline; trạng thái Gate được báo cáo riêng và dẫn đến review/audit. G7 chỉ ghi nếu có incident nghiêm trọng kích hoạt. Chỉ tóm tắt rủi ro, vấn đề và quyết định; dẫn về hồ sơ gốc bằng ID/link.

### Tạm dừng và tiếp tục
PM đề xuất chuyển `active` → `on_hold` hoặc `on_hold` → `active` và ghi rõ lý do, phạm vi ảnh hưởng và điều kiện tiếp tục. Sponsor **và** PO phải phê duyệt từng quyết định. Chỉ sau khi đủ phê duyệt, PM cập nhật mục **Trạng thái dự án** trong README PM và ghi ID/link phê duyệt quản trị tương ứng. Tiếp tục dự án không thay cho phê duyệt Gate hay phê duyệt lại baseline khi có thay đổi.

## 4. Change control
Người đề xuất tạo change request. PM điều phối đánh giá tác động scope, lịch, chi phí, chất lượng, kiến trúc, bảo mật và vận hành. Trước khi trình duyệt, người phụ trách từng lĩnh vực bị ảnh hưởng phải đánh giá và ghi kết luận cùng bằng chứng trong change request hoặc hồ sơ được dẫn tới. Trong ngưỡng, chỉ người được charter ủy quyền mới được duyệt. Vượt ngưỡng, thiếu ủy quyền hoặc tranh chấp thẩm quyền thì PM trình Sponsor **và** PO, không sửa baseline trước khi đủ phê duyệt. Ghi ID, lý do, phiên bản và bằng chứng trong [Change Log](change-log.md) và liên kết hồ sơ phê duyệt. Phê duyệt quản trị không thay Gate hoặc yêu cầu review lại của Gate Policy.

## 5. Risk and issue
Risk là sự kiện chưa chắc chắn; issue là vấn đề đã xảy ra. Mỗi mục có owner, next action, hạn, trạng thái và escalation khi cần. Khi risk xảy ra, tạo issue và liên kết hai ID. Dẫn hồ sơ chi tiết từ [Risk Register](risk-register.md) hoặc [Issue Log](issue-log.md).

## 6. Decision and approval
[Decision Log](decision-log.md) chỉ ghi quyết định quản trị và dẫn đến ADR nếu liên quan tới kiến trúc. [Approval Register](approval-register.md) chỉ dẫn về hồ sơ gốc: phê duyệt quản trị theo charter hoặc review/audit theo [Gate Policy](README.md#nguồn-chuẩn). Biên bản họp và nội dung AI tạo không phải phê duyệt.

## 7. Escalation
PM chuyển cấp theo ngưỡng scope/lịch/chi phí ghi trong charter và khi có risk High/Critical, tranh chấp thẩm quyền, vấn đề compliance/security, hoặc Gate/milestone có nguy cơ trễ. Ghi ai nhận, thời điểm, quyết định và hành động tiếp theo. Escalation không thay cho phê duyệt bắt buộc.

## 8. Closeout
PM đề xuất trạng thái và lập báo cáo theo [mẫu closeout](README.md#mẫu-hồ-sơ):

- `completed`: dẫn bằng chứng nghiệm thu deliverables đã cam kết và xác nhận bàn giao.
- `cancelled`: có thể đề xuất từ `active` hoặc `on_hold`, không cần kích hoạt lại dự án. Ghi quyết định/lý do hủy, hạng mục chưa hoàn thành hoặc chưa nghiệm thu, và người nhận các nghĩa vụ/rủi ro còn lại. Không yêu cầu nghiệm thu phần chưa hoàn tất.

Trước khi trình duyệt `completed` hoặc `cancelled`, PM đối chiếu Risk Register và Issue Log. Mỗi mục còn mở phải được xử lý hoặc có người được chỉ định xác nhận tiếp quản. Báo cáo ghi ID và bằng chứng xử lý; nếu bàn giao, ghi thêm người nhận, hạn xem xét và bằng chứng xác nhận tiếp quản. Sau khi Sponsor **và** PO phê duyệt đúng phiên bản báo cáo, PM cập nhật mục **Trạng thái dự án** trong README PM, dẫn tới phê duyệt closeout và lưu trữ theo retention policy. Giữ nguyên baseline và phê duyệt lịch sử.
