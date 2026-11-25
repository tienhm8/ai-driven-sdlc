# Workflow — Testing & QA

> Tài liệu workflow cấp framework cho giai đoạn này. Tuân thủ governance, standards và template dùng chung trong `framework/`; các cấu hình riêng của dự án được kế thừa từ `projects/<Project>/.ai-sdlc/`.

# 6. Giai đoạn 06 — Testing & QA

## 6.1 Purpose — Mục đích

Xác minh độc lập sản phẩm đáp ứng requirement, acceptance criteria, NFR và mức chất lượng đã thống nhất. Phát hiện, phân loại, theo dõi defect; cung cấp bằng chứng khách quan để quyết định release readiness.

## 6.2 Workflow Overview — Tổng quan luồng xử lý

```text
Reviewed Build / Integrated Candidate
        ↓
Test Strategy & Environment Readiness
        ↓
Test Design & Test Data
        ↓
Execute Functional / Non-functional Tests
        ↓
Defect Management & Retest / Regression
        ↓
Quality Assessment
        ↓
G5 — QA / Release Candidate Approval
        ↓
Handoff to Deployment
```

## 6.3 Intake — Điều kiện vào giai đoạn

- Có requirement baseline, Acceptance Criteria và release scope đã duyệt.
- Có kết quả merge G4 đã xác minh và release candidate tích hợp: URI/version, SHA-256 và provenance đã xác minh liên kết digest với repository và merge commit G4. Ghi vào [intake record](inputs/README.md).
- Strategy, plan, môi trường, dữ liệu và quyền truy cập được chuẩn bị trong giai đoạn này. Trước execution, dùng [Test Readiness Checklist](checklists/test-readiness-checklist.md).

## 6.4 Workflow Steps — Các bước thực hiện

1. **Xác nhận test scope:** xác định build, requirement, feature, platform, browser/device và loại test.
2. **Rà soát traceability:** map requirement/acceptance criteria tới test cases; nhận diện coverage gap.
3. **Chuẩn bị môi trường:** xác nhận config, service dependency, test account, data, observability và environment parity.
4. **Thiết kế test:** xây dựng test scenario/case cho positive, negative, boundary, integration, regression và exploratory testing.
5. **Review test design:** QA/BA/Developer xác nhận expected result và testability.
6. **Thực thi functional tests:** bắt đầu sau khi đạt readiness checklist. Có thể dùng evidence unit/component từ CI/04 nếu truy vết được và chỉ chạy lại khi test plan hoặc rủi ro yêu cầu. Evidence trước merge không thay thế kiểm thử bắt buộc trên release candidate.
7. **Thực thi non-functional tests:** performance, load/stress, security, accessibility, usability, reliability hoặc compatibility khi áp dụng.
8. **Thu thập evidence:** log, screenshot, report, trace, metrics và version; bảo vệ dữ liệu nhạy cảm.
9. **Quản lý defect:** tạo ticket có steps, expected/actual, environment, severity, priority và evidence.
10. **Fix và retest:** Developer sửa; QA retest và xác nhận trạng thái theo luồng rework tại mục 6.12.
11. **Regression testing:** kiểm tra vùng ảnh hưởng và chức năng liên quan; cập nhật regression suite.
12. **Đánh giá chất lượng:** tổng hợp pass/fail, defect trend, coverage, residual risk và known limitations.
13. **Lập QA recommendation:** đề xuất Go / No-Go / Conditional Go / Blocked theo quy tắc G5; chỉ là khuyến nghị.
14. **Trình G5:** review bằng chứng và phê duyệt release candidate.

## 6.5 Input — Đầu vào

- Release candidate tích hợp và intake record chứa định danh artifact, bằng chứng merge G4 và provenance đã xác minh.
- Requirement baseline, RTM, acceptance criteria.
- Test strategy, test plan, test cases, automation suite, môi trường, test accounts và test data: dùng lại nếu có, hoàn thiện trước execution.
- Review findings, risk register và change impact.
- NFR targets và security/compliance requirements.

## 6.6 AI Activities — Hoạt động AI

- Phân tích requirement để đề xuất test scenario/case và edge cases.
- Kiểm tra coverage requirement → test và phát hiện gap.
- Sinh test data tổng hợp/an toàn, script và automation skeleton.
- Hỗ trợ phân tích log, stack trace, flaky test và defect clustering.
- Tóm tắt test run, xu hướng defect và residual risk.
- Đề xuất regression scope dựa trên changed files/dependency map.
- Hỗ trợ phân tích kết quả performance/security scan nhưng không tự xác nhận compliance.
- Không tự đóng defect hoặc tuyên bố release-ready nếu thiếu evidence và approval.

## 6.7 Human Activities — Hoạt động con người

