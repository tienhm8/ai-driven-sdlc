# Workflow — Monitoring & Maintenance

> Tài liệu workflow cấp framework cho giai đoạn này. Tuân thủ governance, standards và template dùng chung trong `framework/`; các cấu hình riêng của dự án được kế thừa từ `projects/<Project>/.ai-sdlc/`.

# 8. Giai đoạn 08 — Monitoring & Maintenance

## 8.1 Purpose — Mục đích

Duy trì sức khỏe, tính sẵn sàng, an toàn và hiệu quả của hệ thống sau triển khai. Phát hiện bất thường, xử lý incident, phân tích nguyên nhân gốc (RCA), thực hiện bảo trì/cải tiến và cung cấp phản hồi cho backlog/SDLC tiếp theo.

## 8.2 Workflow Overview — Tổng quan luồng xử lý

```text
Bàn giao Production đã xác minh → Vận hành liên tục
  ├─ Giám sát thường kỳ → Quan sát, phân loại cảnh báo, review SLO
  ├─ Khi xác minh có sự cố → Triage, ứng phó (G7 nếu áp dụng), phục hồi, đóng
  │                         └─ RCA/postmortem nếu policy yêu cầu
  └─ Theo lịch/rủi ro → Bảo trì, vá lỗi, kiểm tra restore/DR

Cả ba nhánh → Review vận hành → Cải tiến/runbook/backlog
```

## 8.3 Entry Criteria — Điều kiện bắt đầu

- Release Production đã được xác minh thành công và bàn giao cho Operations theo [intake record](inputs/README.md#intake-record).
- Monitoring, logging, tracing, alerting và dashboard tối thiểu đã cấu hình.
- Có runbook, escalation path, on-call roster và incident severity definitions.
- Backup, restore, DR và access policy được xác định theo mức độ quan trọng của hệ thống.
- SLO/SLI hoặc tiêu chí vận hành đã được thống nhất ở mức phù hợp.

## 8.4 Workflow Steps — Các bước thực hiện

- **Bàn giao:** Operations xác nhận [intake 07 → 08](inputs/README.md#intake-record), service owner, system inventory và support window.
- **Giám sát thường kỳ:** theo dõi metrics, logs, traces, dependencies và business signals. Loại nhiễu, nhóm cảnh báo và định tuyến theo [mức ưu tiên alert](operations/alerting-guidelines.md). Nếu xác minh có sự cố, chuyển sang nhánh incident; không mở incident chỉ vì có alert.
- **Ứng phó sự cố:** xác minh tác động và severity, điều phối, ứng phó và phục hồi theo [Incident Management](operations/incident-management.md). Áp dụng G7 trước hành động thuộc gate. Người có thẩm quyền xác nhận phục hồi, đóng incident và quyết định postmortem theo policy.
- **Bảo trì có kế hoạch:** vá lỗi, cập nhật dependency, rotation, kiểm tra backup/restore/DR và capacity theo [hướng dẫn bảo trì và phục hồi](operations/maintenance-and-recovery.md). Nhánh này chạy theo lịch/rủi ro, không cần chờ incident.
- **Review và feedback:** đánh giá SLO/SLI, incident trend, alert quality, capacity, hiệu năng, chi phí và rủi ro. Đưa việc cải tiến vào backlog với priority, owner, hạn và tiêu chí xác minh; cập nhật runbook, architecture hoặc standards khi cần.

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
- Alert có mức ưu tiên, owner, action/runbook và ngưỡng hợp lý; incident severity được xác nhận riêng trong triage.
- Incident có timeline, impact, response và recovery evidence.
- RCA dựa trên evidence; phân biệt root cause với contributing factors.
- Action items có owner, due date và tiêu chí xác minh.
- Backup/restore/DR được kiểm tra theo lịch và policy.
- Patch/vulnerability được xử lý theo risk-based SLA.
- SLO/error budget/capacity/cost được review định kỳ.
- Runbook và ownership còn hiệu lực, có thể sử dụng khi incident.

## 8.10 Human Review Gate — Điểm phê duyệt bắt buộc

**G7 — phê duyệt trước hành động ứng phó thuộc gate.** Incident Commander (IC), hoặc người được ủy quyền theo [chính sách G7](../governance/human-review-gates/G7-incident-approval.md), duyệt phương án cho đúng incident và đúng phiên bản trước khi thực thi. Nếu phương án thay đổi trọng yếu, phải duyệt lại theo [gate policy](../governance/human-review-gates/gate-policy.md). Ngoại lệ khẩn cấp chỉ theo quy trình break-glass đã được tổ chức định nghĩa. Monitoring thường kỳ không qua G7 và không có G8.

**Phê duyệt vận hành — không phải G7.** Người được chỉ định trong incident policy xác nhận phục hồi, đóng incident hoặc ký xác nhận RCA. Service Owner hoặc người có thẩm quyền theo risk policy chấp nhận rủi ro còn lại. Thay đổi có kế hoạch theo change control và gate tương ứng nếu áp dụng. Các phê duyệt này không thay thế G7 cho hành động thuộc gate. Phê duyệt G7 cũng không cấp quyền thực thi; AI không tự phê duyệt.

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
