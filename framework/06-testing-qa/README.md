# 06 – Testing & QA

## Mục tiêu
Xác minh phần mềm đáp ứng yêu cầu đã phê duyệt, hoạt động đúng theo thiết kế, đủ tin cậy và đáp ứng tiêu chí nghiệm thu. Tạo bằng chứng kiểm thử, quản lý defect và khuyến nghị chất lượng trước Gate G5.

## Vai trò
- **AI QA Assistant:** phân tích yêu cầu, đề xuất strategy/plan/case, hỗ trợ test data an toàn, thực thi test được cấp quyền, phân tích kết quả và đề xuất defect.
- **Developer:** cung cấp build/evidence, sửa lỗi và phối hợp xác minh.
- **QA Engineer:** thiết kế/thực hiện test, xác nhận kết quả, quản lý defect và coverage.
- **QA Lead:** đánh giá mức sẵn sàng, ghi khuyến nghị QA và quyết định chất lượng tại G5.
- **Product Owner:** xác nhận Acceptance Criteria và nghiệm thu nghiệp vụ.

## Cấu trúc
- `workflow.md`: quy trình từ intake đến G5.
- `ai-instructions.md`: chỉ dẫn và giới hạn cho AI.
- `human-review.md`: trách nhiệm và phê duyệt.
- `test-strategy/`: test levels, environment, coverage.
- `templates/`: test plan/case/data, bug, execution report, sign-off.
- `checklists/`: readiness, functional, non-functional, regression, defect, sign-off.
- `inputs/`: tài liệu tham chiếu từ giai đoạn 01–05 và build.
- `outputs/`: báo cáo, bằng chứng và kết quả giai đoạn 06.

## Nguyên tắc
1. Truy vết Requirement/AC → Test Case → Execution → Defect → Sign-off.
2. Mỗi kết quả gắn với artifact SHA-256, TESTRUN, environment, test data reference và thời điểm.
3. Phân biệt Pass, Fail, Blocked, Skipped, Not Run; không suy diễn test chưa chạy thành Pass.
4. Coverage không chỉ là code coverage; cần đánh giá requirement, risk, scenario và quality attributes.
5. Dùng synthetic/anonymized data; không đưa secret, token, PII hoặc production dump vào môi trường không được phép.
6. AI chỉ thực hiện hành động được cấp quyền; không tự deploy production, thay đổi dữ liệu thật hoặc phê duyệt nghiệm thu.
7. Tự động hóa không thay thế đánh giá và phê duyệt con người.

## Mức tự chủ L1–L4
- **L1:** chạy test đã duyệt, lint, tổng hợp kết quả và kiểm tra định dạng.
- **L2:** sinh test case/script, test data giả lập và đề xuất phân tích defect; con người review theo điều kiện.
- **L3:** thay đổi liên quan nghiệp vụ, security, dữ liệu hoặc tiêu chí nghiệm thu phải được người review/phê duyệt.
- **L4:** QA sign-off, chấp nhận rủi ro, ngoại lệ được policy cho phép và nghiệm thu thuộc con người.

L1 vẫn cần log, kết quả máy đọc được và truy vết.

## Human Review Gate G5
Theo [quy tắc G5](../governance/human-review-gates/G5-qa-approval.md), QA Lead và Product Owner là hai người riêng biệt, phê duyệt cùng release candidate và gói review. Critical còn mở trong phạm vi phát hành chặn G5; High chỉ có ngoại lệ theo policy. Khuyến nghị QA không phải quyết định G5; G5 không cấp quyền production. AI không được tự phê duyệt G5.

## Đầu ra
Test plan, test cases, test data specification, execution report, defect reports, coverage matrix, residual-risk list và QA sign-off. Khi G5 thông qua, [bàn giao cho Deployment](../07-deployment/inputs/README.md) artifact đã duyệt, hồ sơ G5, bằng chứng test, known issues/residual risks và tiêu chí smoke.
