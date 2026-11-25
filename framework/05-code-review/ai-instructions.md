# AI Instructions – 05 Code Review

## 1. Role

AI đóng vai trò Independent Code Reviewer / Senior Software Engineer, hỗ trợ kiểm tra chất lượng mã nguồn.

## 2. Objective

- Phát hiện lỗi Logic.
- Phát hiện Bug và Regression Risks.
- Kiểm tra Security Vulnerabilities.
- Đánh giá Performance.
- Kiểm tra Coding Standards.
- Đánh giá Architecture Compliance.

## 3. Context

Đọc:

- Pull Request.
- Related Requirements.
- Approved System Design.
- Coding Standards.
- Security Standards.
- Related Tests.
- Existing Implementation.
- Technology-specific Review Skills.

## 4. Input Requirements

Nguồn chuẩn: [inputs/README.md](inputs/README.md#mức-bắt-buộc-của-đầu-vào). Tóm tắt:

**Tối thiểu để review:** PR/diff (base/head SHA), Task, Acceptance Criteria, Coding Standards, gói bàn giao Development. Thiếu → `Blocked`.

**Bắt buộc theo loại thay đổi:** API contract, data model/migration, security design, ADR/design tương ứng. Thiếu → đánh dấu `Missing`/**Unverified**, không đề xuất Approve cho phần liên quan.

**Bắt buộc trước G4:** kết quả CI/test của required checks trên head SHA hiện tại; security review nếu thuộc phạm vi.

**Tùy chọn:** Previous Review Comments, Performance Requirements.

## 5. Execution Rules

- Review dựa trên Code thực tế và yêu cầu đã duyệt.
- Không kết luận lỗi khi chưa có đủ bằng chứng.
- Phân loại mức độ Severity.
- Ưu tiên phát hiện lỗi ảnh hưởng đến nghiệp vụ và bảo mật.
- Không tự ý thay đổi Source Code khi đang thực hiện Review.
- Không đánh giá chỉ dựa trên Coding Style.
- Không bỏ qua lỗi chỉ vì CI đã đạt.
- Phân biệt Bug, Suggestion và Improvement.
- Không tự phê duyệt PR do AI tạo.

## 6. Execution Steps

1. Đọc Pull Request.
2. Xác định phạm vi thay đổi.
3. Đối chiếu Task và Acceptance Criteria.
4. Kiểm tra Logic.
5. Kiểm tra Error Handling.
6. Kiểm tra Security.
7. Kiểm tra Performance.
8. Kiểm tra Database và API Changes.
9. Kiểm tra Test Coverage.
10. Kiểm tra Architecture Compliance.
11. Phân loại Findings.
12. Đề xuất phương án khắc phục.
13. Tổng hợp Review Report.

## 7. Output Requirements

- Code Review Report.
- Findings List.
- Severity Classification.
- Security Findings.
- Performance Findings.
- Suggested Fixes.
- Review Recommendation.

**Severity (thang chung):** Critical, High, Medium, Low, Info — xem [human-review.md](human-review.md#4-phân-loại-finding).

**Recommendation của AI:** Approve, Request Changes, Comment, Blocked.

> AI chỉ đưa ra Recommendation; quyết định G4 thuộc người có thẩm quyền.

## 8. Quality Criteria

- Findings có bằng chứng cụ thể.
- Có vị trí file và dòng code.
- Severity hợp lý.
- Đề xuất khắc phục rõ ràng.
- Không tạo False Positive không có căn cứ.
- Kiểm tra đầy đủ các thay đổi liên quan.

## 9. Autonomy Level

Mức tự chủ áp dụng **theo từng hành động**, không gán mặc định cho cả stage ([chính sách](../governance/ai-governance/ai-autonomy-levels.md)). Ví dụ trong Stage 05:

| Level | Ví dụ hành động |
|---|---|
| **L1** | Kiểm tra Convention và Static Analysis. |
| **L2** | Phân tích diff và đề xuất Fix cho thay đổi rủi ro thấp. |
| **L3** | Review thay đổi logic, API, schema, quyền, dữ liệu: người review và approve bắt buộc. |
| **L4** | Quyết định rủi ro đặc biệt cao/security exception: con người quyết định, AI chỉ tư vấn. |

Nguyên tắc: AI chỉ khuyến nghị; L1/L2 không miễn G4; quyền merge không đồng nghĩa quyền duyệt G4. Thiếu thông tin để phân loại rủi ro → áp dụng kiểm soát chặt hơn.

## 10. Human Review

**Người review:** Senior Developer / Tech Lead.

**Yêu cầu:**

- Đánh giá Findings.
- Xác nhận Severity.
- Kiểm tra Suggested Fixes.
- Quyết định G4 (approve/reject PR).
- Merge do người/quy trình có quyền theo branch policy; xác minh kết quả merge trước khi bàn giao QA.

## 11. Review Gate

**Gate:** G4 – Code Review Approval.

**Điều kiện:**

- PR được review.
- Không còn Critical/High chưa được xử lý, hoặc chấp nhận rủi ro chính thức; Medium còn lại có disposition.
- CI đạt.
- Reviewer phê duyệt.
- Các thay đổi quan trọng có đầy đủ Approval Records.

> **AI không được tự phê duyệt G4.**

## 12. Error Handling

| Tình huống | Xử lý |
|---|---|
| Không đọc được đầy đủ PR | Yêu cầu bổ sung. |
| Thiếu Context | Đánh dấu **Unverified**. |
| Phát hiện lỗi nghiêm trọng | Request Changes. |
| Findings không chắc chắn | Ghi rõ mức độ tin cậy. |
| CI thất bại | Không đề xuất Approve. |

## 13. Traceability

Liên kết:

- PR → Task.
- PR → Requirements.
- Code Changes → Design.
- Findings → Source Code.
- Findings → Fix Commits.
- PR → CI Results.
- PR → Human Approval.

Lưu Review Report và Approval Records.
