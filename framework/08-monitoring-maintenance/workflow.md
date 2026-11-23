# Workflow — Monitoring & Maintenance

> Tài liệu workflow cấp framework cho giai đoạn này. Tuân thủ governance, standards và template dùng chung trong `framework/`; các cấu hình riêng của dự án được kế thừa từ `projects/<Project>/.ai-sdlc/`.

# 8. Giai đoạn 08 — Monitoring & Maintenance

## 8.1 Purpose — Mục đích

Duy trì sức khỏe, tính sẵn sàng, an toàn và hiệu quả của hệ thống sau triển khai. Phát hiện bất thường, xử lý incident, phân tích nguyên nhân gốc (RCA), thực hiện bảo trì/cải tiến và cung cấp phản hồi cho backlog/SDLC tiếp theo.

## 8.2 Workflow Overview — Tổng quan luồng xử lý

```text
Production Handoff
        ↓
Observe Metrics / Logs / Traces / Business Signals
        ↓
Alert Triage & Incident Classification
        ↓
Mitigation / Recovery
        ↓
RCA & Corrective / Preventive Actions
        ↓
Maintenance / Optimization / Security Updates
        ↓
Operational Review & Feedback to Backlog
        ↺
```

## 8.3 Entry Criteria — Điều kiện bắt đầu

- Release đã được bàn giao cho operations; có production version và owner.
- Monitoring, logging, tracing, alerting và dashboard tối thiểu đã cấu hình.
- Có runbook, escalation path, on-call roster và incident severity definitions.
- Backup, restore, DR và access policy được xác định theo mức độ quan trọng của hệ thống.
- SLO/SLI hoặc tiêu chí vận hành đã được thống nhất ở mức phù hợp.

## 8.4 Workflow Steps — Các bước thực hiện

1. **Tiếp nhận vận hành:** xác nhận service owner, system inventory, production version, support window và escalation contact.
2. **Quan sát hệ thống:** theo dõi metrics, logs, traces, infrastructure, dependency và business signals.
3. **Quản lý alert:** nhận alert, loại bỏ noise, deduplicate, correlate và xác định mức độ ưu tiên.
4. **Triage:** xác minh impact, affected users/services, timeline, severity và incident commander.
5. **Ứng phó incident:** kích hoạt runbook, khoanh vùng, giảm blast radius, thông báo stakeholder và bảo toàn evidence.
6. **Khôi phục dịch vụ:** failover, rollback, scale, disable feature hoặc workaround theo quyền hạn và runbook.
7. **Xác nhận recovery:** kiểm tra health, data consistency, business transaction và thời gian ổn định.
8. **Truyền thông và đóng incident:** cập nhật status, impact, resolution và follow-up owner.
9. **RCA/post-incident review:** dựng timeline, xác định contributing factors/root causes; tập trung cải tiến hệ thống, tránh quy lỗi cá nhân.
10. **Tạo corrective/preventive actions:** chuyển thành task có priority, owner, due date và verification criteria.
11. **Bảo trì định kỳ:** patching, dependency updates, certificate rotation, backup verification, capacity review và vulnerability remediation.
12. **Tối ưu:** phân tích performance/cost/reliability, technical debt và user feedback; đề xuất cải tiến.
13. **Review vận hành:** đánh giá SLO/SLI, incident trend, alert quality, capacity và operational risk.
14. **Feedback loop:** chuyển yêu cầu/cải tiến vào Requirement Analysis hoặc Task Planning; cập nhật runbook/architecture/standards khi cần.

## 8.5 Input — Đầu vào

- Production handoff và deployment records.
- SLI/SLO, metrics, logs, traces, alerts và dashboards.
- Incident tickets, user reports và business impact.
- Runbooks, architecture/dependency map và configuration inventory.
- Backup/restore/DR records, vulnerability/dependency reports.
- Capacity, cost, availability và performance history.

## 8.6 AI Activities — Hoạt động AI

- Tổng hợp telemetry và phát hiện anomaly/trend trong phạm vi dữ liệu được phép.
- Correlate alert/log/trace và đề xuất phạm vi ảnh hưởng.
- Hỗ trợ incident triage, timeline và incident communication draft.
- Tìm kiếm runbook liên quan và đề xuất bước chẩn đoán an toàn.
- Hỗ trợ RCA bằng cách tổng hợp evidence, giả thuyết và contributing factors; không kết luận nguyên nhân khi chưa xác minh.
- Đề xuất corrective/preventive actions, patch prioritization và capacity optimization.
- Tạo operational report, SLO summary và knowledge base update draft.
- Không tự thực hiện hành động phá hủy, thay đổi production hoặc truy cập dữ liệu nhạy cảm ngoài quyền được cấp.

## 8.7 Human Activities — Hoạt động con người

