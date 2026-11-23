# L3 – Mandatory Human Approval

AI phân tích, chuẩn bị và có thể thực hiện trong sandbox/phạm vi được cấp, nhưng con người bắt buộc review và approve trước khi áp dụng hoặc chuyển bước có tác động.

**Ví dụ:** logic nghiệp vụ; API contract; database schema; authorization; xử lý dữ liệu; kiến trúc thành phần.

**Điều kiện:** requirement/design đã duyệt; có diff, impact analysis, test và rollback/mitigation khi phù hợp; reviewer đủ chuyên môn/thẩm quyền; approval gắn artifact version/commit.

Không thực hiện hành động tiếp theo khi chưa có approval. Artifact đổi đáng kể sau approval thì review lại. Rủi ro vượt thẩm quyền reviewer hoặc khó đảo ngược thì chuyển L4.
