# Templates - 01 Requirement Analysis

## Giới thiệu

Bộ template được thiết kế để sử dụng xuyên suốt giai đoạn Requirement Analysis, hỗ trợ cả Business Analyst, Product Owner, AI Agent và đội ngũ phát triển.

## Quan hệ giữa 5 template

![Quan hệ giữa 5 template](../../assets/template-relationships.png)

| Template | Vai trò |
|---|---|
| `business-requirement.md` | Mẫu Tài liệu yêu cầu nghiệp vụ (BRD) |
| `user-story.md` | Chuyển yêu cầu thành nhu cầu của người dùng |
| `acceptance-criteria.md` | Điều kiện nghiệm thu |
| `use-case.md` | Luồng tương tác chi tiết |
| `requirement-traceability.md` | Liên kết và truy vết toàn bộ yêu cầu |

## Nguyên tắc

- **BRD** là tài liệu chứa các yêu cầu nghiệp vụ (**BRQ**). Các quy tắc nghiệp vụ (**BR**) được tham chiếu theo yêu cầu mà chúng áp dụng.
- **User Story** mô tả yêu cầu từ góc nhìn người dùng.
- **Acceptance Criteria** xác định điều kiện đạt.
- **Use Case** mô tả tương tác và luồng xử lý.
- **Requirement Traceability** quản lý mối liên kết giữa các tài liệu và các giai đoạn SDLC.

Dùng [Quy ước định danh](../../standards/metadata/id-conventions.md) để liên kết tài liệu và artifact. Ví dụ: `BRD-0001` chứa `BRQ-0001`, và `BR-0001` áp dụng cho `BRQ-0001`.

## Kiến trúc

```
templates/
├── README.md                          # Hướng dẫn sử dụng và quan hệ giữa các template
├── business-requirement.md            # Template Tài liệu yêu cầu nghiệp vụ (BRD)
├── user-story.md                      # Template User Story (US)
├── acceptance-criteria.md             # Template tiêu chí nghiệm thu (AC)
├── use-case.md                        # Template Use Case (UC)
└── requirement-traceability.md        # Template ma trận truy vết (RTM)
```

Template là khuôn mẫu chưa có dữ liệu thật. Khi tạo artifact thực tế, nội dung được điền vào `../outputs/` theo đúng cấu trúc của template tương ứng.

## Vai trò từng file

| File | Vai trò | Được dùng để tạo | Thứ tự phụ thuộc |
|---|---|---|---|
| `README.md` | Mô tả bộ template, quan hệ giữa các template và nguyên tắc ID. | — | Đọc đầu tiên |
| `business-requirement.md` | Khuôn cho BRD: mục tiêu, phạm vi, các BRQ, quy tắc nghiệp vụ (BR), NFR, rủi ro và phê duyệt G1. | `outputs/business-requirements.md` | Gốc, tạo đầu tiên |
| `user-story.md` | Khuôn cho US: phát biểu As a / I want / So that, luồng, DoR và DoD. | `outputs/user-stories.md` | Sau khi xác định BRQ trong BRD |
| `acceptance-criteria.md` | Khuôn cho AC, kịch bản Given / When / Then, kiểm thử âm tính và trạng thái nghiệm thu. | `outputs/acceptance-criteria.md` | Sau US |
| `use-case.md` | Khuôn cho UC: actor, luồng chính, luồng thay thế, ngoại lệ và hậu điều kiện. | `outputs/use-cases.md` | Sau US, song song AC |
| `requirement-traceability.md` | Khuôn cho RTM: liên kết xuyên suốt BRQ → US → AC → UC → thiết kế → test, phân tích khoảng trống và tác động thay đổi. | `outputs/requirement-traceability-matrix.md` | Cuối cùng, tổng hợp các file trên |
