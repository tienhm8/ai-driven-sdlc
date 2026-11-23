# Project Management Workflow

## 1. Initiate
Sponsor/PO nêu business need và chỉ định PM. PM lập charter, xác định mục tiêu, phạm vi, deliverables, stakeholders, giả định và ràng buộc. Cập nhật `structure.yml`. Sponsor/PO phê duyệt; chỉ sau đó chuyển project sang `active`.

## 2. Establish baseline
Xác định delivery approach, milestones, nguồn lực, cadence và success criteria. Liên kết requirement, design, backlog, repository. Tạo register ban đầu; ghi `No entries` nếu chưa phát sinh.

## 3. Execute and monitor
PM cập nhật status theo cadence. Change vào `change-log.md`; risk vào `risk-register.md`; vấn đề đã xảy ra vào `issue-log.md`; quyết định vào `decision-log.md`; phê duyệt vào `approval-register.md`; cuộc họp/action items vào `meeting-notes.md`.

## 4. Change control
Người đề xuất tạo request theo template. PM điều phối impact assessment (scope, schedule, cost, quality, architecture, security, operations). Owner chuyên môn đánh giá; người có thẩm quyền phê duyệt/từ chối. Chỉ cập nhật baseline sau approval; lưu ID, lý do và bằng chứng.

## 5. Risk and issue
Risk là sự kiện chưa chắc chắn; issue là vấn đề đã xảy ra. Mỗi mục có owner, response/next action, due date, status và escalation. Khi risk xảy ra, tạo issue và liên kết hai ID.

## 6. Decision and approval
Decision log ghi phương án, rationale, consequence và decision owner. Approval register ghi người duyệt, thời điểm, artifact version/commit SHA và bằng chứng. AI không tự phê duyệt Gate bắt buộc.

## 7. Escalation
Escalate khi vượt tolerance scope/schedule/cost, có risk Critical/High, tranh chấp quyền quyết định, compliance/security concern hoặc Gate/milestone có nguy cơ trễ. Ghi nhận người nhận, thời điểm, quyết định và action.

## 8. Closeout
Xác nhận deliverables/acceptance; xử lý hoặc bàn giao issue/risk còn lại; bàn giao vận hành, tài liệu và quyền truy cập; ghi lessons learned; Sponsor/PO xác nhận đóng; cập nhật `completed` hoặc `cancelled`; archive theo retention policy.
