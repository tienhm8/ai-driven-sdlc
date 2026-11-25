# Human Review – Testing & QA

> **Giai đoạn:** 06 – Testing & QA  
> **Mục đích:** Bảo đảm kiểm thử đủ phù hợp để đánh giá sản phẩm so với yêu cầu, rủi ro và tiêu chí nghiệm thu; kết quả test trung thực, có thể tái lập và truy vết.  
> **Review Gate:** G5 – QA / Acceptance Approval  
> **Người phê duyệt:** QA Lead và Product Owner là hai người riêng biệt; cả hai phê duyệt cùng phiên bản release candidate

## 1. Nguyên tắc review

- Test pass không đồng nghĩa hệ thống không có lỗi; phải xem xét coverage, rủi ro còn lại và giới hạn kiểm thử.
- AI có thể sinh test case, test data và phân tích kết quả; QA xác nhận test có giá trị và phản ánh yêu cầu.
- Không sửa test chỉ để làm pipeline xanh nếu việc sửa làm mất khả năng phát hiện lỗi hoặc thay đổi ý nghĩa Acceptance Criteria.
- Test result phải phản ánh đúng artifact SHA-256, môi trường, dữ liệu và cấu hình đã chạy.
- Không dùng dữ liệu production nhạy cảm trong test nếu chưa có phê duyệt và biện pháp bảo vệ phù hợp.

## 2. Vai trò và trách nhiệm

| Vai trò | Trách nhiệm review / quyết định |
|---|---|
| QA Lead – **Approver G5** | Phê duyệt chiến lược/phạm vi test, đánh giá chất lượng bằng chứng, residual risk và QA sign-off. |
| QA Engineer / Test Engineer | Review test case, test data, test execution, defect và độ bao phủ. |
| Product Owner – **Approver G5 cho nghiệm thu nghiệp vụ** | Xác nhận Acceptance Criteria và quyết định chấp nhận sản phẩm về mặt nghiệp vụ. |
| Developer | Phân tích/sửa defect, cung cấp thông tin kỹ thuật và hỗ trợ kiểm thử; không tự đóng defect nếu chưa đáp ứng quy trình xác nhận. |
| Security Tester / Performance Tester (khi áp dụng) | Đánh giá bảo mật, tải, hiệu năng và các kiểm thử chuyên sâu. |
| Release Manager / Tech Lead | Được tham vấn về release risk, known issues và readiness; không thay QA/PO phê duyệt nội dung thuộc thẩm quyền của họ. |

## 3. Trách nhiệm review của con người

1. **Test traceability:** Test case liên kết với Requirement ID, Acceptance Criteria và risk; xác định yêu cầu chưa có test.
2. **Test strategy:** Mức unit, integration, system, regression, acceptance, security, performance và compatibility phù hợp rủi ro.
3. **Test validity:** Preconditions, steps, expected results và dữ liệu test rõ ràng; test có thể lặp lại.
4. **Coverage:** Đánh giá coverage theo yêu cầu, luồng nghiệp vụ, risk và code; không chỉ dựa vào một con số line coverage.
5. **Test data & environment:** Dữ liệu đại diện, được bảo vệ; môi trường và cấu hình đủ tương đồng với mục tiêu kiểm thử.
6. **Execution evidence:** Log, screenshot, report, build ID, environment và timestamp đủ để xác minh kết quả.
7. **Defect triage:** Xác nhận mức độ nghiêm trọng, phạm vi ảnh hưởng, khả năng tái hiện, priority và owner.
8. **Retest & regression:** Xác nhận fix thực sự giải quyết lỗi và không gây regression ở khu vực liên quan.
9. **Non-functional quality:** Xem xét performance, security, reliability, accessibility, usability và compatibility khi có yêu cầu.
10. **Known issues:** Lỗi còn tồn tại, workaround, tác động và rủi ro được công khai; không che giấu bằng cách loại khỏi báo cáo.
11. **AI-generated tests:** Kiểm tra test không trùng lặp, không phụ thuộc implementation sai, không có expected result tự suy diễn và không bị flaky.
12. **Acceptance readiness:** Kết quả test đủ bằng chứng để QA Lead và PO đưa ra quyết định trong phạm vi thẩm quyền.

## 4. Review theo Autonomy Level

| Level | Cách con người tham gia |
|---|---|
| L1 | AI có thể chạy test suite đã được phê duyệt, tổng hợp report và phân loại log; pipeline phải lưu kết quả và build context. |
| L2 | QA review theo mẫu/điều kiện đối với test case sinh tự động, test bổ sung hoặc phân tích lỗi rủi ro thấp. |
| L3 | QA bắt buộc review và phê duyệt test scope, kết quả, defect disposition và bằng chứng nghiệm thu trước G5. |
| L4 | QA Lead và PO quyết định G5 trong phạm vi vai trò; người có thẩm quyền theo policy quyết định ngoại lệ/risk acceptance. AI chỉ tư vấn. |

## 5. Checklist G5

Dùng [checklist QA sign-off](checklists/qa-signoff-checklist.md) làm danh sách kiểm tra duy nhất.

## 6. Điều kiện quyết định G5

Áp dụng [quy tắc G5](../governance/human-review-gates/G5-qa-approval.md) về điều kiện chặn, ngoại lệ và hai phê duyệt bắt buộc trên cùng artifact và gói review. QA Lead đánh giá chất lượng bằng chứng; Product Owner xác nhận nghiệm thu nghiệp vụ. CI xanh, code coverage cao hay Conditional Go không thay được quyết định G5.

## 7. Khi yêu cầu AI làm lại

QA cung cấp test ID, artifact SHA-256, environment, dữ liệu đã dùng (đã loại bỏ dữ liệu nhạy cảm), kết quả thực tế/mong đợi và bước tái hiện. AI có thể đề xuất test/fix; QA xác minh test và kết quả trên đúng artifact SHA-256 và cấu hình đã ghi nhận. Developer sửa lỗi nhưng QA xác nhận retest.

## 8. Bằng chứng và hồ sơ review

Lưu [hồ sơ Stage 06 của dự án](outputs/README.md), gồm test plan/version, traceability, định danh artifact và provenance, execution/coverage report, defect và retest evidence, known issues và hồ sơ G5 cho đúng gói review.

## 9. Trách nhiệm cuối cùng

QA Lead chịu trách nhiệm về đánh giá chất lượng và QA sign-off. PO chịu trách nhiệm quyết định nghiệm thu nghiệp vụ. Developer chịu trách nhiệm xử lý defect theo phân công. AI không được tự tuyên bố sản phẩm đạt nghiệm thu.
