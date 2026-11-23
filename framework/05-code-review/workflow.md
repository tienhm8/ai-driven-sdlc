# Workflow — Code Review

> Tài liệu workflow cấp framework cho giai đoạn này. Tuân thủ governance, standards và template dùng chung trong `framework/`; các cấu hình riêng của dự án được kế thừa từ `projects/<Project>/.ai-sdlc/`.

# 5. Giai đoạn 05 — Code Review

## 5.1 Purpose — Mục đích

Đánh giá độc lập thay đổi mã nguồn trước khi tích hợp, nhằm phát hiện defect, rủi ro bảo mật, sai lệch kiến trúc, vấn đề maintainability và thiếu kiểm thử. Xác nhận thay đổi đáp ứng tiêu chuẩn dự án và có thể chuyển sang Testing & QA.

## 5.2 Workflow Overview — Tổng quan luồng xử lý

```text
Ready Pull Request
        ↓
Review Scope & Context
        ↓
Automated Review Checks
        ↓
Human Technical / Security Review
        ↓
Findings & Remediation
        ↓
Re-review
        ↓
G5 — Approve Code Review
        ↓
Merge / Handoff to QA
```

## 5.3 Entry Criteria — Điều kiện bắt đầu

- PR đã qua G4 và ở trạng thái Ready for Review.
- Build, lint và automated checks bắt buộc đã chạy.
- PR có mô tả, task/requirement links, test evidence và risk notes.
- Reviewer không có xung đột lợi ích phù hợp với policy; đủ quyền truy cập context.

## 5.4 Workflow Steps — Các bước thực hiện

1. **Tiếp nhận PR:** xác định scope, mục tiêu, risk level, file/module và loại thay đổi.
2. **Đối chiếu yêu cầu:** kiểm tra PR đáp ứng task, acceptance criteria và design baseline.
3. **Kiểm tra tự động:** xem CI, test, lint, static analysis, dependency/license và security scan.
4. **Review correctness:** đánh giá logic, edge cases, concurrency, transaction, error handling và backward compatibility.
5. **Review architecture:** kiểm tra layering, coupling, cohesion, interface, data ownership và consistency với ADR.
6. **Review security/privacy:** kiểm tra authentication, authorization, input validation, injection, secrets, sensitive data và audit.
7. **Review performance/reliability:** xem query, caching, resource lifecycle, timeout/retry, idempotency và failure handling.
8. **Review test/documentation:** xác nhận test có ý nghĩa, coverage phù hợp, docs/changelog được cập nhật.
9. **Phân loại findings:** Critical/High/Medium/Low hoặc severity scale của dự án; mô tả evidence, impact và remediation.
10. **Gửi phản hồi:** dùng comment rõ ràng, phân biệt blocker với suggestion; không chỉ yêu cầu sửa theo cảm tính.
11. **Remediation:** author sửa, bổ sung test/evidence và phản hồi từng finding.
12. **Re-review:** reviewer xác nhận sửa đúng, không phát sinh regression hoặc scope ngoài ý muốn.
13. **Phê duyệt:** xác nhận các rule bắt buộc và trình G5; merge theo branch protection sau khi đủ approval.

## 5.5 Input — Đầu vào

- Pull Request, commit diff và branch context.
- Requirement/task, acceptance criteria và design/ADR.
- Coding, security, testing và review standards.
- CI results, test reports, static/security scan reports.
- PR risk classification và previous review findings.

## 5.6 AI Activities — Hoạt động AI

- Tóm tắt diff và xác định vùng rủi ro cao.
- Kiểm tra lỗi logic, edge cases, code smell và sai lệch convention.
- Hỗ trợ phân tích security vulnerabilities và dependency risks.
- Đánh giá traceability giữa PR, task, requirement và design.
- Đề xuất test còn thiếu và câu hỏi reviewer cần đặt.
- Phân loại finding sơ bộ, kèm file/line/evidence và remediation suggestion.
- Kiểm tra phản hồi remediation và phát hiện vấn đề mới trong diff.
- AI review chỉ là lớp hỗ trợ; không thay thế approval của reviewer có thẩm quyền.

## 5.7 Human Activities — Hoạt động con người

- Reviewer chịu trách nhiệm đánh giá độc lập và quyết định approve/request changes.
- Security reviewer tham gia với thay đổi nhạy cảm hoặc risk cao.
- Author giải trình, sửa lỗi và xác nhận tác động của remediation.
- Maintainer kiểm soát merge policy và branch protection.
- Tech Lead phân xử tranh luận kỹ thuật và exception.

## 5.8 Output — Đầu ra

- Review comments/findings có severity và trạng thái.
- Remediation commits và re-review evidence.
- Approved PR / merge approval hoặc rejection.
- Code Review Report và security review record khi cần.
- Updated risk/technical debt register.
- G5 approval record.

## 5.9 Quality Check — Kiểm tra chất lượng

- Review đúng diff cuối cùng, không chỉ phiên bản trước remediation.
- Critical/High findings đã đóng hoặc có risk acceptance hợp lệ.
- Approval đến từ reviewer đủ thẩm quyền.
- CI và required checks xanh theo policy.
- Không có unresolved conversation/blocking comment.
- Test và documentation phản ánh đúng behavior mới.
- Branch protection và merge strategy được tuân thủ.

## 5.10 Human Review Gate — Điểm phê duyệt bắt buộc

**G5 — Code Review Approval**

Người phê duyệt: reviewer/maintainer được chỉ định; thay đổi bảo mật hoặc kiến trúc nhạy cảm cần reviewer chuyên môn.

Điều kiện:
- Reviewer đã xem xét đầy đủ diff và context.
- Không còn finding blocker; ngoại lệ có risk acceptance được ghi nhận.
- Required checks đạt.
- PR được approve theo số lượng/quy tắc reviewer của dự án.

## 5.11 Exit Criteria — Điều kiện hoàn thành

- G5 được Approved.
- PR được merge hoặc được phép chuyển sang bước tích hợp theo branch policy.
- Review findings đã đóng/có quyết định.
- Commit/merge reference được lưu để truy vết.

## 5.12 Exception Handling — Xử lý ngoại lệ

- **Reviewer không thống nhất:** chuyển Tech Lead/Architecture Owner; lưu decision.
- **Phát hiện lỗ hổng nghiêm trọng:** block merge, tạo security finding/incident theo policy.
- **CI flaky hoặc unavailable:** xác định test thay thế và người chấp thuận; không tự bỏ required check.
- **PR quá lớn:** yêu cầu tách PR nếu có thể; nếu không, tăng reviewer và review theo vùng rủi ro.
- **Emergency fix:** áp dụng emergency review policy, ghi nhận retrospective và bổ sung kiểm soát sau đó.

## 5.13 Next Stage — Chuyển sang giai đoạn tiếp theo

Bàn giao merge reference, approved PR, review findings, test evidence và known risks cho **06 — Testing & QA**.

---
