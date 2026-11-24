# Hồ sơ phê duyệt G1 (G1 Approval Record)

## 1. Thông tin cổng

| Trường | Giá trị |
|---|---|
| Gate | G1 — Requirement Approval |
| Dự án/workflow | [Project ID / execution ID] |
| Requirement baseline version/hash | [Version/hash] |
| Review package version/hash | [Version/hash] |
| Trạng thái | Pending |
| Ngày gửi duyệt | [YYYY-MM-DDThh:mm:ssZ] |

## 2. Bộ tài liệu xin phê duyệt

| Deliverable | ID/version | Tham chiếu bất biến | Trạng thái artifact |
|---|---|---|---|
| BRD | [ID/version] | [Path/URL/commit] | [Draft/In Review] |
| Scope Definition | [ID/version] | [Path/URL/commit] | [Draft/In Review] |
| Functional Requirements | [ID/version] | [Path/URL/commit] | [Draft/In Review] |
| Non-functional Requirements | [ID/version] | [Path/URL/commit] | [Draft/In Review] |
| User Stories | [ID/version] | [Path/URL/commit] | [Draft/In Review] |
| Use Cases | [ID/version] | [Path/URL/commit] | [Draft/In Review] |
| Acceptance Criteria | [ID/version] | [Path/URL/commit] | [Draft/In Review] |
| Business Rules Catalogue | [Version] | [Path/URL/commit] | [Draft/In Review] |
| Business Process Model (nếu áp dụng) | [Version/N/A + lý do] | [Path/N/A] | [Status] |
| Business Glossary (nếu áp dụng) | [Version/N/A + lý do] | [Path/N/A] | [Status] |
| Assumptions, Constraints, Dependencies & Risks | [Version] | [Path/URL/commit] | [Draft/In Review] |
| RTM | [Version] | [Path/URL/commit] | [Draft/In Review] |
| Requirement Review Record | [Review ID/version] | [Path/URL/commit] | [Completed/Findings open] |

## 3. Điều kiện trước khi quyết định

- [ ] Các đầu ra bắt buộc đã được hoàn thiện và review.
- [ ] Các đầu ra tùy chọn được tạo khi phù hợp, hoặc ghi N/A cùng lý do.
- [ ] Findings trọng yếu đã được xử lý; phần còn lại có owner, hạn và được PO chấp nhận rõ ràng.
- [ ] Không còn câu hỏi critical ngăn cản System Design.
- [ ] Phạm vi, yêu cầu, acceptance criteria, NFR và RTM nhất quán.
- [ ] Đúng phiên bản artifact/review package đã được trình duyệt.

## 4. Quyết định của Product Owner

- **Approver:** [Danh tính]
- **Vai trò/thẩm quyền:** Product Owner
- **Decision:** [Approve / Reject / Blocked / Changes Requested]
- **Reason/comment:** [Lý do và điều kiện]
- **Timestamp:** [YYYY-MM-DDThh:mm:ssZ]
- **Evidence/reference:** [Approval event/link]

## 5. Ngoại lệ/điều kiện được chấp nhận

| Nội dung | Rủi ro | Giảm thiểu | Owner | Hạn/expiry | Bằng chứng phê duyệt |
|---|---|---|---|---|---|
| [Không có/Nội dung] | [Rủi ro] | [Biện pháp] | [Owner] | [Ngày] | [Link] |

## 6. Hướng dẫn quản trị

- Chỉ Product Owner được ủy quyền mới quyết định G1; AI không được phê duyệt hoặc diễn giải sự im lặng thành approval.
- Quyết định chỉ áp dụng cho đúng artifact và review package đã ghi ở trên.
- Reject, Blocked hoặc Changes Requested đều chặn chuyển sang System Design cho đến khi có review và quyết định hợp lệ mới.
- Thay đổi trọng yếu sau approval cần đánh giá hiệu lực G1 và trình duyệt lại khi cần.
