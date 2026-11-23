# Autonomy Levels – Operating Model

Tài liệu tổng quan chính sách: `../ai-governance/ai-autonomy-levels.md`.

| Level | AI được làm | Human control |
|---|---|---|
| L1 | Tự thực hiện tác vụ rủi ro thấp, đã giới hạn | Policy, log và automated checks |
| L2 | Thực hiện tác vụ giới hạn, đề xuất/sửa trong phạm vi | Checklist, sampling hoặc trigger review |
| L3 | Chuẩn bị/thực hiện trong phạm vi được phép | Review/approval trước khi áp dụng hoặc chuyển bước |
| L4 | Phân tích, tư vấn, mô phỏng | Con người quyết định và kiểm soát hành động |

Level gắn với action, không chỉ agent. Gate G1–G7 vẫn bắt buộc độc lập với level. Không rõ level thì dừng để owner phân loại và áp dụng kiểm soát nghiêm ngặt hơn. Project phải ghi action, level, allowed tools, scope, approver và evidence.

Đánh giá lại khi đổi model/provider, tool, quyền, dữ liệu, workflow, environment hoặc sau sự cố.
