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
G4 — Approve Code Review
        ↓
Merge theo branch policy
        ↓
Xác minh kết quả merge (merge commit SHA + bằng chứng)
        ↓
Handoff to QA
```

Stage chỉ hoàn tất sau khi merge đã được xác minh. PR đã G4 Approved nhưng chưa merge thì stage vẫn mở.

## 5.3 Entry Criteria — Điều kiện bắt đầu

- PR đã qua kiểm tra bàn giao Development và ở trạng thái Ready for Review; G4 chưa được duyệt.
- Đủ đầu vào tối thiểu theo [inputs/README.md](inputs/README.md) (gồm gói bàn giao Development: mô tả, task/requirement links, test evidence, risk notes). Thiếu → Blocked.
- Build, lint và automated checks bắt buộc đã chạy; CI chưa đạt không ngăn đọc diff nhưng chặn G4.
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
9. **Phân loại findings:** Critical/High/Medium/Low/Info (thang chung trong `human-review.md`); mô tả evidence, impact và remediation.
10. **Gửi phản hồi:** dùng comment rõ ràng, phân biệt blocker với suggestion; không chỉ yêu cầu sửa theo cảm tính.
11. **Remediation:** author sửa, bổ sung test/evidence và phản hồi từng finding.
12. **Re-review:** reviewer xác nhận sửa đúng, không phát sinh regression hoặc scope ngoài ý muốn.
13. **Phê duyệt:** xác nhận các rule bắt buộc và trình G4 cho người có thẩm quyền duyệt G4.
14. **Merge:** người/quy trình có quyền merge thực hiện theo branch protection sau khi G4 Approved.
15. **Xác minh merge & bàn giao:** ghi `merge commit SHA` và link bằng chứng merge; kiểm tra build/CI sau merge (nếu policy yêu cầu) và bàn giao cho QA.

## 5.5 Input — Đầu vào

- Pull Request, commit diff và branch context.
- Requirement/task, acceptance criteria và design/ADR (mức bắt buộc xem `inputs/README.md`).
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
- Maintainer kiểm soát merge policy và branch protection. Quyền merge không đồng nghĩa quyền duyệt G4.
- Tech Lead phân xử tranh luận kỹ thuật và exception.

## 5.8 Output — Đầu ra

- Review comments/findings có severity và trạng thái.
- Remediation commits và re-review evidence.
- Approved PR / G4 decision hoặc rejection.
- Merge evidence: merge identity, merge commit SHA, link bằng chứng merge.
- Code Review Report và security review record khi cần.
- Updated risk/technical debt register.
- G4 approval record.

## 5.9 Quality Check — Kiểm tra chất lượng

- Review đúng diff cuối cùng, không chỉ phiên bản trước remediation.
- Critical/High findings đã đóng hoặc có risk acceptance hợp lệ.
- Approval đến từ reviewer đủ thẩm quyền.
- CI và required checks xanh theo policy.
- Không có unresolved conversation/blocking comment.
- Test và documentation phản ánh đúng behavior mới.
- Branch protection và merge strategy được tuân thủ.

## 5.10 Human Review Gate — Điểm phê duyệt bắt buộc

**G4 — Code Review Approval**

Nguồn quy định: [G4 — Code Review & Merge Approval](../governance/human-review-gates/G4-code-approval.md). Danh sách thao tác: [Merge Approval Checklist](checklists/merge-approval-checklist.md). Phân vai và xử lý bất đồng: [human-review.md](human-review.md).

Tóm tắt: người duyệt G4 là reviewer/Tech Lead có thẩm quyền (cần reviewer chuyên môn với thay đổi bảo mật/kiến trúc nhạy cảm); không còn Critical/High chưa xử lý (ngoại lệ phải có risk acceptance); required checks đạt; approval đúng head SHA. AI chỉ khuyến nghị, không duyệt G4.

## 5.11 Exit Criteria — Điều kiện hoàn thành

- G4 được Approved cho đúng head SHA.
- PR đã được merge theo branch policy và kết quả merge đã được xác minh (merge commit SHA + link bằng chứng).
- Review findings đã đóng/có quyết định.
- Build đưa vào G5 truy vết được về merge commit này.
- PR approved nhưng chưa merge: stage chưa hoàn tất.

## 5.12 Exception Handling — Xử lý ngoại lệ

- **Reviewer không thống nhất:** chuyển Tech Lead/Architecture Owner; lưu decision.
- **Phát hiện lỗ hổng nghiêm trọng:** block merge, tạo security finding/incident theo policy.
- **CI flaky hoặc unavailable:** xác định test thay thế và người chấp thuận; không tự bỏ required check.
- **PR quá lớn:** yêu cầu tách PR nếu có thể; nếu không, tăng reviewer và review theo vùng rủi ro.
- **Emergency fix:** áp dụng emergency review policy, ghi nhận retrospective và bổ sung kiểm soát sau đó.

## 5.13 Next Stage — Chuyển sang giai đoạn tiếp theo

Bàn giao merge commit SHA và bằng chứng merge, approved PR, review findings, test evidence và known risks (ghi trong review report/outputs) cho **06 — Testing & QA**.

---
