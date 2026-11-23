# G5 – Testing & QA Approval

**Thời điểm:** Sau Testing & QA, trước nghiệm thu/release handoff.  
**Approvers (hai người riêng biệt):** QA Lead xác nhận chất lượng kiểm thử; Product Owner xác nhận đáp ứng nghiệp vụ/nghiệm thu. Cả hai duyệt cùng một phiên bản release candidate.

## AI chuẩn bị
Test plan/cases, execution results, coverage, defect list, regression evidence, NFR test results và known limitations.

## Điều kiện thông qua
- [ ] Test cases truy vết tới Acceptance Criteria.
- [ ] Test bắt buộc chạy trên build/version xác định.
- [ ] Không còn defect nghiêm trọng chưa có quyết định xử lý.
- [ ] Regression/integration test phù hợp hoàn tất.
- [ ] Coverage đánh giá theo rủi ro, không chỉ theo một tỷ lệ tổng.
- [ ] NFR/security/performance test hoàn tất khi thuộc phạm vi.
- [ ] Known issues và residual risks công khai.
- [ ] PO xác nhận tiêu chí nghiệp vụ nghiệm thu.

**Decision:** Approve / Reject / Blocked. Test pass tự động không tự tạo approval G5.  
**Audit:** Build/version, test run, environment, report, defect disposition, QA/PO approver và timestamp.
