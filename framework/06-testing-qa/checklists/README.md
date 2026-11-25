# Checklists – Testing & QA

## Mục đích
Tập checklist dùng để kiểm tra độ đầy đủ của công việc test ở từng bước: sẵn sàng test, thực thi, retest, regression và sign-off G5. Checklist là công cụ rà soát, không thay thế việc đánh giá của QA Lead.

## Kiến trúc
Các checklist được nhóm theo thời điểm sử dụng trong workflow:

```text
test-readiness-checklist        → trước khi thực thi (entry)
functional / non-functional     → trong quá trình thực thi
defect-verification             → khi retest defect
regression-testing              → trước sign-off, sau fix
qa-signoff-checklist            → trước khi trình và đóng G5
```

## Vai trò từng file
| File | Dùng khi | Người sử dụng chính | Nội dung |
|---|---|---|---|
| `test-readiness-checklist.md` | Trước khi chạy test (entry criteria) | QA Engineer, QA Lead | Requirement/AC, build SHA, environment, test data, logging, reset/cleanup |
| `functional-testing-checklist.md` | Thiết kế và thực thi functional test | QA Engineer | Happy/negative/boundary, business rule, error handling, idempotency, expected result truy về AC |
| `non-functional-testing-checklist.md` | Thực thi performance, security, accessibility, compatibility, reliability | QA Engineer, Security/Performance specialist | Workload, threat profile, authz, sensitive data, resource usage, finding và accepted risk |
| `defect-verification-checklist.md` | Ghi nhận và retest defect | QA Engineer | Bug report đầy đủ, evidence đã redacted, retest scenario gốc, regression liên quan, QA xác nhận closure |
| `regression-testing-checklist.md` | Sau fix và trước sign-off | QA Engineer, QA Lead | Impact analysis, defect cũ, critical workflow, contract/integration, flaky và skipped test |
| `qa-signoff-checklist.md` | Trước khi trình và đóng G5 | QA Lead, Product Owner | Scope, defect policy, coverage, provenance, artifact/gói review SHA-256, hai phê duyệt; AI không tự phê duyệt |

## Quy tắc sử dụng
- Mỗi checklist là danh sách rà soát; mục chưa đạt phải ghi lý do, không tick cho có.
- Không tick mục nếu chưa có evidence tương ứng trong `outputs/`.
- Ngưỡng cụ thể (coverage, defect threshold) lấy từ test plan của dự án, không lấy từ checklist.
