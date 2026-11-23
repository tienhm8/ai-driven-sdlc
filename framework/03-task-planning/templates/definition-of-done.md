# Mẫu Definition of Done
| Dự án | ID/phiên bản DoD | Áp dụng cho | Owner | Người phê duyệt | Ngày có hiệu lực |
|---|---|---|---|---|---|
| | | `Task/Story/Sprint/Release` | | | |

## Tiêu chí hoàn thành
- [ ] Requirement/AC được đáp ứng; không có thay đổi scope chưa được phê duyệt.
- [ ] Các edge case và error path đã được xử lý.
- [ ] Tuân thủ coding standard và architecture.
- [ ] Peer review và các phê duyệt bắt buộc đã hoàn tất.
- [ ] Static analysis/lint đạt chính sách.
- [ ] Các test unit/integration/API/E2E/regression liên quan đều pass.
- [ ] Bằng chứng test đã được liên kết.
- [ ] Không còn finding Critical/High nào chưa xử lý, trừ khi được miễn trừ chính thức.
- [ ] Đã kiểm tra authorization/input validation và xử lý dữ liệu nhạy cảm.
- [ ] Đã xử lý migration/backward compatibility khi có liên quan.
- [ ] Tài liệu API/kỹ thuật đã được cập nhật.
- [ ] Đã xem xét logging/metrics/tracing và ghi chú triển khai.

| Tiêu chí | Có áp dụng? | Bằng chứng | Lý do ngoại lệ | Phê duyệt bởi |
|---|---|---|---|---|
| | `Yes/No` | | | |

Với mục N/A, phải ghi lý do; không được bỏ qua âm thầm. DoD không thay thế G4 code review, G5 QA acceptance hay G6 release approval.

| Phiên bản | Thay đổi | Tác giả | Người phê duyệt | Ngày |
|---|---|---|---|---|
| 1.0 | Khởi tạo | | | |
