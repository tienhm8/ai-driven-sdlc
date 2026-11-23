# Workflow — Development

> Tài liệu workflow cấp framework cho giai đoạn này. Tuân thủ governance, standards và template dùng chung trong `framework/`; các cấu hình riêng của dự án được kế thừa từ `projects/<Project>/.ai-sdlc/`.

# 4. Giai đoạn 04 — Development

## 4.1 Purpose — Mục đích

Triển khai phần mềm theo design và task baseline đã duyệt, tuân thủ coding/security standards, tạo code có thể kiểm thử, review, build và vận hành. Đảm bảo thay đổi có traceability, kiểm soát phiên bản và bằng chứng thực thi.

## 4.2 Workflow Overview — Tổng quan luồng xử lý

```text
Ready Task + Approved Design
        ↓
Developer / AI Coding Preparation
        ↓
Implement in Small Changes
        ↓
Local Validation & Automated Tests
        ↓
Documentation + Evidence
        ↓
G4 — Development Completion Check
        ↓
Create Pull Request
        ↓
Handoff to Code Review
```

## 4.3 Entry Criteria — Điều kiện bắt đầu

- G3 đã được phê duyệt; task đạt DoR.
- Có design/API/data contract và coding guidelines.
- Repository, branch strategy, CI checks và môi trường phát triển sẵn sàng.
- Developer/AI agent được cấp quyền tối thiểu cần thiết.
- Task có acceptance criteria, owner và liên kết requirement.

## 4.4 Workflow Steps — Các bước thực hiện

1. **Nhận task:** xác nhận mục tiêu, scope, acceptance criteria, dependency và DoD.
2. **Đọc chuẩn liên quan:** kiểm tra architecture, coding, security, API, database và testing standards.
3. **Lập implementation approach:** xác định file/module dự kiến thay đổi, migration, interface và test strategy; trao đổi nếu lệch design.
4. **Tạo branch/workspace:** tuân thủ branch naming, commit convention và quy tắc bảo vệ secret.
5. **Triển khai theo lát cắt nhỏ:** code theo module/component; ưu tiên thay đổi nhỏ, dễ review và rollback.
6. **Sử dụng AI coding có kiểm soát:** cung cấp context tối thiểu cần thiết; yêu cầu AI giải thích thay đổi, giả định và file bị ảnh hưởng.
7. **Thực hiện self-review:** kiểm tra logic, error handling, validation, authorization, logging, performance và edge cases.
8. **Viết automated tests:** unit/component/integration tests phù hợp; không chỉ tạo test để hợp thức hóa implementation.
9. **Chạy validation:** formatter, linter, static analysis, type check, build, unit tests và security checks theo pipeline.
10. **Cập nhật database/API/docs:** tạo migration an toàn, cập nhật contract, changelog và tài liệu kỹ thuật.
11. **Kiểm tra diff:** xác nhận không có secret, debug code, file ngoài scope, dependency không cần thiết hoặc thay đổi ngoài ý muốn.
12. **Commit và tạo PR:** commit có ý nghĩa; PR nêu mục tiêu, giải pháp, test evidence, risk và liên kết task/requirement.
13. **Xác nhận hoàn thành:** cập nhật task, đính kèm kết quả kiểm tra và trình G4.

## 4.5 Input — Đầu vào

- Approved task/backlog và acceptance criteria.
- Design baseline, ADR, API/data contract.
- Coding guidelines, security standards và testing standards.
- Repository, branch policy, CI configuration và development environment.
- Shared skills/agent instructions được dự án cho phép.
- Test data an toàn và các dependency cần thiết.

## 4.6 AI Activities — Hoạt động AI

- Phân tích task và codebase trong phạm vi được cấp quyền.
- Đề xuất implementation plan, code changes và test cases.
- Sinh code, migration, API/client, unit tests và tài liệu theo standards.
- Giải thích diff, dependency và các quyết định triển khai.
- Chạy/diễn giải linter, tests, static analysis và hỗ trợ debug.
- Phát hiện lỗi tiềm ẩn, security smell, performance issue và thiếu test.
- Tự kiểm tra giới hạn thay đổi so với task.
- Không tự mở rộng scope, truy cập secret, merge hoặc deploy nếu chưa được cấp quyền và phê duyệt rõ ràng.

## 4.7 Human Activities — Hoạt động con người

- Developer chịu trách nhiệm tính đúng đắn của code và nội dung PR.
- Tech Lead giải quyết sai lệch thiết kế và quyết định kỹ thuật.
- Developer xác nhận mọi thay đổi do AI đề xuất trước khi commit.
- QA phối hợp làm rõ testability và test data.
- Maintainer quản lý branch, dependency và quyền truy cập.

## 4.8 Output — Đầu ra

- Source code và configuration changes.
- Database migration/schema changes khi có.
- Automated tests và test data phù hợp.
- API/client/interface updates.
- Technical documentation/changelog.
- Commit history, PR description và CI/local validation evidence.
- Updated task status và development completion record.

## 4.9 Quality Check — Kiểm tra chất lượng

- Code tuân thủ coding conventions và architecture boundaries.
- Build, lint, type check và các test bắt buộc đạt.
- Có test cho logic mới, lỗi và edge cases phù hợp.
- Không lộ secret, PII hoặc dữ liệu production trong code/log/test fixture.
- Error handling, validation, authorization và audit phù hợp.
- Migration có phương án an toàn, backward compatibility và rollback khi cần.
- Diff nằm trong scope; dependency/license được kiểm tra.
- PR có mô tả, liên kết task và evidence đầy đủ.

## 4.10 Human Review Gate — Điểm phê duyệt bắt buộc

**G4 — Development Completion / PR Readiness Check**

Người xác nhận: Developer owner và Tech Lead/maintainer theo policy dự án. Đây là xác nhận sẵn sàng đưa vào Code Review, không thay thế G5.

Điều kiện:
- Task implementation hoàn tất theo scope.
- Self-review và automated checks bắt buộc đã chạy.
- PR và evidence đầy đủ.
- Known limitations và rủi ro được công khai.

## 4.11 Exit Criteria — Điều kiện hoàn thành

- G4 được xác nhận.
- PR ở trạng thái Ready for Review.
- Task, commit, PR và requirement có traceability.
- Không còn lỗi build/test bắt buộc chưa giải thích.

## 4.12 Exception Handling — Xử lý ngoại lệ

- **Design không khả thi:** dừng phần thay đổi liên quan, tạo design question/ADR change và xin SA quyết định.
- **Test thất bại:** phân loại defect/environment/flaky test; không bỏ qua gate để hợp thức hóa.
- **Scope creep:** tách task hoặc tạo change request.
- **Phát hiện secret/PII:** dừng chia sẻ, xử lý theo security incident policy và rotate/revoke credential khi cần.
- **AI tạo code không hiểu được:** không merge; yêu cầu giải thích, viết lại hoặc loại bỏ.
- **Migration rủi ro:** yêu cầu review chuyên môn và rehearsal trước khi áp dụng môi trường quan trọng.

## 4.13 Next Stage — Chuyển sang giai đoạn tiếp theo

Bàn giao PR, diff, test evidence, task/requirement links và known issues cho **05 — Code Review**.

---
