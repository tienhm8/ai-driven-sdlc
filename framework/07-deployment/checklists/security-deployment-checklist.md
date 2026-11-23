# Checklist bảo mật triển khai

- [ ] Deploy identity của Production tách biệt với tài khoản cá nhân khi có thể.
- [ ] Áp dụng least privilege và credential ngắn hạn.
- [ ] Secrets không được nhúng trong images, source, logs hoặc artifacts.
- [ ] Provenance, dependency và image scan của artifact đạt policy.
- [ ] Images/packages được pin vào version/digest bất biến đã phê duyệt.
- [ ] Network exposure, ingress, firewall và security groups đã được review.
- [ ] TLS certificates và secure transport còn hợp lệ.
- [ ] Debug mode, sample credentials và development endpoints đã bị tắt.
- [ ] Security headers và cấu hình bảo mật Production đúng.
- [ ] Dữ liệu nhạy cảm không bị lộ trong logs, metrics hoặc deployment output.
- [ ] Audit logging ghi nhận các hành động deploy có đặc quyền.
- [ ] Mọi ngoại lệ bảo mật có người phê duyệt, lý do và ngày hết hạn.
