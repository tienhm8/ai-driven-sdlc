# Knowledge: database

Chỉ mục tra cứu theo câu hỏi; không chép lại standards hay checklist.

| Câu hỏi | Đọc chuẩn | Dùng skill |
|---|---|---|
| Chọn mô hình và thiết kế schema thế nào? | [Database](../../../framework/standards/architecture/database-standards.md) | [database-design](../../skills/database/database-design/SKILL.md), [postgresql](../../skills/database/postgresql/SKILL.md), [mongodb](../../skills/database/mongodb/SKILL.md), [redis](../../skills/database/redis/SKILL.md) |
| Thay đổi schema an toàn thế nào? | [Database](../../../framework/standards/architecture/database-standards.md) | [database-migration](../../skills/database/database-migration/SKILL.md) |

**Gợi ý:** thử backup/restore trên bản dữ liệu không nhạy cảm; ghi RPO, RTO và thời gian phục hồi đo được. Review transaction, khóa, chỉ mục và retention theo truy vấn thực tế.

**Ghi kết quả ở đâu:** Ghi quyết định schema trong [Database Design](../../../framework/02-system-design/templates/database-design.md); ghi kết quả diễn tập vào [hồ sơ vận hành](../../../framework/08-monitoring-maintenance/outputs/README.md) của dự án.
