# G6 – Production Deployment Approval

**Thời điểm:** Chỉ áp dụng cho Production, sau khi readiness đạt và trước khi cấp quyền thực thi.

**Approver:** Release Manager; Operations/Security/Business Owner tham gia theo rủi ro và release policy.

## AI chuẩn bị
Release note, deployment plan, change list, config checklist, migration plan, monitoring/alert plan, rollback/mitigation và CI/security evidence.

## Điều kiện thông qua
- [ ] Truy vết đúng chuỗi release: **G4** ghi repository và merge commit đã xác minh → **G5** duyệt release candidate có build provenance nối đúng repository/commit đó với digest của candidate → **G6** phê duyệt và triển khai đúng digest đã qua G5 vào môi trường Production đích đã duyệt.
- [ ] CI/CD và security checks bắt buộc đạt.
- [ ] Environment/config/secrets được quản lý an toàn.
- [ ] Nếu G5 duyệt phạm vi phát hành giới hạn bằng feature flag, Release Manager đối chiếu cấu hình flag của môi trường production đích với gói review G5 và lưu bằng chứng trước khi cấp quyền. Kiểm tra lại trước rollout. Nếu không xác minh được hoặc cấu hình không khớp, chặn rollout; nếu muốn mở rộng phạm vi, quay lại QA và lấy G5 mới trước G6, kể cả khi artifact SHA-256 không đổi.
- [ ] Migration có sequencing và recovery strategy phù hợp.
- [ ] Rollback/mitigation khả thi và có owner.
- [ ] Monitoring, alerting, health check và on-call sẵn sàng.
- [ ] Change window, dependency và communication được xác nhận.
- [ ] Residual risk được người có thẩm quyền chấp nhận.
- [ ] Gói review đã chốt ghi rõ artifact SHA-256, môi trường Production đích và SHA-256 của gói review; tham chiếu hồ sơ G5 trên cùng artifact.

**Quyết định:** Release Manager ghi quyết định trong [hồ sơ G6](../../07-deployment/templates/production-approval.md) theo [policy chung về quyết định và trạng thái gate](gate-policy.md#reviewer-decision). Pipeline xanh hoặc đánh giá của AI không thay thế approval.

**Trước khi thực thi:** Nếu plan, cấu hình hoặc bằng chứng trọng yếu thay đổi, trình review mới dù artifact không đổi. Sau khi cấp quyền, dùng [kiểm tra quyền thực thi Production](../../07-deployment/checklists/production-authorization-checklist.md) ngay trước khi chạy.

**Bằng chứng riêng của G6:** Hồ sơ G6 dẫn chiếu change record, hồ sơ G5 và [Deployment Record](../../templates/deployment/deployment-record.md). Deployment Record lưu tham chiếu quyền thực thi và lần bắt đầu, kết quả triển khai đã xác minh và quyết định/kết quả rollback nếu có.
