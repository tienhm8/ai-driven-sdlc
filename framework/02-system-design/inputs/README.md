# Inputs — System Design

## Mục đích
Dùng manifest này làm điểm tham chiếu chuẩn cho đầu vào Stage 02. Nguồn yêu cầu chính thức là baseline đã được phê duyệt ở G1. Liên kết đúng phiên bản artifact thay vì sao chép tài liệu hoặc trỏ tới bản mới nhất chưa được duyệt.

## Input baseline
| Input | Nguồn | Bắt buộc | Kiểm tra |
|---|---|---:|---|
| Approved Requirement Baseline | `01-requirement-analysis/outputs/12-requirement-review/G1-approval.md` và các artifact được tham chiếu | Có | G1 Approved, version/hash và approval reference |
| User Stories & Acceptance Criteria | `01-requirement-analysis/outputs/05-user-stories-use-cases/`; `06-acceptance-criteria/` | Có | ID rõ, AC kiểm chứng được |
| Functional Requirements | `01-requirement-analysis/outputs/03-functional-requirements/` | Có | Không mâu thuẫn, có traceability |
| Non-functional Requirements | `01-requirement-analysis/outputs/04-non-functional-requirements/` | Có | Giữ toàn bộ NFR đã duyệt, kể cả hiệu năng và bảo mật; có target/định nghĩa đo được khi phù hợp |
| Requirement Traceability Matrix (RTM) | `01-requirement-analysis/outputs/11-requirement-traceability/requirement-traceability-matrix.md` | Có | Đường dẫn và phiên bản/hash khớp với baseline đã được duyệt ở G1 |
| Business Rules | `01-requirement-analysis/outputs/07-business-rules/` | Khi có | Được business owner xác nhận |
| Scope, assumptions, constraints | `01-requirement-analysis/outputs/02-scope-definition/`; `10-assumptions-constraints-risks/` | Có | Phân biệt fact với assumption |
| Rủi ro, phụ thuộc và câu hỏi mở | Baseline G1 và các register được tham chiếu | Khi có | Nêu tác động đến thiết kế, quyết định hoặc người phụ trách và hạn xử lý |
| Integration requirements | `01-requirement-analysis/outputs/03-functional-requirements/`; `10-assumptions-constraints-risks/` | Khi áp dụng | Hệ thống liên quan và owner rõ |
| Data classification/privacy needs | 01 / security owner | Khi áp dụng | Phân loại và hạn chế dữ liệu |
| Existing architecture | Project docs | Dự án hiện hữu | Có version/tình trạng cập nhật |
| Technology constraints | Project context / standards | Khi áp dụng | Nguồn có thẩm quyền |
| Tài liệu bổ sung về hạ tầng, hiệu năng hoặc bảo mật | Project docs / chuyên gia phụ trách | Tùy bối cảnh | Không thay thế hoặc làm giảm hiệu lực yêu cầu đã duyệt |

Mọi yêu cầu thuộc baseline G1 đều có hiệu lực. Các mục ghi `Khi có`, `Khi áp dụng` hoặc `Tùy bối cảnh` không làm cho yêu cầu đã duyệt trở thành tùy chọn.

## Manifest
| Field | Value |
|---|---|
| Project | `[Project name]` |
| Requirement baseline ID/version | `[REQ-BASELINE-XXX / x.y]` |
| G1 status | `Approved / Not approved` |
| PO / approver | |
| Approval reference | `[Link]` |
| RTM đã duyệt | `[Path / URL tới đúng phiên bản]` |
| Phiên bản/hash RTM | `[Version / hash hoặc commit định danh bản RTM]` |
| Source location | `[Path / URL]` |
| Date | `[YYYY-MM-DD]` |

## Validation
- [ ] Requirement baseline đã qua G1.
- [ ] Có version và approval reference cho baseline; đường dẫn và phiên bản/hash RTM khớp với baseline đó.
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
