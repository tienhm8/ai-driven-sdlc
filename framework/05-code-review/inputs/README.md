# Inputs – Code Review

`inputs/` là danh mục đầu vào/tham chiếu cho giai đoạn 05. Không mặc định sao chép tài liệu của giai đoạn trước vào đây.

## Nguồn đầu vào
| Nguồn | Nội dung cần có | Mục đích |
|---|---|---|
| 01 Requirement Analysis | User Story, Acceptance Criteria, business rules đã duyệt | Xác định behavior mong đợi |
| 02 System Design | Architecture, API contract, data model, security decisions | Đối chiếu implementation với thiết kế |
| 03 Task Planning | Task, scope, dependency, Definition of Done | Xác định phạm vi và điều kiện hoàn thành |
| 04 Development | PR URL, diff, base/head SHA, test, build/CI evidence | Đối tượng review trực tiếp |
| Repository standards | Coding, testing, security standards | Tiêu chí đánh giá |

## Quy ước
- Ưu tiên liên kết đến tài liệu gốc có version/commit.
- Nếu cần snapshot, lưu metadata nguồn, version, thời điểm lấy và owner.
- Không lưu secret, token, production dump hoặc PII không cần thiết.
- Ghi rõ `Missing` nếu đầu vào bắt buộc chưa có; không tự suy diễn.
- PR diff phải gắn với head SHA cụ thể; review lại khi SHA thay đổi đáng kể.

## Intake record tối thiểu
- Project / repository:
- PR:
- Base SHA / Head SHA:
- Requirement reference:
- Design reference:
- Task reference:
- CI/test evidence:
- Missing inputs:
- Intake owner/date:

## Kiến trúc

```
inputs/
├── README.md        # Quy định nguồn đầu vào, intake record và quy ước
```

## Vai trò từng file

| File | Vai trò |
|---|---|
| `README.md` | Quy định nguồn đầu vào của giai đoạn Code Review, cách liên kết đến tài liệu gốc có version/commit, và mẫu intake record tối thiểu. Là điểm bắt đầu trước khi review PR. |

Thư mục hiện chỉ có `README.md`. Tài liệu từ các giai đoạn 01–04 được tham chiếu qua liên kết, không sao chép vào đây.
