# Hồ sơ phê duyệt G1 (G1 Approval Record)

## Thông tin cổng

| Trường | Giá trị |
|---|---|
| Gate | G1 — Requirement Approval |
| Dự án/workflow | |
| Baseline version/hash | |
| Review package version/hash | |
| Trạng thái | PENDING |
| Ngày gửi duyệt | |

## Deliverables được trình duyệt

| Deliverable | ID/version | Tham chiếu bất biến | Trạng thái |
|---|---|---|---|
| Requirement Analysis Report (bổ sung) | | | |
| BRD | | | |
| Scope Definition | | | |
| FRS | | | |
| NFR | | | |
| User Stories | | | |
| Use Cases | | | |
| Acceptance Criteria | | | |
| Business Rules Catalogue | | | |
| Business Process Model (nếu áp dụng/N/A + lý do) | | | |
| Business Glossary (nếu áp dụng/N/A + lý do) | | | |
| Assumptions/Constraints/Dependencies/Risks | | | |
| Open Questions | | | |
| RTM | | | |
| Requirement Review Record | | | |
| G1 Approval (quyết định ghi bên dưới) | | | |

## Checklist và vấn đề còn mở

| Checklist | Kết quả | Tham chiếu run/bằng chứng |
|---|---|---|
| Input completeness | | |
| Requirement analysis | | |
| Requirement quality | | |
| Ambiguity and conflict | | |
| NFR validation | | |
| G1 readiness | | |

- Câu hỏi còn mở: [OQ IDs, owner, hạn, criticality]
- Yêu cầu nào chưa được phê duyệt hoặc còn provisional: [IDs]

## Điều kiện trình duyệt

- [ ] Deliverables bắt buộc đã hoàn thiện và kiểm tra.
- [ ] Deliverables tùy chọn được tạo khi phù hợp hoặc ghi N/A cùng lý do.
- [ ] Findings trọng yếu đã xử lý; vấn đề còn lại có owner/hạn và được PO chấp nhận rõ ràng.
- [ ] Không còn câu hỏi critical ngăn cản System Design.
- [ ] Scope, yêu cầu, AC, NFR và RTM nhất quán.
- [ ] Baseline và review package đúng phiên bản.

## Quyết định của Product Owner

- Approver:
- Vai trò: Product Owner
- Decision: [APPROVED / REJECTED / BLOCKED / CHANGES_REQUESTED]
- Reason/comment:
- Timestamp:
- Evidence/approval reference:

## Điều kiện hoặc ngoại lệ được chấp nhận

| Nội dung | Rủi ro | Giảm thiểu | Owner | Hạn/expiry | Bằng chứng |
|---|---|---|---|---|---|

## Quy tắc quản trị

- Chỉ Product Owner được ủy quyền mới quyết định G1; AI không được tự phê duyệt hoặc suy diễn im lặng thành approval.
- Quyết định chỉ áp dụng cho đúng artifact và review package đã ghi.
- REJECTED, BLOCKED hoặc CHANGES_REQUESTED chặn chuyển sang System Design cho đến khi có review và quyết định hợp lệ mới.
- Thay đổi trọng yếu sau approval cần đánh giá hiệu lực G1 và trình duyệt lại khi cần.
