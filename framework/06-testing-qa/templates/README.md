# Templates – Testing & QA

## Mục đích
Mẫu chuẩn cho các artifact của giai đoạn 06. AI và QA dùng cùng mẫu để kết quả nhất quán, truy vết được và dễ review. Đây là nguồn chuẩn; mục `templates/testing` dùng chung chỉ ghi đường dẫn tới nguồn chuẩn và bản làm việc trong dự án. Điền mẫu vào `docs/06-testing-qa/outputs/<project>/<release-or-cycle>/` trong repository dự án, không sửa mẫu gốc.

## Kiến trúc
Các template theo thứ tự vòng đời test:

```text
test-plan → test-data → test-case → test-execution-report → bug-report → qa-signoff
(lập kế hoạch)  (chuẩn bị)  (thiết kế)   (thực thi & báo cáo)       (defect)   (G5)
```

## Vai trò từng file
| File | Tạo khi | Người điền/review | Nội dung chính |
|---|---|---|---|
| `test-plan.md` | Bắt đầu cycle/release | QA Lead (review), QA Engineer (soạn) | Scope, test approach, risk, entry/exit criteria, environment & data, lịch và trách nhiệm |
| `test-data.md` | Chuẩn bị data | QA Engineer; security/privacy approver nếu cần | Data design (valid, invalid, boundary, duplicate…), nguồn synthetic/anonymized, setup/cleanup |
| `test-case.md` | Thiết kế test | QA Engineer (soạn), QA review | Metadata, traceability tới AC, preconditions, steps/expected, execution record |
| `test-execution-report.md` | Sau mỗi cycle thực thi | QA Engineer (soạn), QA Lead (review) | Summary Pass/Fail/Blocked/Skipped/Not Run, execution details, defect summary, limitations, recommendation |
| `bug-report.md` | Khi Fail được xác nhận | QA Engineer; Developer cập nhật fix | Classification (severity/priority tách riêng), steps, actual/expected, evidence đã redacted, retest |
| `qa-signoff.md` | Trước G5 | QA Lead, Product Owner | Quality summary, open defect & residual risk, coverage gap, recommendation, approval record |

## Quy tắc sử dụng
- Khi điền kết quả, ghi TESTRUN, artifact SHA-256 và environment để truy vết. Dùng `TC-0001`, `BUG-0001`, `TESTRUN-0001` theo chuẩn ID.
- Không điền secret, token, PII hay production dump vào template; tham chiếu data ID thay thế.
- AI có thể chuẩn bị evidence và đề xuất recommendation; mục G5 approval chỉ ghi quyết định thực tế của con người.
