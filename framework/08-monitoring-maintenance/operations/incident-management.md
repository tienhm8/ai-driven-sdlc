# Incident Management

## Mục tiêu
Khôi phục dịch vụ an toàn, giảm tác động, duy trì thông tin nhất quán và học hỏi sau sự cố.

## Kích hoạt
Tạo incident khi gián đoạn/suy giảm đáng kể, vi phạm/nguy cơ vi phạm SLO, ảnh hưởng dữ liệu, security/privacy event hoặc cần phối hợp nhiều nhóm. Severity theo policy đã duyệt.

## Vai trò
- **IC:** điều phối, ưu tiên, quyết định/phê duyệt theo thẩm quyền.
- **Technical Lead:** điều tra và đề xuất mitigation.
- **SRE/Operations:** thực thi runbook được phép.
- **Communications Lead:** cập nhật stakeholder.
- **Scribe:** ghi timeline, quyết định, actions, evidence.

## Quy trình
1. Detect & declare: ghi thời điểm, nguồn alert, người báo.
2. Triage: service, environment, blast radius, user impact, data/security risk, recent changes.
3. Mobilize: chỉ định IC và vai trò; mở incident channel theo policy.
4. Mitigate: ưu tiên biện pháp giảm tác động, có thể đảo ngược; xin G7 approval khi cần.
5. Communicate: cập nhật impact, workaround và thời điểm cập nhật tiếp; không suy đoán nguyên nhân.
6. Recover: rollback/failover/restore theo runbook; kiểm tra SLI, health, data integrity.
7. Resolve & close: người có thẩm quyền xác nhận tiêu chí phục hồi và thông báo.
8. Learn: RCA/postmortem và action tracking.

## G7
AI không tự quyết định/thực hiện remediation rủi ro cao. IC phê duyệt phương án, executor, stop condition, rollback và communications. Emergency playbook đã duyệt áp dụng theo policy và phải hậu kiểm.

## Incident record
Incident ID, severity, service/environment, detect/ack/mitigate/recover/resolve timestamps, impact, timeline, participants, evidence, actions, approvals, communications, recovery validation và follow-up owners.

Không đổ lỗi cá nhân; phân tích điều kiện hệ thống, quy trình, công cụ và rào chắn.
