# G6 – Production Deployment Approval

**Thời điểm:** Ngay trước production deployment.  
**Approver:** Release Manager; Operations/Security/Business Owner tham gia theo rủi ro và release policy.

## AI chuẩn bị
Release note, deployment plan, change list, config checklist, migration plan, monitoring/alert plan, rollback/mitigation và CI/security evidence.

## Điều kiện thông qua
- [ ] Artifact/version đúng bản đã qua G4/G5.
- [ ] CI/CD và security checks bắt buộc đạt.
- [ ] Environment/config/secrets được quản lý an toàn.
- [ ] Nếu G5 duyệt phạm vi phát hành giới hạn bằng feature flag, Release Manager đối chiếu cấu hình flag của môi trường production đích với gói review G5 và lưu bằng chứng trước khi cấp quyền. Kiểm tra lại trước rollout. Nếu không xác minh được hoặc cấu hình không khớp, chặn rollout; nếu muốn mở rộng phạm vi, quay lại QA và lấy G5 mới trước G6, kể cả khi artifact SHA-256 không đổi.
- [ ] Migration có sequencing và recovery strategy phù hợp.
- [ ] Rollback/mitigation khả thi và có owner.
- [ ] Monitoring, alerting, health check và on-call sẵn sàng.
- [ ] Change window, dependency và communication được xác nhận.
- [ ] Residual risk được người có thẩm quyền chấp nhận.
- [ ] Có production approval rõ ràng.

**Decision:** Approve / Reject / Blocked. Pipeline xanh hoặc AI đánh giá rủi ro thấp không thay thế approval.  
**Audit:** Release ID, artifact digest, environment, approver, timestamp, deployment result, change record và rollback decision.
