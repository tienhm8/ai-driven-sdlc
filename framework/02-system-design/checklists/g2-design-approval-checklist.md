# G2 — System Design Approval Checklist

> G2 là điểm kiểm soát bắt buộc. AI không được tự approve hoặc bỏ qua gate.

## Gate information
| Field | Value |
|---|---|
| Project | |
| Design package version | |
| Requirement baseline version | |
| Gate | `G2 — After System Design` |
| Required approver | `Solution Architect` |
| Review date | |
| Approval reference | |

## Completeness & quality
| # | Gate condition | Result | Evidence / comment |
|---:|---|---|---|
| 1 | Requirement baseline đã qua G1 và tham chiếu đúng version | | |
| 2 | Architecture overview, boundaries và component responsibilities rõ | | |
| 3 | ADR ghi nhận quyết định kỹ thuật trọng yếu | | |
| 4 | API specification đủ cho planning/implementation | | |
| 5 | Database design và data model nhất quán | | |
| 6 | Luồng chính, alternate flow và failure path được mô tả | | |
| 7 | Security/privacy controls được xem xét | | |
| 8 | NFR, observability, resilience và operability được xem xét | | |
| 9 | Checklist chuyên môn đã hoàn thành | | |
| 10 | Critical/High findings đã xử lý hoặc có waiver hợp lệ | | |
| 11 | Traceability và versioning đầy đủ | | |
| 12 | Handoff sang Task Planning có constraints/dependencies rõ | | |

## Decision
- [ ] Approved
- [ ] Approved with conditions — chưa Passed (không áp dụng nếu còn blocker/critical risk chưa xử lý)
- [ ] Changes requested
- [ ] Rejected

**Conditions / outstanding actions:** Ghi điều kiện, việc còn mở và bằng chứng đóng; package index ghi điều kiện đã đóng.

**Risk accepted and by whom:**

| Approver | Role | Decision | Timestamp/timezone | Approved version | Reference |
|---|---|---|---|---|---|
| | Solution Architect | | | | |
| | Security owner (khi thuộc phạm vi bắt buộc) | | | | |
| | Data owner (khi thuộc phạm vi bắt buộc) | | | | |
| | Chuyên môn khác (khi thuộc phạm vi bắt buộc) | | | | |

Với từng vai trò chuyên môn, ghi quyết định thực tế (ví dụ `Approved`, `Changes requested` hoặc `N/A` kèm lý do); chỉ các phê duyệt bắt buộc theo phạm vi mới được tính là điều kiện gate.

**Gate status:** `Passed / Failed / Pending`

**Rule:**
- Chỉ quyết định `Approved` mới cho phép G2 `Passed`, sau khi các điều kiện gate và các phê duyệt chuyên môn bắt buộc theo phạm vi đã đầy đủ.
- Với `Approved with conditions`, giữ gate ở `Pending` và không bàn giao chính thức sang Stage 03. Sau khi đóng điều kiện, lưu bằng chứng và trình Solution Architect xác nhận lại quyết định `Approved`. Quyết định và baseline phải gắn với phiên bản gói sau khi đóng điều kiện. Nếu thay đổi chỉ nhằm đóng điều kiện đã ghi, Solution Architect xác nhận dựa trên bằng chứng; nếu vượt phạm vi điều kiện, phải review lại theo G2.
- Khi G2 `Passed`, Solution Architect chốt đúng phiên bản gói đã duyệt làm baseline và ghi quyết định, phiên bản, thời điểm và waiver hợp lệ (nếu có) vào hồ sơ G2 và package index. Bàn giao phiên bản này cùng bằng chứng G2 hợp lệ cho Stage 03 Task Planning; sau planning phải qua G3 trước coding. Baseline không phải trạng thái artifact riêng.
