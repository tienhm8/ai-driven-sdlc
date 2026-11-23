# 06 – Testing & QA

## Mục tiêu
Xác minh phần mềm đáp ứng yêu cầu đã phê duyệt, hoạt động đúng theo thiết kế, đủ tin cậy và đáp ứng tiêu chí nghiệm thu. Tạo bằng chứng kiểm thử, quản lý defect và khuyến nghị chất lượng trước Gate G5.

## Vai trò
- **AI QA Assistant:** phân tích yêu cầu, đề xuất strategy/plan/case, hỗ trợ test data an toàn, thực thi test được cấp quyền, phân tích kết quả và đề xuất defect.
- **Developer:** cung cấp build/evidence, sửa lỗi và phối hợp xác minh.
- **QA Engineer:** thiết kế/thực hiện test, xác nhận kết quả, quản lý defect và coverage.
- **QA Lead:** đánh giá mức sẵn sàng và khuyến nghị G5.
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
2. Mỗi kết quả gắn với build/version, environment, test data reference và thời điểm.
3. Phân biệt Pass, Fail, Blocked, Skipped, Not Run; không suy diễn test chưa chạy thành Pass.
4. Coverage không chỉ là code coverage; cần đánh giá requirement, risk, scenario và quality attributes.
5. Dùng synthetic/anonymized data; không đưa secret, token, PII hoặc production dump vào môi trường không được phép.
6. AI chỉ thực hiện hành động được cấp quyền; không tự deploy production, thay đổi dữ liệu thật hoặc phê duyệt nghiệm thu.
7. Tự động hóa không thay thế đánh giá và phê duyệt con người.

## Mức tự chủ L1–L4
- **L1:** chạy test đã duyệt, lint, tổng hợp kết quả và kiểm tra định dạng.
- **L2:** sinh test case/script, test data giả lập và đề xuất phân tích defect; con người review theo điều kiện.
- **L3:** thay đổi liên quan nghiệp vụ, security, dữ liệu hoặc tiêu chí nghiệm thu phải được người review/phê duyệt.
- **L4:** QA sign-off, chấp nhận rủi ro, miễn trừ test bắt buộc và nghiệm thu thuộc con người.

L1 vẫn cần log, kết quả máy đọc được và truy vết.

## Human Review Gate G5
Trước nghiệm thu: Acceptance Criteria được xác nhận; test gắn với build cụ thể; có evidence; defect Critical/High được xử lý theo policy; coverage gaps và residual risks được công khai; regression và test bắt buộc hoàn tất; QA Lead đánh giá, Product Owner xác nhận nghiệp vụ. Lưu approver, timestamp, report version, build, environment và quyết định. AI không được tự phê duyệt G5.

## Đầu ra
Test plan, test cases, test data specification, execution report, defect reports, coverage matrix, residual-risk list và QA sign-off. Bàn giao known issues và release-blocking risks cho 07-Deployment.
