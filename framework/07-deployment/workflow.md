# Workflow — Deployment

> Tài liệu workflow cấp framework cho giai đoạn này. Tuân thủ governance, standards và template dùng chung trong `framework/`; các cấu hình riêng của dự án được kế thừa từ `projects/<Project>/.ai-sdlc/`.

# 7. Giai đoạn 07 — Deployment

## 7.1 Purpose — Mục đích

Đưa release candidate đã được QA phê duyệt vào môi trường mục tiêu một cách an toàn, có kiểm soát, quan sát được và có khả năng rollback/restore. Đảm bảo cấu hình, dữ liệu, quyền truy cập và truyền thông phát hành được chuẩn bị đầy đủ.

## 7.2 Workflow Overview — Tổng quan luồng xử lý

```text
Approved Release Candidate (G5)
        ↓
Deployment Readiness & Change Review
        ↓
Immutable Artifact / Configuration Validation
        ↓
Pre-deployment Backup & Safety Checks
        ↓
G6 — Production Deployment Approval
        ↓
Deploy (Staged / Canary / Blue-Green / Rolling)
        ↓
Smoke Test & Health Verification
        ↓
Handoff to Monitoring & Maintenance
```

## 7.3 Entry Criteria — Điều kiện bắt đầu

- G5 đã phê duyệt đúng release candidate.
- Có release plan, deployment runbook, rollback/restore plan.
- Change window, approver, on-call và stakeholder communication được xác định.
- CI/CD pipeline, secrets, environment và access control sẵn sàng.
- Database migration, feature flags và external dependencies đã được đánh giá.

## 7.4 Workflow Steps — Các bước thực hiện

1. **Lập deployment request:** ghi release version, scope, mục tiêu, change window, impact và owner.
2. **Kiểm tra readiness:** xác nhận G5, artifact provenance, approvals, runbook, rollback và support coverage.
3. **Xác minh artifact:** dùng đúng immutable artifact đã qua G5; đối chiếu commit, tag, build ID và SHA-256. Nếu cần rebuild trước khi G6 cấp quyền triển khai, ghi lý do, quay lại QA và lấy lại G5/G6 cho candidate mới. Không dùng quyền G6 cũ để triển khai lại.
4. **Kiểm tra cấu hình:** validate environment variables, secrets reference, feature flags, resource limits và network policy.
5. **Chuẩn bị dữ liệu:** backup/snapshot theo policy; rehearsal migration; xác nhận backward/forward compatibility và restore path.
6. **Thông báo:** gửi release notice, expected impact, maintenance window và escalation contact.
7. **Pre-deployment checks:** kiểm tra health baseline, capacity, dependency, alert status và freeze condition.
8. **G6 trước khi triển khai production:** Release Manager ghi quyết định Go/No-Go cho đúng artifact đã qua G5. Không chạy rollout hoặc migration trên production nếu chưa đủ điều kiện G6. Sau đó **triển khai theo chiến lược:** rolling/canary/blue-green/staged phù hợp; áp dụng giới hạn blast radius.
9. **Thực hiện migration:** chạy theo thứ tự, idempotency và kiểm soát lock/downtime; ghi log kết quả.
10. **Smoke/sanity test:** xác minh critical path, health endpoint, integration và telemetry sau triển khai.
11. **Theo dõi rollout:** đánh giá error rate, latency, saturation, business metrics và alert trong observation window.
12. **Quyết định tiếp tục/rollback:** so sánh với deployment success criteria; kích hoạt rollback/mitigation nếu vượt ngưỡng.
13. **Closure:** người có thẩm quyền xác nhận trạng thái production sau rollout, lưu deployment record và thông báo hoàn tất. Không dùng bước này thay cho G6 trước rollout.

## 7.5 Input — Đầu vào

- Release candidate đã qua G5, artifact và provenance.
- Deployment plan/runbook, change request và approval.
- Infrastructure/configuration/secrets reference.
- Database migration, backup/restore và rollback plan.
- Smoke test, health check và monitoring dashboard.
- Release notes, stakeholder/on-call contacts và incident procedure.

