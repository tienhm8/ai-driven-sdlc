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

## 3. Kết quả kiểm tra (dẫn chiếu)

Kết quả checklist 01–06 được ghi tại các checklist run; hồ sơ này chỉ dẫn chiếu, không ghi lại điều kiện hay kết quả kiểm tra.

| Checklist | Tham chiếu run/bằng chứng |
|---|---|
| 01–05 | [Run/evidence link] |
| 06 G1 readiness | [Run/evidence link] |

**Câu hỏi mở, giả định, ràng buộc thuộc phiên bản được duyệt:**

| Loại | Phiên bản/tham chiếu bất biến | ID liên quan (owner, hạn, criticality nếu là OQ) |
|---|---|---|
| Open Questions | [Path/URL/commit] | [OQ IDs/Không có] |
| Assumptions | [Path/URL/commit] | [IDs/Không có] |
| Constraints | [Path/URL/commit] | [IDs/Không có] |
| Yêu cầu chưa duyệt/provisional | | [IDs/Không có] |

## 4. Quyết định chính thức của Product Owner

Quyết định G1 được ghi trên platform; hồ sơ này chỉ dẫn chiếu, không sao chép nội dung quyết định.

- **Tham chiếu quyết định trên platform:** [Link/ID]
- **Áp dụng cho:** Requirement baseline và Review package ở mục 1.

## 5. Ngoại lệ/điều kiện được chấp nhận

| Nội dung | Rủi ro | Giảm thiểu | Owner | Hạn/expiry | Bằng chứng phê duyệt |
|---|---|---|---|---|---|
| [Không có/Nội dung] | [Rủi ro] | [Biện pháp] | [Owner] | [Ngày] | [Link] |

## 6. Hướng dẫn quản trị

- Chỉ Product Owner được ủy quyền mới quyết định G1; AI không được phê duyệt hoặc diễn giải sự im lặng thành approval.
- Quyết định chỉ áp dụng cho đúng artifact và review package đã ghi ở trên.
- Reject, Blocked hoặc Changes Requested đều chặn chuyển sang System Design cho đến khi có review và quyết định hợp lệ mới.
- Thay đổi trọng yếu sau approval cần đánh giá hiệu lực G1 và trình duyệt lại khi cần.
