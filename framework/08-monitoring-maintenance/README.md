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
- `operations/`: monitoring, alerting, incident management, RCA và [bảo trì/kiểm tra phục hồi](operations/maintenance-and-recovery.md).
- `templates/`: maintenance plan, monitoring report, postmortem, backlog, incident report.
- `checklists/`: readiness, incident response, maintenance, security operations, recovery.
- [Đầu vào](inputs/README.md): bàn giao từ 07, tham chiếu 01–06 và dữ liệu runtime.
- [Đầu ra](outputs/README.md): quy ước và ví dụ; hồ sơ thực tế nằm trong project instance.
- `workflow.md`, `ai-instructions.md`, `human-review.md`: quy trình, chỉ dẫn AI và kiểm soát con người.

## Nguyên tắc
1. Ưu tiên khôi phục dịch vụ và giảm tác động; điều tra sâu có thể thực hiện sau khi ổn định.
2. Alert phải actionable, có owner, mức ưu tiên và runbook; incident severity được xác nhận riêng khi triage.
3. Mọi hành động production phải đúng quyền, có audit trail và rollback phù hợp.
4. AI chỉ tự thực hiện tác vụ L1/L2 đã được cho phép. Với L3, AI chỉ thực thi khi có phê duyệt trước và quyền thực thi được cấp riêng. Với L4, AI chỉ hỗ trợ; con người quyết định và kiểm soát hành động.
5. Không đưa secrets, credentials, raw PII hoặc dữ liệu nhạy cảm vào báo cáo.
6. Postmortem không quy kết cá nhân; tập trung vào điều kiện hệ thống.
7. Mọi quyết định và hành động phải có timestamp, người thực hiện và kết quả.

## Autonomy
Áp dụng [autonomy theo từng hành động](ai-instructions.md#9-autonomy-level). Mức autonomy, phê duyệt hành động và quyền của executor là ba kiểm tra riêng.

## Human Review Gate G7
[G7](../governance/human-review-gates/G7-incident-approval.md) áp dụng trước hành động ứng phó thuộc gate, không áp dụng cho giám sát thường kỳ, xác nhận phục hồi, đóng incident hay ký RCA. Xem [workflow](workflow.md) để phân biệt G7 với phê duyệt vận hành.
