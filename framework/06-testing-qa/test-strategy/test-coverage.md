# Test Coverage Strategy

## Mục tiêu
Đánh giá mức độ kiểm thử đối với requirement, risk, luồng nghiệp vụ, code và quality attributes. Coverage là chỉ báo, không bảo đảm không có lỗi.

## Các chiều coverage
1. **Requirement:** mỗi requirement/AC liên kết test case.
2. **Risk:** risk cao có test/mitigation tương ứng.
3. **Scenario:** happy, negative, boundary, alternate, failure path.
4. **Code:** statement/line, branch, function theo công cụ.
5. **API/interface:** endpoint, method, contract, status/error, permission.
6. **Data:** loại dữ liệu, boundary, state, migration, integrity.
7. **Platform:** browser/device/OS/version được hỗ trợ.
8. **Non-functional:** performance, security, accessibility, reliability theo scope.

## Traceability matrix
| Requirement/AC | Risk | Test Case IDs | Execution | Defect IDs | Coverage |
|---|---|---|---|---|---|
| BRQ-0001 | High | TC-001, TC-002 | Pass/Fail/... | BUG-001 | Covered/Partial/Missing |

Requirement quan trọng cần liên kết test và kết quả. Ghi rõ không test được, N/A hoặc Blocked.

## Diễn giải đúng
- Code coverage cao không chứng minh assertion tốt.
- Requirement coverage 100% không chứng minh mọi combination/boundary đã test.
- Pass rate bị ảnh hưởng bởi flaky, skipped và data không đại diện.
- Automation percentage không đồng nghĩa chất lượng cao.
- Số liệu phải kèm mẫu số, phạm vi, build, tool và thời điểm.

## Mục tiêu và gap
QA Lead/project đặt target theo risk, criticality, tiêu chuẩn và khả năng kỹ thuật; không áp ngưỡng chung. Mỗi gap ghi requirement/risk, lý do, impact, mitigation, owner và due date. Gap ảnh hưởng acceptance phải xử lý hoặc được risk owner có thẩm quyền chấp nhận trước G5.
