# Test Strategy – Testing & QA

## Mục đích
Định nghĩa cách tiếp cận kiểm thử cho dự án: test level nào, loại test nào, môi trường nào, và coverage được đo và diễn giải ra sao. Đây là đầu vào cho `templates/test-plan.md` của từng release/cycle.

## Kiến trúc
Ba tài liệu, mỗi tài liệu trả lời một câu hỏi:

```text
test-levels.md       → Kiểm thử ở mức nào, loại nào?       (WHAT)
test-environment.md  → Chạy ở đâu, với dữ liệu nào?         (WHERE)
test-coverage.md     → Đã kiểm thử đủ chưa, đo bằng gì?     (HOW MUCH)
```

Luồng sử dụng: `test-levels` và `test-environment` được chốt trước → `test-plan` tham chiếu → `test-coverage` được dùng khi đánh giá và báo cáo.

## Vai trò từng file
| File | Nội dung chính | Dùng để |
|---|---|---|
| `test-levels.md` | Định nghĩa test level (Unit → Acceptance), test type (functional, regression, smoke, performance, security…), tiêu chí chọn và automation | Chọn phạm vi và loại test trong test plan; xác định test nào tự động hóa được |
| `test-environment.md` | Các môi trường tham khảo (Local, Integration, QA/Staging, UAT, isolated Performance/Security), environment manifest, readiness, data safety | Chuẩn bị và kiểm soát môi trường; ghi nhận environment issue để không nhầm với product defect |
| `test-coverage.md` | 8 chiều coverage (requirement, risk, scenario, code, API, data, platform, non-functional), traceability matrix, cách diễn giải số liệu | Lập requirement-to-test matrix; báo cáo coverage gap cho QA Lead và G5 |

## Nguyên tắc chung
- Target coverage và defect threshold do QA Lead/dự án đặt theo risk; không áp ngưỡng chung cho mọi dự án.
- Coverage là chỉ báo, không chứng minh không có lỗi.
- Mọi thay đổi chiến lược có tác động đến acceptance phải được QA Lead review (xem `human-review.md`).
