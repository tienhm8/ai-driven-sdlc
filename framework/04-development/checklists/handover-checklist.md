# PR Readiness Check — bàn giao 04 → 05

Dùng checklist này để kiểm gói bàn giao và ghi kết quả theo [quy tắc PR Readiness Check](../workflow.md#410-pr-readiness-check--bàn-giao-04--05). Kiểm chất lượng triển khai và self-review tại [Implementation DoD](implementation-dod.md).

## Gói bàn giao

- [ ] Có PR/MR, mô tả thay đổi và liên kết task, requirement, thiết kế.
- [ ] Có `Base SHA` và `Head SHA` của phiên bản bàn giao.
- [ ] Có tham chiếu Implementation DoD, implementation summary, test evidence và tài liệu liên quan.
- [ ] Evidence ghi rõ SHA đã kiểm tra và đủ để xác minh kết quả bắt buộc cho phiên bản bàn giao; có link ngoại lệ đã duyệt nếu áp dụng.
- [ ] Đã gán reviewer theo policy và kiểm tra reviewer truy cập được PR và evidence.
- [ ] Đã công bố known issues, giới hạn, rủi ro và các tác động cần theo dõi (ví dụ migration, cấu hình, rollback); không ghi giá trị secret.

## Kết quả bàn giao

**PR/MR và phiên bản (link gói bàn giao có Base SHA / Head SHA):**

**Kết quả:** Ready for Review / Blocked

**Developer xác nhận / ngày:**

**Tech Lead/maintainer xác nhận / ngày (nếu policy dự án yêu cầu):**

**Blocker / owner / hạn xử lý (nếu Blocked):**

Không ghi `G4 Approved` ở Stage 04. Reviewer có thẩm quyền quyết định G4 ở Stage 05.
