# Hồ sơ review yêu cầu (Requirement Review Record)

## 1. Thông tin review

| Trường | Giá trị |
|---|---|
| Review ID | REV-0001 |
| Dự án | [Tên dự án] |
| Gate | G1 — Requirement Approval |
| Requirement baseline/version | [ID/phiên bản/hash] |
| Review package/version | [Phiên bản hoặc tham chiếu bất biến] |
| Thời gian review | [YYYY-MM-DDThh:mm:ssZ] |
| Điều phối/BA | [Owner] |
| Trạng thái review | [Pending / In Review / Completed] |

## 2. Artifact được review

| Artifact | Version/ID | Tham chiếu bất biến | Tác giả | Reviewer |
|---|---|---|---|---|
| BRD | [Version] | [Path/URL/commit] | [ID] | [ID] |
| Scope Definition | [Version] | [Path/URL/commit] | [ID] | [ID] |
| FR/NFR/US/UC/AC/BR/RTM | [Version] | [Path hoặc danh sách] | [ID] | [ID] |

## 3. Findings

| Finding ID | Severity | Artifact/ID/section | Finding và bằng chứng | Resolution cần thiết | Owner | Due date | Status |
|---|---|---|---|---|---|---|---|
| RF-0001 | [Critical/High/Medium/Low] | [Tham chiếu] | [Mô tả] | [Resolution cần thiết] | [Owner] | [Ngày] | Open |

## 4. Resolution và xác minh

| Finding ID | Resolution/thay đổi | Artifact version sau sửa | Người xác minh | Bằng chứng | Trạng thái |
|---|---|---|---|---|---|
| RF-0001 | [Mô tả] | [Version] | [Reviewer] | [Link] | [Resolved/Accepted/Unresolved] |

## 5. Tổng hợp checklist và ý kiến

- Kết quả checklist liên quan: [Tham chiếu run và kết quả]
- Ý kiến Product Owner: [Ý kiến, hoặc link tới ghi nhận]
- Rủi ro/câu hỏi còn lại và việc chấp nhận: [ID, owner, hạn, lý do]
- Khuyến nghị reviewer: [Ready for G1 / Changes requested / Blocked]

## 6. Lịch sử review

| Thời điểm | Người/role | Hành động/nhận xét | Tham chiếu bằng chứng |
|---|---|---|---|
| [Timestamp] | [Reviewer/role] | [Nội dung] | [Link] |

**Quy tắc:** Hồ sơ này ghi quá trình, findings và resolution; không thay thế quyết định chính thức G1. Không tự ghi finding là resolved nếu chưa có bằng chứng xác minh.
