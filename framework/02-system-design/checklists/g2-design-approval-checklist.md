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
- [ ] Changes requested (bao gồm điều kiện cần đóng)
- [ ] Rejected
- [ ] Blocked (thiếu đầu vào, bằng chứng hoặc phê duyệt bắt buộc)

**Conditions / outstanding actions:** Ghi điều kiện, việc còn mở và bằng chứng đóng; package index ghi điều kiện đã đóng.

**Risk accepted and by whom:**

| Approver | Role | Decision | Timestamp/timezone | Approved version | Reference |
|---|---|---|---|---|---|
| | Solution Architect | | | | |
| | Security owner (khi thuộc phạm vi bắt buộc) | | | | |
| | Data owner (khi thuộc phạm vi bắt buộc) | | | | |
| | Chuyên môn khác (khi thuộc phạm vi bắt buộc) | | | | |

Với từng vai trò chuyên môn, ghi quyết định thực tế (ví dụ `Approved`, `Changes requested` hoặc `N/A` kèm lý do); chỉ các phê duyệt bắt buộc theo phạm vi mới được tính là điều kiện gate.

**Gate status:** `Pending / In Review / Approved / Rejected / Blocked / Changes Requested`

**Rule:**
- Chỉ G2 `Approved`, sau khi đủ điều kiện gate và phê duyệt chuyên môn bắt buộc, mới cho phép chốt baseline và bàn giao.
- Nếu còn điều kiện cần đóng, ghi `Changes Requested`, không dùng quyết định `Approved with conditions`. Thiếu đầu vào, bằng chứng hoặc phê duyệt bắt buộc thì ghi `Blocked`. Sau khi xử lý, lưu bằng chứng và trình Solution Architect phê duyệt lại phiên bản gói sau khi đóng điều kiện; thay đổi vượt phạm vi điều kiện phải review lại theo G2.
- Khi G2 `Approved`, Solution Architect chốt đúng phiên bản gói đã duyệt làm baseline và ghi quyết định, phiên bản, thời điểm và waiver hợp lệ (nếu có) vào hồ sơ G2 và package index. Bàn giao phiên bản này cùng bằng chứng G2 hợp lệ cho Stage 03 Task Planning; sau planning phải qua G3 trước coding. Baseline không phải trạng thái artifact riêng.