- SRE/Operations chịu trách nhiệm health, monitoring, alerting và reliability.
- On-call Engineer thực hiện triage và mitigation trong phạm vi runbook.
- Incident Commander điều phối incident theo severity.
- Service Owner quyết định ưu tiên remediation và chấp nhận rủi ro vận hành.
- Security/Privacy/Compliance tham gia sự cố liên quan dữ liệu/bảo mật.
- Engineering team thực hiện corrective actions và xác nhận hiệu quả.
- Product Owner tiếp nhận feedback để điều chỉnh roadmap/backlog.

## 8.8 Output — Đầu ra

- Operational dashboards, SLI/SLO reports và alert history.
- Incident records, timeline, communication log và recovery evidence.
- RCA/Postmortem report.
- Corrective/Preventive Action items.
- Maintenance, patching, backup/restore và DR verification records.
- Capacity/performance/cost optimization recommendations.
- Updated runbooks, knowledge base, architecture/technical debt records.
- Feedback backlog/change requests cho chu kỳ SDLC tiếp theo.

## 8.9 Quality Check — Kiểm tra chất lượng

- Monitoring bao phủ service health, critical dependency và business-critical flow.
- Alert có severity, owner, action/runbook và ngưỡng hợp lý.
- Incident có timeline, impact, response và recovery evidence.
- RCA dựa trên evidence; phân biệt root cause với contributing factors.
- Action items có owner, due date và tiêu chí xác minh.
- Backup/restore/DR được kiểm tra theo lịch và policy.
- Patch/vulnerability được xử lý theo risk-based SLA.
- SLO/error budget/capacity/cost được review định kỳ.
- Runbook và ownership còn hiệu lực, có thể sử dụng khi incident.

## 8.10 Human Review Gate — Điểm phê duyệt bắt buộc

**Operational Approval / Incident Closure Review**

Giai đoạn này không mặc định có G8 trong mapping G1–G7. Áp dụng các phê duyệt vận hành theo `governance/human-review-gates/gate-policy.md` và incident policy.

Bắt buộc có người phê duyệt khi:
- Thực hiện hành động production có rủi ro cao hoặc khó đảo ngược.
- Thay đổi dữ liệu, quyền truy cập, security control hoặc cấu hình trọng yếu.
- Chấp nhận rủi ro vượt ngưỡng/SLO hoặc đóng incident nghiêm trọng.
- Xác nhận RCA và các action ưu tiên đối với incident major.

Người phê duyệt: Service Owner, Incident Commander, Change Owner hoặc Security/Data Owner tùy loại quyết định. AI không được tự phê duyệt.

## 8.11 Exit Criteria — Điều kiện hoàn thành

Đây là giai đoạn vận hành liên tục, không có “hoàn thành cuối cùng” như các giai đoạn trước. Một work item vận hành được đóng khi:
- Service trở lại trạng thái ổn định hoặc trạng thái degraded được chấp nhận chính thức.
- Incident/maintenance record có đầy đủ evidence và owner.
- RCA/action items được tạo khi cần.
- Runbook, monitoring và knowledge base được cập nhật.
- Các cải tiến được chuyển thành backlog có thể truy vết.

## 8.12 Exception Handling — Xử lý ngoại lệ

- **Major/Critical incident:** kích hoạt incident command, escalation và communication policy; ưu tiên khôi phục dịch vụ và bảo toàn evidence.
- **Mất telemetry:** chuyển sang phương án quan sát dự phòng; ghi nhận blind spot và khôi phục instrumentation.
- **Alert storm:** áp dụng deduplication/correlation có kiểm soát; không tắt alert quan trọng khi chưa đánh giá.
- **Backup/restore thất bại:** escalates tới service/data owner; đánh giá RPO/RTO và rủi ro mất dữ liệu.
- **Phát hiện security/privacy incident:** kích hoạt security incident response và nghĩa vụ thông báo theo policy/pháp luật.
- **Không đạt SLO kéo dài:** lập reliability improvement plan, review capacity/architecture và ưu tiên backlog.
- **AI đưa ra chẩn đoán thiếu bằng chứng:** coi là giả thuyết; yêu cầu xác minh trước khi thay đổi production.

## 8.13 Next Stage — Chuyển sang giai đoạn tiếp theo

- Incident, user feedback, operational metrics và technical debt trở thành đầu vào cho **01 — Requirement Analysis** hoặc **03 — Task Planning** tùy bản chất thay đổi.
- Thay đổi nhỏ, đã nằm trong backlog và không đổi requirement/design baseline có thể đi thẳng vào Task Planning theo change policy.
- Thay đổi ảnh hưởng mục tiêu nghiệp vụ, phạm vi hoặc NFR phải quay lại Requirement Analysis.
- Thay đổi kiến trúc trọng yếu phải cập nhật System Design và ADR trước khi triển khai.
- Duy trì vòng lặp liên tục: **Monitor → Learn → Prioritize → Improve → Release → Monitor**.

---
