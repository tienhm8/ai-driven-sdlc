# Framework Governance

## Mục tiêu
`framework/governance/` là lớp quản trị dùng chung cho toàn bộ 8 giai đoạn AI-Driven SDLC. Tài liệu quy định quyền hạn AI, trách nhiệm con người, điểm phê duyệt bắt buộc và yêu cầu truy vết.

## Cấu trúc
- `ai-governance/`: chính sách sử dụng, bảo mật, trách nhiệm và autonomy của AI.
- `autonomy-levels/`: hướng dẫn vận hành chi tiết L1–L4.
- `human-review-gates/`: chính sách chung và tiêu chí G1–G7.
- `audit-policy/`: audit trail, quyền truy cập, retention và disposition.

## Thứ tự ưu tiên
1. Pháp luật và nghĩa vụ hợp đồng áp dụng.
2. Chính sách bảo mật, an toàn thông tin và quản trị rủi ro của tổ chức.
3. Governance cấp framework.
4. Governance/rules riêng của project nếu nghiêm ngặt hơn và không mâu thuẫn cấp trên.
5. Hướng dẫn workflow/agent/skill.

Project không được hạ thấp yêu cầu bắt buộc cấp trên. Ngoại lệ phải do người có thẩm quyền phê duyệt và lưu audit.

## Nguyên tắc
- Human accountability; least privilege; explicit approval.
- Traceability; separation of duties; fail safely.
- Ưu tiên thay đổi có thể rollback; hành động khó đảo ngược cần kiểm soát tăng cường.
- AI có thể kiểm tra điều kiện kỹ thuật nhưng không tự phê duyệt Gate bắt buộc.

## Áp dụng
Mỗi project phải chọn autonomy level theo từng action/rủi ro, chỉ định approver G1–G7, cấu hình audit store/access/retention và bổ sung yêu cầu pháp lý, bảo mật phù hợp.
