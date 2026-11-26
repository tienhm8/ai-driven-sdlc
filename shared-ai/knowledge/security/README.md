# Knowledge: security

Chỉ mục tra cứu theo câu hỏi; không chép lại standards hay checklist.

| Câu hỏi | Đọc chuẩn | Dùng skill |
|---|---|---|
| Yêu cầu bảo mật tối thiểu là gì? | [Security standards](../../../framework/standards/security/security-standards.md) | [owasp](../../skills/security/owasp/SKILL.md) |
| Xác thực và phân quyền thiết kế thế nào? | [Security standards](../../../framework/standards/security/security-standards.md) | [authentication](../../skills/security/authentication/SKILL.md), [authorization](../../skills/security/authorization/SKILL.md) |
| Review code về bảo mật? | [Coding standards](../../../framework/standards/coding/coding-standards.md) | [code-review](../../skills/core/code-review/SKILL.md) |

**Gợi ý:** lập danh mục tài sản và trust boundaries; quyền tối thiểu, kiểm tra quyền theo tài nguyên, lọc dữ liệu nhạy cảm khỏi log; bằng chứng review phải che dữ liệu, ưu tiên giảm thiểu và kiểm thử phòng thủ.

**Ghi kết quả ở đâu:** Ghi quyết định vào [Security Design](../../../framework/02-system-design/templates/security-design.md); ghi phát hiện và bằng chứng đã che dữ liệu trong [hồ sơ review](../../../framework/05-code-review/outputs/README.md).
