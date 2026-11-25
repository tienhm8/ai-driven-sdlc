# Security Checklist

> Kiểm tra nhanh mọi PR có rủi ro bảo mật. Với thay đổi nhạy cảm, dùng thêm [security-review](../templates/security-review.md) (trust boundary, bằng chứng, kết luận chuyên môn).

- [ ] Authentication được áp dụng cho endpoint/chức năng cần bảo vệ.
- [ ] Authorization kiểm tra quyền trên từng resource/action phù hợp.
- [ ] Input được validate server-side; output được encode đúng ngữ cảnh.
- [ ] Không có injection, path traversal, SSRF hoặc deserialization không an toàn.
- [ ] Secret/key không hardcode hoặc ghi vào log.
- [ ] Dữ liệu nhạy cảm được bảo vệ khi truyền, lưu và hiển thị.
- [ ] Error response không tiết lộ stack trace hoặc thông tin nội bộ.
- [ ] Dependency mới có nguồn gốc và phiên bản được chấp nhận.
- [ ] Thay đổi security-sensitive có chuyên gia/con người review.
