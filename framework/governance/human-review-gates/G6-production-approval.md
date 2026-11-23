# G6 – Production Deployment Approval

**Thời điểm:** Ngay trước production deployment.  
**Approver:** Release Manager; Operations/Security/Business Owner tham gia theo rủi ro và release policy.

## AI chuẩn bị
Release note, deployment plan, change list, config checklist, migration plan, monitoring/alert plan, rollback/mitigation và CI/security evidence.

## Điều kiện thông qua
- [ ] Artifact/version đúng bản đã qua G4/G5.
- [ ] CI/CD và security checks bắt buộc đạt.
- [ ] Environment/config/secrets được quản lý an toàn.
- [ ] Migration có sequencing và recovery strategy phù hợp.
- [ ] Rollback/mitigation khả thi và có owner.
- [ ] Monitoring, alerting, health check và on-call sẵn sàng.
- [ ] Change window, dependency và communication được xác nhận.
- [ ] Residual risk được người có thẩm quyền chấp nhận.
- [ ] Có production approval rõ ràng.

**Decision:** Approve / Reject / Blocked. Pipeline xanh hoặc AI đánh giá rủi ro thấp không thay thế approval.  
**Audit:** Release ID, artifact digest, environment, approver, timestamp, deployment result, change record và rollback decision.
