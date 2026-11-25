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
| 1 | [Input manifest](../inputs/README.md) tham chiếu đúng phiên bản requirement baseline và RTM đã duyệt ở G1 | | |
| 2 | Architecture overview, boundaries và component responsibilities rõ | | |
| 3 | ADR ghi nhận quyết định kỹ thuật trọng yếu | | |
| 4 | API specification đủ cho planning/implementation | | |
| 5 | Database design và data model nhất quán | | |
| 6 | Luồng chính, alternate flow và failure path được mô tả | | |
| 7 | Security/privacy controls được xem xét | | |
| 8 | NFR, observability, resilience và operability được xem xét | | |
| 9 | Checklist chuyên môn đã hoàn thành | | |
| 10 | Critical/High findings đã xử lý hoặc có waiver hợp lệ | | |
| 11 | [Bảng truy vết thiết kế](../outputs/design-package-index.md#4-truy-vết-yêu-cầu) đã được đối chiếu: FR/NFR trong phạm vi và AC khi áp dụng liên kết tới mục thiết kế có phiên bản và cách kiểm chứng dự kiến; gap được ghi nhận | | |
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
- Xem [quy tắc quyết định G2 và chốt baseline](../human-review.md#6-điều-kiện-quyết-định-g2). Mỗi phê duyệt chuyên môn bắt buộc phải gắn với đúng phiên bản/hash của gói và lần review hiện hành (review ID hoặc định danh bất biến của bối cảnh review, chẳng hạn `review_context_sha256`). Nếu thay đổi ảnh hưởng đến phạm vi chuyên môn, yêu cầu phê duyệt lại dù hash của gói không đổi. Khi mở review mới mà phạm vi đó không bị ảnh hưởng, chỉ dùng lại bằng chứng nếu reviewer xác nhận bằng chứng vẫn áp dụng cho lần review mới và ghi tham chiếu tương ứng.
- Sau khi đóng điều kiện bắt buộc, lưu bằng chứng cho đúng phiên bản gói trình lại; thay đổi vượt phạm vi điều kiện phải review lại theo G2.
- Đối chiếu điều kiện hoàn thành tại [workflow](../workflow.md#211-exit-criteria--điều-kiện-hoàn-thành) trước khi bàn giao.
