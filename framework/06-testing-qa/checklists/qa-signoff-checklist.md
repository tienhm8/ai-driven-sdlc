# QA Sign-off Checklist – G5

Áp dụng [quy tắc G5](../../governance/human-review-gates/G5-qa-approval.md).

## Trước khi trình G5
- [ ] Strategy, scope, exit criteria và test cases phù hợp rủi ro; kết quả có thể tái lập.
- [ ] Test bắt buộc (gồm regression và non-functional khi áp dụng) đã chạy và đạt tiêu chí trên đúng artifact SHA-256; ghi môi trường, cấu hình và tham chiếu test data.
- [ ] Acceptance Criteria bắt buộc đạt và có evidence; coverage theo requirement/risk, gaps, Blocked/Skipped/Not Run và flaky test được công khai. Test chưa chạy không tính Pass.
- [ ] Defect có severity, impact, owner và disposition; fix đã retest/regression; lỗi còn mở đáp ứng quy tắc chặn/ngoại lệ G5.
- [ ] Nếu đã loại phần bị ảnh hưởng khỏi phạm vi: gói review có tham chiếu yêu cầu thay đổi, quyết định của PO và phiên bản phạm vi phát hành đã duyệt; nếu có thay đổi triển khai, ghi thêm tham chiếu G4 và bằng chứng kiểm thử mới. QA đã xác minh phần đó không thể sử dụng hoặc kích hoạt; nếu dùng feature flag, ghi cấu hình đích và bằng chứng retest/regression trên đúng artifact và cấu hình đó để G6 đối chiếu.
- [ ] Nếu đã phân loại lại Critical: gói review ghi severity cũ/mới, lý do, bằng chứng mới và người quyết định theo policy để QA Lead và PO cùng kiểm tra.
- [ ] Known issues, residual risks và ngoại lệ có hồ sơ; tiêu chí smoke được thống nhất với Deployment trước bàn giao.
- [ ] Execution report và gói review truy vết đến cùng artifact SHA-256, merge G4 và provenance đã xác minh; gói review có tham chiếu và SHA-256.

## Trước khi đóng G5
- [ ] QA Lead ghi khuyến nghị và quyết định về chất lượng; Product Owner ghi quyết định về nghiệm thu nghiệp vụ.
- [ ] Nếu G5 thông qua, hai người riêng biệt đều Approve cùng artifact và gói review; lưu review ID, quyết định, timestamp, phiên bản report và bằng chứng audit.
- [ ] AI không tự phê duyệt gate; G5 không cấp quyền triển khai production.
