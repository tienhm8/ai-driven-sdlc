# Inputs — System Design

## Mục đích
Đây là đầu vào của giai đoạn 02. **Đúng, nguồn đầu vào chính là kết quả đã được xác nhận ở 01-Requirement Analysis.** Không nhất thiết copy toàn bộ file sang đây; nên dùng manifest/link cùng version để tránh lệch bản.

## Input baseline
| Input | Nguồn | Bắt buộc | Kiểm tra |
|---|---|---:|---|
| Approved Requirement Baseline | 01 / outputs | Có | G1 Approved, version và approval reference |
| User Stories & Acceptance Criteria | 01 / outputs | Có | ID rõ, AC kiểm chứng được |
| Functional Requirements | 01 / outputs | Có | Không mâu thuẫn, có traceability |
| Non-functional Requirements | 01 / outputs | Có | Có target/định nghĩa đo được khi phù hợp |
| Business Rules | 01 / outputs | Khi có | Được business owner xác nhận |
| Scope, assumptions, constraints | 01 / outputs | Có | Phân biệt fact với assumption |
| Integration requirements | 01 / outputs | Khi áp dụng | Hệ thống liên quan và owner rõ |
| Data classification/privacy needs | 01 / security owner | Khi áp dụng | Phân loại và hạn chế dữ liệu |
| Existing architecture | Project docs | Dự án hiện hữu | Có version/tình trạng cập nhật |
| Technology constraints | Project context / standards | Khi áp dụng | Nguồn có thẩm quyền |

## Manifest
| Field | Value |
|---|---|
| Project | `[Project name]` |
| Requirement baseline ID/version | `[REQ-BASELINE-XXX / x.y]` |
| G1 status | `Approved / Not approved` |
| PO / approver | |
| Approval reference | `[Link]` |
| Source location | `[Path / URL]` |
| Date | `[YYYY-MM-DD]` |

## Validation
- [ ] Requirement baseline đã qua G1.
- [ ] Có version và approval reference.
- [ ] Stories, AC, FR, NFR có ID và truy vết.
- [ ] Open questions ảnh hưởng thiết kế đã có quyết định hoặc owner/hạn xử lý.
- [ ] Scope, constraint, assumption được phân biệt.
- [ ] Không chứa secret, token, password hoặc dữ liệu thật nhạy cảm không cần thiết.

Nếu chưa đạt, ghi nhận gap và yêu cầu BA/PO làm rõ; không tự điền giả định thành yêu cầu nghiệp vụ.

## Kiến trúc

```
inputs/
└── README.md    # Manifest đầu vào, bảng baseline và kiểm tra trước khi thiết kế
```

Thư mục hiện chỉ có một file. Đây là cách ghi nhận đầu vào bằng **manifest và liên kết**, không sao chép tài liệu từ `01-requirement-analysis/`.

## Vai trò từng phần của README

| Phần | Vai trò | Ai kiểm tra |
|---|---|---|
| Input baseline | Liệt kê từng loại đầu vào, nguồn, mức bắt buộc và điều kiện kiểm tra. Là căn cứ để xác định thiếu sót. | AI kiểm tra; Solution Architect xác nhận |
| Manifest | Ghi phiên bản requirement baseline, trạng thái G1, người phê duyệt, đường dẫn và ngày. Đây là điểm neo version cho toàn bộ giai đoạn 02. | Người quản lý baseline |
| Validation | Danh sách kiểm tra đầu vào: baseline đã qua G1, có version, ID truy vết được, open question đã có owner, phân biệt fact với assumption, không chứa secret. | AI đề xuất; BA/PO xác nhận gap |

Nếu một mục chưa đạt, ghi nhận gap và yêu cầu BA/PO làm rõ. Không tự chuyển giả định thành yêu cầu chính thức.
