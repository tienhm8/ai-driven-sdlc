# Code Review Checklist – Template

> Bản một trang để ghi kết quả và bằng chứng (Pass / Fail / N/A + link/vị trí). Không thay thế đánh giá theo ngữ cảnh. Chi tiết từng khía cạnh: [code-quality](../checklists/code-quality-checklist.md), [security](../checklists/security-checklist.md), [performance](../checklists/performance-checklist.md); điều kiện G4: [merge-approval](../checklists/merge-approval-checklist.md).

## Correctness
- [ ] Thay đổi đáp ứng User Story và Acceptance Criteria.
- [ ] Logic xử lý đúng cả happy path và failure path.
- [ ] Xử lý null, empty, boundary và invalid input.
- [ ] Không phá vỡ behavior hiện hữu ngoài phạm vi dự kiến.

## Design & maintainability
- [ ] Tuân thủ kiến trúc và coding standards.
- [ ] Trách nhiệm module rõ ràng, tránh coupling không cần thiết.
- [ ] Tên, cấu trúc và abstraction dễ hiểu.
- [ ] Không thêm code/dependency không cần thiết.

## Reliability & performance
- [ ] Xử lý exception, timeout, retry và cancellation phù hợp.
- [ ] Không có resource leak hoặc concurrency issue rõ ràng.
- [ ] Query/algorithm phù hợp với quy mô dữ liệu dự kiến.

## Testing
- [ ] Có test cho behavior mới và regression liên quan.
- [ ] Test bao phủ edge case và failure path quan trọng.
- [ ] Test có assertion có ý nghĩa, không phụ thuộc thứ tự/ngẫu nhiên.
- [ ] CI/build/check bắt buộc đạt.

## Security & data
- [ ] Input được validate ở trust boundary.
- [ ] Authentication và authorization được kiểm tra đúng nơi.
- [ ] Không lộ secret, PII hoặc thông tin nhạy cảm.
- [ ] Không có injection hoặc unsafe deserialization rõ ràng.
- [ ] Logging không ghi dữ liệu nhạy cảm.

## Compatibility & release
- [ ] API/schema tương thích hoặc có versioning phù hợp.
- [ ] Migration có kế hoạch an toàn và rollback khi cần.
- [ ] Config/environment changes được tài liệu hóa.
- [ ] G4 có reviewer con người phê duyệt.
