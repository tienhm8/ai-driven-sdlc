# Project Management

Quản lý hồ sơ điều hành xuyên suốt AI-Driven SDLC: khởi tạo, baseline, theo dõi, thay đổi, rủi ro, issue, quyết định, phê duyệt và đóng dự án.

## Cấu trúc
```
project-management/
├── README.md
├── structure.yml
├── project-charter.md
├── project-status.md
├── workflow.md
├── change-log.md
├── risk-register.md
├── issue-log.md
├── decision-log.md
├── approval-register.md
├── meeting-notes.md
├── project-closeout.md
│
└── templates/
    ├── README.md
    ├── project-charter-template.md
    ├── status-report-template.md
    ├── change-request-template.md
    ├── risk-register-template.md
    ├── issue-log-template.md
    ├── decision-record-template.md
    ├── approval-record-template.md
    ├── meeting-notes-template.md
    └── closeout-report-template.md
```

## Nội dung đã thiết kế

| Thành phần | Chức năng |
|---|---|
| Project Charter | Khởi tạo và phê duyệt dự án |
| Structure YAML | Metadata và cấu hình dự án |
| Project Status | Theo dõi tiến độ, ngân sách, chất lượng |
| Change Log | Quản lý thay đổi |
| Risk Register | Quản lý rủi ro |
| Issue Log | Theo dõi vấn đề |
| Decision Log | Lưu quyết định |
| Approval Register | Truy vết phê duyệt G1–G7 |
| Meeting Notes | Biên bản và action items |
| Project Closeout | Nghiệm thu và đóng dự án |
| Workflow | Quy trình quản lý xuyên suốt |

Đặc biệt, đã phân biệt rõ:
- Risk: sự kiện chưa xảy ra nhưng có khả năng xảy ra.
- Issue: vấn đề đã thực sự xảy ra.
- Change: yêu cầu thay đổi baseline.
- Decision: quyết định được đưa ra.
- Approval: xác nhận chính thức của người có thẩm quyền.

## Vai trò
Sponsor bảo trợ và quyết định cấp cao; PO chịu trách nhiệm nghiệp vụ; PM điều phối; Tech Lead/Architect quản trị kỹ thuật; QA Lead xác nhận chất lượng; Release Manager phê duyệt sẵn sàng phát hành. AI hỗ trợ soạn thảo/phân tích, không tự phê duyệt Human Review Gate.

## Quy tắc
- Mỗi project có bộ hồ sơ riêng.
- ID ổn định: `CHG-###`, `RSK-###`, `ISS-###`, `DEC-###`, `APR-###`, `MTG-YYYYMMDD-##`.
- Ghi owner, trạng thái, ngày cập nhật, phiên bản và bằng chứng.
- Không xóa lịch sử đã duyệt; tạo bản ghi mới để thể hiện thay đổi.
- Dùng ISO 8601; ưu tiên timestamp UTC và ghi rõ timezone.
- Dùng link tới tài liệu gốc/version thay vì sao chép tùy tiện.
- Nội dung AI tạo là draft đến khi người có thẩm quyền xác nhận.

## Liên kết 8 giai đoạn
G1 PO – yêu cầu; G2 Solution Architect – thiết kế; G3 Tech Lead – sẵn sàng coding; G4 Reviewer/Tech Lead – trước merge; G5 QA Lead/PO – nghiệm thu; G6 Release Manager – production; G7 Incident Commander – sự cố nghiêm trọng. Gate policy chính thức nằm trong `framework/governance/human-review-gates/`.

## Khởi tạo
Điền charter, cấu hình `structure.yml`, thiết lập baseline/milestone, tạo register ban đầu và thực hiện `workflow.md`. Register chưa có mục phải ghi `No entries`, không để trạng thái mơ hồ.
