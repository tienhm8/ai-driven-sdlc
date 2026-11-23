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
- [ ] Approved with conditions (không áp dụng nếu còn blocker/critical risk chưa xử lý)
- [ ] Changes requested
- [ ] Rejected

**Conditions / outstanding actions:**  
**Risk accepted and by whom:**

| Approver | Role | Decision | Timestamp/timezone | Approved version | Reference |
|---|---|---|---|---|---|
| | Solution Architect | | | | |

**Gate status:** `Passed / Failed / Pending`  
**Rule:** Chỉ khi Passed mới chuyển design package thành baseline chính thức và cho phép G3.
