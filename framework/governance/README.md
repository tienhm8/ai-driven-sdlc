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
Project owner ghi các quyết định dưới đây trong hồ sơ governance của project (ví dụ `docs/governance.md`) và dẫn tới cấu hình, policy và nơi lưu bằng chứng tương ứng. Cập nhật hồ sơ khi phạm vi, quyền, công cụ, dữ liệu hoặc môi trường thay đổi.

- [ ] Chỉ định người phân loại từng hành động theo [chính sách mức tự chủ](ai-governance/ai-autonomy-levels.md). Ghi mức áp dụng, phạm vi, dữ liệu, môi trường, công cụ và quyền được cấp. Khi chưa rõ mức rủi ro, dừng để owner phân loại; nâng mức kiểm soát khi tăng tác động, độ nhạy, quyền hoặc độ khó đảo ngược.
- [ ] Chỉ định approver chính và người thay thế đủ thẩm quyền cho từng gate áp dụng. Ghi phạm vi thẩm quyền, kiểm tra xung đột vai trò và giữ nguyên yêu cầu nhiều người duyệt nếu gate yêu cầu. Nếu dùng platform, xem [cách cấu hình vai trò và kiểm tra thẩm quyền](../../platform/approval-engine/README.md). Không có người đủ thẩm quyền thì chặn, không tự chuyển bước.
- [ ] Ghi ngoại lệ nào được phép, ai có quyền chấp nhận, và cách lưu phạm vi, lý do, rủi ro, giảm thiểu, owner và thời hạn theo [gate policy](human-review-gates/gate-policy.md#ngoại-lệ). Không hạ yêu cầu bắt buộc của framework hoặc của tổ chức; bổ sung yêu cầu pháp lý, hợp đồng và bảo mật áp dụng.
- [ ] Chỉ định nơi lưu audit và bằng chứng, owner vận hành, quyền truy cập, thời hạn lưu và cách truy lại một lần review hoặc thực thi theo [chuẩn audit](audit-policy/audit-trail-standard.md) và [quy định lưu giữ](audit-policy/retention-and-access.md).

`autonomy.default_level` và `autonomy.stages` trong `.ai-sdlc/project.yaml` chỉ là mặc định tham khảo để phân loại. Các giá trị này không cấp quyền thực thi, không miễn gate và không thay thế phê duyệt cho hành động cụ thể.
