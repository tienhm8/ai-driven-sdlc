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

## Mức bắt buộc của đầu vào
Đây là nguồn chuẩn; `ai-instructions.md` và `workflow.md` tham chiếu về đây.

| Mức | Đầu vào | Nếu thiếu |
|---|---|---|
| **Tối thiểu để bắt đầu review** | PR/diff gắn base/head SHA; task và Acceptance Criteria; coding standards; [gói bàn giao Development](../../04-development/outputs/development-handover-template.md) | `Blocked` – không review, trả về Development |
| **Bắt buộc theo loại thay đổi** | Thay đổi API → API contract; schema/migration → data model + kế hoạch rollback; bảo mật/quyền/dữ liệu nhạy cảm → security design/decision; thay đổi kiến trúc → ADR/design | Ghi `Missing`, review được phần còn lại nhưng không đề xuất Approve cho phần liên quan |
| **Bắt buộc trước G4** | Kết quả CI/build/test của required checks trên head SHA hiện tại; security review nếu thuộc phạm vi; xử lý xong finding chặn merge | Không trình/duyệt G4. CI chưa đạt không ngăn đọc diff nhưng chặn G4 và merge nếu là check bắt buộc |
| **Tùy chọn** | Previous review comments, performance requirements, tài liệu kiến trúc bổ sung khi thay đổi không chạm kiến trúc | Ghi chú nếu liên quan |

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
- Missing inputs (kèm mức: Blocked / theo loại thay đổi / trước G4):
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
