# G6 – Production Deployment Approval

**Thời điểm:** Chỉ áp dụng cho Production, sau khi readiness đạt và trước khi cấp quyền thực thi.

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
- [ ] Gói review đã chốt ghi rõ artifact SHA-256, môi trường Production đích và SHA-256 của gói review; tham chiếu hồ sơ G5 trên cùng artifact.

**Decision:** Approve / Reject / Blocked. Release Manager ghi quyết định trong [hồ sơ G6](../../07-deployment/templates/production-approval.md); pipeline xanh hoặc đánh giá của AI không thay thế approval.

**Trước khi thực thi:** Nếu plan, cấu hình hoặc bằng chứng trọng yếu thay đổi, trình review mới dù artifact không đổi. Sau khi cấp quyền, dùng [kiểm tra quyền thực thi Production](../../07-deployment/checklists/production-authorization-checklist.md) ngay trước khi chạy.

**Audit:** Hồ sơ G6 lưu quyết định, approver, thời điểm và các tham chiếu review/change. [Deployment Record](../../templates/deployment/deployment-record.md) lưu tham chiếu authorization/lượt bắt đầu, bằng chứng kết quả và xử lý rollback nếu có; hồ sơ G6 chỉ trỏ tới biên bản.
