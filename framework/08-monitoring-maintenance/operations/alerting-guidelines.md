# Alerting Guidelines

## Nguyên tắc
Alert phải actionable, có owner, severity, impact và runbook. Ưu tiên symptom ảnh hưởng người dùng/SLO hơn cảnh báo mọi nguyên nhân tiềm năng.

## Metadata mỗi rule
Tên/mô tả; service/environment/owner; severity; condition/window/threshold; SLI liên quan; runbook/dashboard; routing/escalation; maintenance suppression; owner/version/review date.

## Severity tham khảo
- **SEV-1:** gián đoạn nghiêm trọng/phạm vi rộng, nguy cơ dữ liệu hoặc security critical.
- **SEV-2:** suy giảm lớn, nhiều người dùng hoặc chức năng trọng yếu ảnh hưởng.
- **SEV-3:** tác động giới hạn, có workaround hoặc không trọng yếu.
- **SEV-4:** cần theo dõi/tối ưu, chưa cần incident response ngay.

Phải dùng severity matrix được tổ chức/service owner phê duyệt; ví dụ trên không thay thế policy.

## Giảm nhiễu
Dùng rolling window, persistence, hysteresis; threshold dựa baseline, seasonality, capacity và SLO. Group/deduplicate theo service/incident/dependency. Suppress chỉ trong maintenance window được duyệt; không che security/critical alert trái policy.

## Routing
Routing theo ownership và severity; xác định primary/secondary on-call, escalation và backup contact. Không tự giả định response-time nếu chưa có on-call policy.

## Lifecycle
`Proposed → Reviewed → Enabled → Tuned → Deprecated`
Mọi thay đổi rule cần owner, lý do, version/change record và xác minh sau triển khai.

## Quality
Theo dõi actionable rate, false positive, duplicates, missed incident, acknowledge time và volume. AI được đề xuất tuning nhưng không tự disable alert quan trọng hoặc đổi routing/threshold production.
