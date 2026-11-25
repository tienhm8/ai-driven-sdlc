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

## Kết luận review và bằng chứng

| Phạm vi | Reviewer / vai trò | Kết luận / ngày | Bằng chứng | Phiên bản gói hoặc hash; review ID hoặc ID bối cảnh review bất biến | Phê duyệt chuyên môn bắt buộc (nếu áp dụng) |
|---|---|---|---|---|---|
| Khả năng triển khai | Tech Lead | | | | |
| Security | Security owner | | | | |
| Data | Data owner | | | | |
| Chuyên môn khác | | | | | |

Ghi `N/A` và lý do khi không áp dụng. Reviewer ghi kết luận theo phạm vi, không mặc nhiên là approver G2; phê duyệt chuyên môn bắt buộc theo policy hoặc phạm vi phải có bằng chứng. Liên kết điều kiện cần đóng, action không chặn và waiver hợp lệ tới các mục riêng trong approval record.

**Hồ sơ quyết định G2 chính thức:** `[Approval record ID / link]` — dùng mẫu `framework/templates/review/approval-record.md` và gate policy. Checklist chỉ lưu tiêu chí, kết quả và bằng chứng; không thay thế hồ sơ quyết định.

**Hồ sơ blocker (nếu có):** `[ID / link, phiên bản gói, owner, việc cần xử lý, hạn]` — liên kết cả từ approval record; tách khỏi quyết định của approver.

**Rule:**
- Chỉ G2 `Approved`, sau khi đủ điều kiện gate và phê duyệt chuyên môn bắt buộc, mới cho phép chốt baseline và bàn giao. Mỗi phê duyệt chuyên môn bắt buộc phải gắn với đúng phiên bản/hash của gói và lần review hiện hành (review ID hoặc định danh bất biến của bối cảnh review, chẳng hạn `review_context_sha256`). Nếu thay đổi ảnh hưởng đến phạm vi chuyên môn, yêu cầu phê duyệt lại dù hash của gói không đổi. Khi mở review mới mà phạm vi đó không bị ảnh hưởng, chỉ dùng lại bằng chứng nếu reviewer xác nhận bằng chứng vẫn áp dụng cho lần review mới và ghi tham chiếu tương ứng.
- Nếu còn điều kiện cần đóng, ghi `Changes Requested`, không dùng quyết định `Approved with conditions`. Thiếu đầu vào, bằng chứng hoặc phê duyệt bắt buộc thì ghi `Blocked`. Sau khi xử lý, lưu bằng chứng và trình Solution Architect phê duyệt lại phiên bản gói sau khi đóng điều kiện; thay đổi vượt phạm vi điều kiện phải review lại theo G2.
- Khi G2 `Approved`, Solution Architect được ủy quyền chốt đúng phiên bản gói đã duyệt làm baseline; quyết định, phiên bản, thời điểm và waiver hợp lệ (nếu có) được ghi trong approval record. Package index chỉ tham chiếu hồ sơ đó. Bàn giao phiên bản này cùng bằng chứng G2 hợp lệ cho Stage 03 Task Planning; sau planning phải qua G3 trước coding. Baseline không phải trạng thái artifact riêng.
