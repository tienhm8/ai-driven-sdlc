# 08 – Monitoring & Maintenance

## Mục tiêu
Duy trì độ tin cậy, tính sẵn sàng, an toàn và hiệu năng sau Production thông qua observability, alerting, incident response, recovery, RCA, bảo trì và cải tiến liên tục.

## Vai trò
- **AI:** phân tích logs, metrics, traces; phát hiện bất thường; tương quan tín hiệu; đề xuất chẩn đoán, mitigation, RCA và backlog.
- **SRE/Operations:** xác minh alert, vận hành runbook được duyệt và theo dõi sức khỏe hệ thống.
- **Incident Commander (IC):** chỉ huy sự cố nghiêm trọng, phân công vai trò và phê duyệt phương án theo thẩm quyền.
- **Service Owner/Tech Lead:** chịu trách nhiệm dịch vụ, đánh giá thay đổi và ưu tiên khắc phục.
- **Security/Privacy:** tham gia sự cố bảo mật hoặc dữ liệu nhạy cảm.

## Cấu trúc
- `operations/`: monitoring, alerting, incident management, RCA.
- `templates/`: maintenance plan, monitoring report, postmortem, backlog, incident report.
- `checklists/`: readiness, incident response, maintenance, security operations, recovery.
- `inputs/`: tham chiếu từ SDLC 01–07 và dữ liệu runtime.
- `outputs/`: báo cáo, hồ sơ sự cố, postmortem và bằng chứng vận hành.
- `workflow.md`, `ai-instructions.md`, `human-review.md`: quy trình, chỉ dẫn AI và kiểm soát con người.

## Nguyên tắc
1. Ưu tiên khôi phục dịch vụ và giảm tác động; điều tra sâu có thể thực hiện sau khi ổn định.
2. Alert phải actionable, có owner, severity và runbook.
3. Mọi hành động production phải đúng quyền, có audit trail và rollback phù hợp.
4. AI chỉ tự thực hiện L1/L2 đã được cho phép; không quyết định L3/L4.
5. Không đưa secrets, credentials, raw PII hoặc dữ liệu nhạy cảm vào báo cáo.
6. Postmortem không quy kết cá nhân; tập trung vào điều kiện hệ thống.
7. Mọi quyết định và hành động phải có timestamp, người thực hiện và kết quả.

## Autonomy
- **L1:** tổng hợp dashboard, phân loại log, báo cáo, phát hiện rule.
- **L2:** đề xuất tuning, tạo ticket, diagnostic read-only hoặc thao tác whitelist.
- **L3:** restart, scale, failover, config change cần người review/phê duyệt theo policy.
- **L4:** sự cố nghiêm trọng, thay đổi dữ liệu, security containment lớn, DR và chấp nhận rủi ro do con người quyết định.

## Human Review Gate G7
Khi xử lý sự cố nghiêm trọng, Incident Commander phê duyệt phương án rủi ro cao. Lưu approver, timestamp, phạm vi, runbook/change version, kết quả và quyết định. Emergency playbook được duyệt trước có thể áp dụng theo policy nhưng phải audit và hậu kiểm.
