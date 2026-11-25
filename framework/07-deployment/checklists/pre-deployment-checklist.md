# Checklist trước triển khai

## Release và artifact
- [ ] Release scope, owner, version và target environment được xác định rõ.
- [ ] Artifact bất biến và gắn với commit SHA/digest.
- [ ] Đã xác minh artifact source/provenance và chữ ký bắt buộc.
- [ ] Hồ sơ G5 duyệt đúng artifact SHA-256; provenance liên kết đúng kết quả merge G4.
- [ ] API/client compatibility và tiêu chí smoke/health đã được xác nhận.

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

Checklist này chỉ xác nhận readiness, không cấp quyền chạy. Với Production, dùng [kiểm tra quyền thực thi](production-authorization-checklist.md) sau G6.
