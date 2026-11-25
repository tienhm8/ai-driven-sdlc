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
Pre-deployment Readiness Checks
        ↓
Production: G6 → authorize_action → check_action_start ngay trước khi chạy
Non-production: kiểm tra quyền theo policy môi trường; không áp dụng G6
        ↓
Thực thi migration / rollout / chuyển traffic theo thứ tự trong plan
        ↓
Xác minh kết quả
        ├─ Production thành công → bàn giao Stage 08
        ├─ Rollback hoặc thất bại không đổi đích đã xác minh → giữ Stage 07
        └─ Kết quả chưa rõ → chặn chuyển stage và thử lại
```

## 7.3 Entry Criteria — Điều kiện bắt đầu

- G5 đã phê duyệt đúng release candidate.
- Có release plan, deployment runbook, rollback/restore plan.
- Change window, approver, on-call và stakeholder communication được xác định.
- CI/CD pipeline, secrets, environment và access control sẵn sàng.
- Database migration, feature flags và external dependencies đã được đánh giá.

## 7.4 Workflow Steps — Các bước thực hiện

1. **Lập deployment request:** ghi release version, scope, mục tiêu, change window, impact và owner.
2. **Kiểm tra readiness:** xác nhận hồ sơ G5, các phê duyệt đầu vào, runbook, rollback và support coverage. Chưa yêu cầu quyết định G6 tại bước này.
3. **Xác minh artifact:** đối chiếu artifact bất biến (URI/version, SHA-256, build ID và provenance liên kết merge G4) với [hồ sơ G5 được bàn giao](inputs/README.md#quy-tắc); không xác nhận lại thay QA. Nếu cần rebuild cùng source, ghi lý do và dùng `return_to_qa` để kiểm thử lại và lấy G5 mới. Nếu phải sửa source, dùng `return_to_development` để quay lại Development → G4 mới → build mới → QA/G5 mới. Sau đó lấy G6 mới nếu triển khai Production. Không quay lại các stage này khi một authorization Production chưa có kết quả kết thúc đã xác minh.
4. **Kiểm tra cấu hình:** validate environment variables, secrets reference, feature flags, resource limits và network policy.
5. **Chuẩn bị dữ liệu:** backup/snapshot theo policy; rehearsal migration; xác nhận backward/forward compatibility và restore path.
6. **Chuẩn bị release notes và thông báo:** Deployment lập release notes từ release scope và gói bàn giao Stage 06; gửi release notice, expected impact, maintenance window và escalation contact.
7. **Pre-deployment checks:** kiểm tra health baseline, capacity, dependency, alert status và freeze condition.
8. **Phê duyệt và kiểm tra quyền thực thi:** chỉ với Production, Release Manager ghi quyết định G6 sau khi readiness đạt. Adapter tin cậy gọi `authorize_action` cho đúng quyết định G6, SHA-256 của artifact, môi trường đích và SHA-256 của gói review đã chốt. Nếu plan/config hoặc bằng chứng trọng yếu thay đổi, trình review mới dù artifact không đổi; nếu mở rộng phạm vi G5 đã duyệt thì quay lại QA trước. Ngay trước khi gửi lệnh chạy, đối chiếu lại các giá trị hiện tại bằng `check_action_start`; nếu không khớp hoặc authorization không hợp lệ, không chạy. Non-production không dùng G6 nhưng vẫn tuân thủ quyền và policy môi trường.
9. **Thực thi theo deployment plan đã duyệt:** làm theo thứ tự migration, rollout và chuyển traffic trong plan; không mặc định migration chạy sau rollout. Ghi rõ bước cần hoàn tất trước khi chuyển traffic (ví dụ mở rộng schema), bước sau rollout (ví dụ thu hẹp schema khi đủ điều kiện), và tiêu chí tiếp tục, dừng hoặc khôi phục ở từng mốc. Kiểm soát lock/downtime, giới hạn phạm vi ảnh hưởng và ghi evidence từng bước.
10. **Smoke/sanity test:** xác minh critical path, health endpoint, integration và telemetry sau triển khai.
11. **Theo dõi rollout:** đánh giá error rate, latency, saturation, business metrics và alert trong observation window.
12. **Quyết định tiếp tục/rollback:** so sánh với deployment success criteria; kích hoạt rollback/mitigation nếu vượt ngưỡng.
13. **Ghi nhận và xác minh kết quả:** lưu [Deployment Record](../templates/deployment/deployment-record.md), trạng thái thực tế và bằng chứng; với Production, nộp tham chiếu kết quả tin cậy cho Workflow Engine đối chiếu với đúng authorization, lượt bắt đầu, artifact và đích. Xử lý theo các nhánh bên dưới; đóng hồ sơ lần thực thi không đồng nghĩa hoàn thành stage và không thay thế G6.

## 7.5 Input — Đầu vào

- [Gói bàn giao Stage 06](inputs/README.md): artifact đã qua G5, định danh/provenance, hồ sơ G5 và bằng chứng QA.
- Deployment plan/runbook, change request và approval.
- Infrastructure/configuration/secrets reference.
- Database migration, backup/restore và rollback plan.
- Tiêu chí smoke từ Stage 06; health check và monitoring dashboard.
- Stakeholder/on-call contacts và incident procedure.

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

- [Deployment Record](../templates/deployment/deployment-record.md): phiên bản đích/thực tế, artifact, commit, môi trường, timestamp, người thực thi, kết quả và bàn giao.
- Change approval và deployment checklist.
- Backup/snapshot reference và migration execution report.
- Smoke test/health verification evidence.
- Rollout metrics, incident/rollback record nếu có.
- Release notes và stakeholder notification.
- Trạng thái phát hành Production và hồ sơ G6 (chỉ áp dụng cho Production).

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

| Kết quả Production | Đóng hồ sơ và chuyển stage |
|---|---|
| **Triển khai thành công đã xác minh** | Cập nhật phiên bản đang chạy và bàn giao cho Operations. Chỉ nhánh này mới hoàn thành Stage 07 và chuyển sang Stage 08. |
| **Rollback đã xác minh** (`rolled_back`) **hoặc thất bại không thay đổi đích đã xác minh** (`failed_no_changes`) | Đóng hồ sơ lần thực thi, ghi phiên bản thực tế và chuyển thông tin sự cố cho Operations nếu cần. Không ghi release mới là đã triển khai; giữ Stage 07. Muốn thử lại phải mở review G6 mới và được cấp quyền mới. |
| **Thiếu, sai lệch hoặc chưa đủ bằng chứng** | Giữ hồ sơ mở, chuyển thông tin sự cố nếu cần và tiếp tục xác minh. Không chuyển stage hoặc thử lại khi authorization trước chưa có kết quả kết thúc đã xác minh. |

Triển khai non-production không thay thế kết quả Production và không tự chuyển Stage 07.

## 7.12 Exception Handling — Xử lý ngoại lệ

- **Pre-check fail:** hoãn deployment; không bypass check nếu chưa có exception approval.
- **Deployment failure:** dừng rollout, thu thập evidence, kích hoạt rollback/mitigation theo runbook.
- **Migration failure:** không chạy lại tùy tiện; đánh giá trạng thái transaction/data và gọi DBA/Data Owner.
- **Health metric vượt ngưỡng:** freeze rollout, notify incident/on-call và quyết định rollback.
- **Artifact/config mismatch:** hủy deployment, xác minh provenance và pipeline.
- **Emergency deployment:** dùng emergency change process, giới hạn scope và thực hiện retrospective. Production vẫn cần G6 và kiểm tra quyền ngay trước khi chạy; nếu dùng ngoại lệ, ghi tham chiếu và thời điểm hết hiệu lực trong [hồ sơ G6](templates/production-approval.md).

## 7.13 Next Stage — Chuyển sang giai đoạn tiếp theo

Sau khi xác minh triển khai Production thành công, bàn giao theo [đầu vào Stage 08](../08-monitoring-maintenance/inputs/README.md#intake-record). Ghi phiên bản đang chạy, dashboard/alert, runbook, on-call, rủi ro còn lại, người tiếp nhận và thời điểm trong Deployment Record. Nếu chưa xác minh thành công, chỉ bàn giao thông tin sự cố khi cần, không chuyển stage.

---