## 7.6 AI Activities — Hoạt động AI

- Kiểm tra deployment checklist, runbook completeness và dependency.
- Tóm tắt change impact, release notes và communication draft.
- Hỗ trợ validate cấu hình, manifest, IaC plan và pipeline output.
- Phân tích health metrics/logs trong rollout và cảnh báo bất thường.
- Đề xuất bước xử lý/rollback dựa trên runbook đã duyệt.
- Tạo deployment evidence và cập nhật change record.
- Không tự phê duyệt production change, không tự thay đổi production hoặc rollback nếu chưa được cấp quyền/ủy quyền rõ ràng.

## 7.7 Human Activities — Hoạt động con người

- DevOps/SRE/Release Engineer thực hiện và giám sát deployment.
- Change/Release Manager xác nhận change window và approval.
- QA xác nhận smoke/sanity tests khi cần.
- DBA/Data Owner phê duyệt migration và backup/restore quan trọng.
- Business Owner xác nhận tác động nghiệp vụ và thông báo.
- Incident Commander/on-call quyết định escalation/rollback theo policy.

## 7.8 Output — Đầu ra

- Deployment record: version, artifact, commit, environment, timestamp, actor.
- Change approval và deployment checklist.
- Backup/snapshot reference và migration execution report.
- Smoke test/health verification evidence.
- Rollout metrics, incident/rollback record nếu có.
- Release notes và stakeholder notification.
- Production release status và G6 approval record.

## 7.9 Quality Check — Kiểm tra chất lượng

- Artifact triển khai đúng SHA-256 đã qua G5 và được G6 phê duyệt trước rollout; provenance có thể truy vết.
- Cấu hình/secrets đúng môi trường, không lộ secret.
- Backup/restore và migration plan được xác nhận.
- Deployment theo đúng change window và approval.
- Smoke test, health check và business-critical path đạt.
- Metrics không vượt rollback threshold trong observation window.
- Có deployment log, người thực hiện và kết quả rõ ràng.

## 7.10 Human Review Gate — Điểm phê duyệt bắt buộc

**G6 — Production Deployment Approval (trước khi thay đổi production)**

Người phê duyệt: Release Manager. SRE/DevOps và owner chuyên môn xác nhận readiness theo mức rủi ro.

Điều kiện:
- G5 hợp lệ và đúng artifact.
- Change/deployment plan, rollback/restore và on-call sẵn sàng.
- Pre-deployment checks đạt.

Smoke test và health criteria được kiểm tra sau rollout để đóng deployment; không phải điều kiện để phê duyệt G6 từ trước.

## 7.11 Exit Criteria — Điều kiện hoàn thành

- Deployment được xác nhận thành công hoặc rollback được ghi nhận hoàn chỉnh.
- Có bản ghi authorization G6 trước khi triển khai đúng artifact lên production.
- Production version và deployment evidence được cập nhật.
- Monitoring/alerting ownership và support handoff đã xác nhận.

## 7.12 Exception Handling — Xử lý ngoại lệ

- **Pre-check fail:** hoãn deployment; không bypass check nếu chưa có exception approval.
- **Deployment failure:** dừng rollout, thu thập evidence, kích hoạt rollback/mitigation theo runbook.
- **Migration failure:** không chạy lại tùy tiện; đánh giá trạng thái transaction/data và gọi DBA/Data Owner.
- **Health metric vượt ngưỡng:** freeze rollout, notify incident/on-call và quyết định rollback.
- **Artifact/config mismatch:** hủy deployment, xác minh provenance và pipeline.
- **Emergency deployment:** dùng emergency change process, giới hạn scope, ghi nhận người phê duyệt và retrospective bắt buộc.

## 7.13 Next Stage — Chuyển sang giai đoạn tiếp theo

Bàn giao production version, deployment record, dashboard, alert rules, runbook, known issues và on-call ownership cho **08 — Monitoring & Maintenance**.

---
