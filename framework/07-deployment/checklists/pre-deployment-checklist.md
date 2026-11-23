# Checklist trước triển khai

## Release và artifact
- [ ] Release scope, owner, version và target environment được xác định rõ.
- [ ] Artifact bất biến và gắn với commit SHA/digest.
- [ ] Đã xác minh artifact source/provenance và chữ ký bắt buộc.
- [ ] Phê duyệt G4 và G5 tham chiếu đúng release candidate.

## Môi trường
- [ ] Capacity/quota và dependencies ở trạng thái khỏe.
- [ ] Giá trị cấu hình đúng theo môi trường và đã được review.
- [ ] Secrets lấy từ secret manager được phê duyệt; không có plaintext.
- [ ] IAM, service account và quyền deploy tuân thủ least privilege.
- [ ] DNS, certificate, network rules và endpoints đã sẵn sàng.

## Dữ liệu và an toàn
- [ ] Thứ tự migration và khả năng tương thích đã được review.
- [ ] Yêu cầu và evidence backup/restore còn hiệu lực.
- [ ] Rủi ro mất dữ liệu và side-effect bên ngoài đã được ghi nhận.
- [ ] Rollback/mitigation plan được version hóa và có thể thực thi.

## Vận hành
- [ ] Monitoring, alerting, dashboards và logs truy cập được.
- [ ] On-call và escalation contacts đã được gán.
- [ ] Maintenance window và thông báo cho stakeholder đã sẵn sàng.
- [ ] G6 approval đã được ghi nhận trước khi thực thi trên Production.