- QA Lead chịu trách nhiệm test strategy, execution và quality recommendation.
- QA Engineer thiết kế/thực thi test và xác nhận defect.
- Developer phân tích, sửa lỗi và cung cấp build mới.
- BA/PO xác nhận behavior và acceptance.
- Security/Performance specialist đánh giá các test chuyên sâu.
- Người có thẩm quyền theo policy xem xét residual risk; không thay QA Lead hoặc PO phê duyệt G5.

## 6.8 Output — Đầu ra

- Test Plan/Test Strategy và test cases.
- Requirement-to-test traceability/coverage report.
- Test execution report và evidence.
- Defect log, retest và regression report.
- Performance/security/accessibility reports khi áp dụng.
- Known issues, residual risks và QA recommendation.
- Release candidate đã duyệt, hồ sơ G5 và tiêu chí smoke đã thống nhất với 07. Lưu theo [quy ước hồ sơ dự án](outputs/README.md).

## 6.9 Quality Check — Kiểm tra chất lượng

- Test chạy trên đúng artifact SHA-256 và môi trường đã ghi nhận.
- Requirement quan trọng có test evidence.
- Áp dụng [quy tắc chặn và ngoại lệ G5](../governance/human-review-gates/G5-qa-approval.md).
- Regression phù hợp với phạm vi thay đổi.
- Test data không vi phạm privacy/security.
- NFR được đánh giá theo target/threshold đã duyệt.
- Test report có pass/fail/blocked và lý do; không che giấu test bị bỏ qua.
- Known limitations và residual risks có owner.

## 6.10 Human Review Gate — Điểm phê duyệt bắt buộc

Áp dụng [quy tắc G5](../governance/human-review-gates/G5-qa-approval.md) và [checklist sign-off](checklists/qa-signoff-checklist.md). QA Lead và Product Owner là hai người riêng biệt, duyệt cùng artifact và cùng gói review. Khuyến nghị QA không phải quyết định gate; G5 duyệt ứng viên phát hành, còn G6 mới cấp quyền triển khai production.

## 6.11 Exit Criteria — Điều kiện hoàn thành

- G5 được Approved cho release candidate cụ thể.
- Artifact SHA-256, test evidence và SHA-256 gói review đã duyệt được lưu và truy vết.
- Defect còn mở có quyết định và owner.
- Deployment nhận đủ gói bàn giao ở mục 6.13.

## 6.12 Exception Handling — Xử lý ngoại lệ

- **Môi trường test không ổn định:** phân biệt environment issue với product defect; ghi nhận test blocked và kế hoạch chạy lại.
- **Thiếu test data:** tạo data tổng hợp hoặc xin phê duyệt nguồn dữ liệu; không dùng dữ liệu production tùy tiện.
- **Defect Critical còn mở trong phạm vi phát hành:** No-Go; escalate và áp dụng [cách gỡ chặn theo quy tắc G5](../governance/human-review-gates/G5-qa-approval.md#cách-gỡ-chặn-đối-với-critical).
- **Fix đổi source:** quay lại **04 → 05/G4 mới → merge đã xác minh → build mới → QA retest/regression theo tác động → G5 mới**. Từ QA hoặc Deployment, dùng `return_to_development` để ghi lý do và vô hiệu hóa các phê duyệt bị ảnh hưởng.
- **Digest đổi dù source không đổi:** xác minh provenance của bản mới, kiểm thử trên bản đó và trình G5 mới trước G6. Từ Deployment, dùng `return_to_qa` khi không có production authorization đang chờ kết quả; không dùng lại G5/G6 cũ. Nếu chỉ đổi gói review trong QA, trình lại G5 với SHA-256 gói mới.
- **Không đạt NFR:** đánh giá scope/architecture trade-off; chỉ áp dụng ngoại lệ nếu policy cho phép và người có thẩm quyền phê duyệt.
- **Flaky test:** phân tích nguyên nhân, quarantine có kiểm soát và không tính pass giả.
- **Deadline gấp:** đề xuất risk-based test scope; chỉ ghi ngoại lệ theo policy; không bỏ qua tiêu chí bắt buộc hoặc hai phê duyệt G5.

## 6.13 Next Stage — Chuyển sang giai đoạn tiếp theo

Bàn giao cho [07 — Deployment](../07-deployment/inputs/README.md):

- Artifact bất biến đã duyệt: URI/version, SHA-256, provenance và tham chiếu merge G4.
- Hồ sơ G5: quyết định, hai phê duyệt, tham chiếu và SHA-256 gói review.
- Test report, coverage, defect status và bằng chứng retest/regression.
- Known issues, residual risks, quyết định ngoại lệ, cấu hình đã xác minh nếu dùng để loại phần bị ảnh hưởng khỏi scope, và tiêu chí smoke đã thống nhất với Deployment.

Deployment dùng gói này để lập release notes và chuẩn bị cấu hình triển khai; Stage 06 không chịu trách nhiệm phát hành release notes hay cấu hình production.

---
