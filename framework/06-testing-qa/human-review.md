# Human Review – Testing & QA

> **Giai đoạn:** 06 – Testing & QA  
> **Mục đích:** Bảo đảm kiểm thử đủ phù hợp để đánh giá sản phẩm so với yêu cầu, rủi ro và tiêu chí nghiệm thu; kết quả test trung thực, có thể tái lập và truy vết.  
> **Review Gate:** G5 – QA / Acceptance Approval  
> **Người phê duyệt chính:** QA Lead; Product Owner xác nhận nghiệm thu nghiệp vụ theo phạm vi dự án

## 1. Nguyên tắc review

- Test pass không đồng nghĩa hệ thống không có lỗi; phải xem xét coverage, rủi ro còn lại và giới hạn kiểm thử.
- AI có thể sinh test case, test data và phân tích kết quả; QA xác nhận test có giá trị và phản ánh yêu cầu.
- Không sửa test chỉ để làm pipeline xanh nếu việc sửa làm mất khả năng phát hiện lỗi hoặc thay đổi ý nghĩa Acceptance Criteria.
- Test result phải phản ánh đúng build, môi trường, dữ liệu và cấu hình đã chạy.
- Không dùng dữ liệu production nhạy cảm trong test nếu chưa có phê duyệt và biện pháp bảo vệ phù hợp.

## 2. Vai trò và trách nhiệm

| Vai trò | Trách nhiệm review / quyết định |
|---|---|
| QA Lead – **Approver G5** | Phê duyệt chiến lược/phạm vi test, đánh giá chất lượng bằng chứng, residual risk và QA sign-off. |
| QA Engineer / Test Engineer | Review test case, test data, test execution, defect và độ bao phủ. |
| Product Owner – nghiệm thu nghiệp vụ | Xác nhận Acceptance Criteria và quyết định chấp nhận sản phẩm về mặt nghiệp vụ. |
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
| L4 | QA Lead/PO quyết định chấp nhận residual risk, waiver, ngoại lệ chất lượng và nghiệm thu nghiệp vụ quan trọng; AI chỉ tư vấn. |

## 5. Checklist G5

- [ ] Test strategy và phạm vi test phù hợp với risk.
- [ ] Các Acceptance Criteria trọng yếu có test/evidence tương ứng.
- [ ] Test case rõ ràng, hợp lệ, có thể tái lập.
- [ ] Unit/integration/system/regression test phù hợp đã chạy.
- [ ] Security/performance/compatibility test đã thực hiện khi được yêu cầu.
- [ ] Test environment, build và test data được ghi nhận.
- [ ] Coverage gap và giới hạn kiểm thử được công khai.
- [ ] Defect được phân loại, có owner và trạng thái chính xác.
- [ ] Defect nghiêm trọng đã được xử lý hoặc có quyết định ngoại lệ đúng thẩm quyền.
- [ ] Fix đã retest và regression test phù hợp.
- [ ] Known issues và residual risks được ghi nhận.
- [ ] QA report và sign-off gắn với đúng build/version.
- [ ] PO đã xác nhận nghiệm thu nghiệp vụ khi cần.

## 6. Điều kiện quyết định G5

**QA sign-off** khi phạm vi test được thực hiện theo kế hoạch hoặc deviation được giải thích; bằng chứng đủ tin cậy; không còn defect vượt ngưỡng chấp nhận; coverage gap và residual risk được công khai.

**Acceptance approval** là quyết định riêng của PO hoặc người được ủy quyền, dựa trên Acceptance Criteria và các rủi ro đã biết.

Không mặc định G5 đạt chỉ vì CI xanh hoặc test coverage vượt một ngưỡng. Ngưỡng defect/coverage phải được quy định theo loại dự án và risk profile. Không được che giấu defect nghiêm trọng hoặc tự hạ severity để thông qua Gate.

## 7. Khi yêu cầu AI làm lại

QA cung cấp test ID, build/environment, dữ liệu đã dùng (đã loại bỏ dữ liệu nhạy cảm), kết quả thực tế/mong đợi và bước tái hiện. AI có thể đề xuất test/fix; QA xác minh test và kết quả trên đúng build. Developer sửa lỗi nhưng QA xác nhận retest.

## 8. Bằng chứng và hồ sơ review

Lưu test plan/version, test case và traceability, build ID, environment/config, execution report, coverage report, defect register, retest evidence, known issues, QA sign-off và PO acceptance record.

## 9. Trách nhiệm cuối cùng

QA Lead chịu trách nhiệm về đánh giá chất lượng và QA sign-off. PO chịu trách nhiệm quyết định nghiệm thu nghiệp vụ. Developer chịu trách nhiệm xử lý defect theo phân công. AI không được tự tuyên bố sản phẩm đạt nghiệm thu.
