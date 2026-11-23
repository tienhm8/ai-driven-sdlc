# Checklist triển khai – Template

**Release:** [ID/version] · **Environment:** [target] · **Owner:** [name]

## A. Định danh release
- [ ] Release scope đã được xác nhận.
- [ ] Commit SHA và artifact digest/version đã được ghi nhận.
- [ ] Artifact được promote từ pipeline đã xác minh.
- [ ] Evidence G4/G5 được liên kết với release candidate này.

## B. Sẵn sàng nền tảng
- [ ] Environment, capacity, network, DNS/TLS và dependencies đã sẵn sàng.
- [ ] Cấu hình riêng môi trường đã review; không có plaintext secrets.
- [ ] IAM/service account tuân thủ least privilege.
- [ ] Pipeline approvals, logs và audit trail hoạt động.

## C. Dữ liệu và tương thích
- [ ] Thứ tự migration và khả năng tương thích đã review.
- [ ] Evidence backup/restore còn hiệu lực khi yêu cầu.
- [ ] Rủi ro mất dữ liệu và side-effect bên ngoài đã được ghi nhận.
- [ ] Đã xác nhận tương thích API/client.

## D. Thực thi và xác minh
- [ ] Chiến lược và batch/traffic shift đã được xác định.
- [ ] Health checks và smoke tests đã sẵn sàng.
- [ ] Dashboard, alerts và on-call đã sẵn sàng.
- [ ] Đã thông báo truyền thông/maintenance window.
- [ ] Đã xác nhận rollback trigger, owner và runbook.

## E. Phê duyệt và đóng
- [ ] G6 đã được Release Manager phê duyệt trước khi thực thi trên Production.
- [ ] Mỗi bước thực thi đều có evidence.
- [ ] Đã hoàn tất kiểm tra sau triển khai.
- [ ] Deployment report và bàn giao đã được lưu.

| Hạng mục | Kết quả (Pass/Fail/N/A) | Evidence | Owner |
|---|---|---|---|
| | | | |
