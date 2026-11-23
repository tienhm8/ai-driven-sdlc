# Test Levels & Types

## Test levels
| Level | Mục tiêu | Ví dụ | Owner thường gặp |
|---|---|---|---|
| Unit | Xác minh đơn vị nhỏ độc lập | Function/class | Developer |
| Component | Xác minh module/service | Service với dependency giả lập | Developer/QA |
| Integration | Xác minh tương tác | API–DB, service, broker | Developer/QA |
| System | Xác minh hệ thống theo yêu cầu | Workflow end-to-end | QA |
| Acceptance | Xác nhận nhu cầu/AC | UAT, business scenario | QA/PO/user đại diện |

Tên gọi và ranh giới có thể điều chỉnh theo kiến trúc; test plan phải định nghĩa rõ.

## Test types
- Functional: behavior, business rules, validation, error handling.
- Regression: bảo đảm thay đổi không phá behavior hiện có.
- Smoke: kiểm tra nhanh chức năng cốt lõi sau build/deploy.
- Sanity: kiểm tra tập trung vùng vừa thay đổi.
- Exploratory: khám phá có charter, ghi nhận quan sát.
- Performance: load/stress/spike/endurance theo mục tiêu được duyệt.
- Security: authentication, authorization, input, dependency và threat-specific checks.
- Compatibility: browser, OS, device, API/client version.
- Usability/accessibility: theo tiêu chuẩn dự án.
- Reliability/resilience: timeout, retry, failover, recovery khi phù hợp.

## Lựa chọn và automation
Chọn theo risk, impact, kiến trúc, tần suất, automation suitability và chi phí. Không phải dự án nào cũng cần mọi loại test. Ưu tiên nhiều test nhanh, ổn định ở unit/component; integration tập trung contract/boundary; E2E vừa đủ cho luồng critical. Exploratory/usability và đánh giá nghiệp vụ vẫn cần con người.

## Exit criteria
Định nghĩa trước: test bắt buộc, defect threshold, coverage target, CI, environment và approval. Không dùng một ngưỡng coverage chung cho mọi dự án.
