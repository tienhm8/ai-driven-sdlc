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

## 6.3 Entry Criteria — Điều kiện bắt đầu

- Thay đổi đã được G4 phê duyệt và merge theo policy; QA nhận merge commit SHA đã xác minh và link bằng chứng merge theo [quy ước intake](inputs/README.md).
- Có release scope và build/version xác định để kiểm thử; build dùng làm bằng chứng G5 phải truy vết được về kết quả merge đã xác minh.
- Requirement baseline, acceptance criteria, test strategy và test environment sẵn sàng.
- Test data được chuẩn bị hợp pháp, an toàn và có khả năng tái tạo.
- Các dependency ngoài và test account cần thiết được xác nhận.

## 6.4 Workflow Steps — Các bước thực hiện

1. **Xác nhận test scope:** xác định build, requirement, feature, platform, browser/device và loại test.
2. **Rà soát traceability:** map requirement/acceptance criteria tới test cases; nhận diện coverage gap.
3. **Chuẩn bị môi trường:** xác nhận config, service dependency, test account, data, observability và environment parity.
4. **Thiết kế test:** xây dựng test scenario/case cho positive, negative, boundary, integration, regression và exploratory testing.
5. **Review test design:** QA/BA/Developer xác nhận expected result và testability.
6. **Thực thi functional tests:** unit/integration/system/API/UI/E2E theo test strategy và scope.
7. **Thực thi non-functional tests:** performance, load/stress, security, accessibility, usability, reliability hoặc compatibility khi áp dụng.
8. **Thu thập evidence:** log, screenshot, report, trace, metrics và version; bảo vệ dữ liệu nhạy cảm.
9. **Quản lý defect:** tạo ticket có steps, expected/actual, environment, severity, priority và evidence.
10. **Fix và retest:** developer sửa; QA retest defect và xác nhận trạng thái.
11. **Regression testing:** kiểm tra vùng ảnh hưởng và chức năng liên quan; cập nhật regression suite.
12. **Đánh giá chất lượng:** tổng hợp pass/fail, defect trend, coverage, residual risk và known limitations.
13. **Lập QA recommendation:** đề xuất Go/No-Go/Conditional Go theo tiêu chí đã thống nhất.
14. **Trình G5:** review bằng chứng và phê duyệt release candidate.

## 6.5 Input — Đầu vào

- Integrated build/release candidate, phiên bản và bằng chứng liên kết build với merge commit SHA đã xác minh.
- Requirement baseline, RTM, acceptance criteria.
- Test strategy, test plan, test cases và automation suite.
- Environment/configuration, test accounts và test data.
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
- Release owner xem xét residual risk và điều kiện phát hành.

## 6.8 Output — Đầu ra

- Test Plan/Test Strategy và test cases.
- Requirement-to-test traceability/coverage report.
- Test execution report và evidence.
- Defect log, retest và regression report.
- Performance/security/accessibility reports khi áp dụng.
- Known issues, residual risks và QA recommendation.
- Approved Release Candidate và G5 approval record.

## 6.9 Quality Check — Kiểm tra chất lượng

- Test chạy trên đúng build/version và môi trường đã ghi nhận.
- Requirement quan trọng có test evidence.
- Critical/High defects được xử lý hoặc risk-accepted rõ ràng.
- Regression phù hợp với phạm vi thay đổi.
- Test data không vi phạm privacy/security.
- NFR được đánh giá theo target/threshold đã duyệt.
- Test report có pass/fail/blocked và lý do; không che giấu test bị bỏ qua.
- Known limitations và residual risks có owner.

## 6.10 Human Review Gate — Điểm phê duyệt bắt buộc

**G5 — QA & Release Candidate Approval**

Hai người phê duyệt độc lập: QA Lead xác nhận bằng chứng kiểm thử và Product Owner xác nhận nghiệm thu nghiệp vụ trên cùng release candidate. Security/Compliance tham gia khi cần.

Điều kiện:
- Acceptance criteria và test scope bắt buộc đạt.
- Không còn defect vượt ngưỡng release policy.
- Test evidence, coverage và residual risk được trình bày.
- Conditional Go (nếu có) phải nêu rõ điều kiện, owner, thời hạn và risk acceptance.

## 6.11 Exit Criteria — Điều kiện hoàn thành

- G5 được Approved cho release candidate cụ thể.
- Build/version và test report được khóa, truy vết.
- Defect còn mở có quyết định và owner.
- Deployment team nhận đủ release notes, configuration và known issues.

## 6.12 Exception Handling — Xử lý ngoại lệ

- **Môi trường test không ổn định:** phân biệt environment issue với product defect; ghi nhận test blocked và kế hoạch chạy lại.
- **Thiếu test data:** tạo data tổng hợp hoặc xin phê duyệt nguồn dữ liệu; không dùng dữ liệu production tùy tiện.
- **Defect critical:** No-Go, tạo incident/defect escalation và retest sau fix.
- **Không đạt NFR:** đánh giá scope/architecture trade-off; chỉ chấp nhận ngoại lệ qua risk owner.
- **Flaky test:** phân tích nguyên nhân, quarantine có kiểm soát và không tính pass giả.
- **Deadline gấp:** đề xuất risk-based test scope; PO/Release Owner phải chấp thuận residual risk bằng văn bản.

## 6.13 Next Stage — Chuyển sang giai đoạn tiếp theo

Bàn giao release candidate, QA approval, test reports, deployment prerequisites, release notes và known issues cho **07 — Deployment**.

---
