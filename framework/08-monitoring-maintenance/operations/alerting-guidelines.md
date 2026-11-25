# Alerting Guidelines

## Nguyên tắc
Alert phải actionable, có owner, mức ưu tiên, tác động dự kiến và runbook. Ưu tiên symptom ảnh hưởng người dùng/SLO hơn cảnh báo mọi nguyên nhân tiềm năng.

## Metadata mỗi rule
Tên/mô tả; service/environment/owner; mức ưu tiên; condition/window/threshold; SLI liên quan; runbook/dashboard; routing/escalation; maintenance suppression; version/review date.

## Mức ưu tiên alert
Dùng policy của dự án để quyết định alert nào cần page ngay, xử lý qua ticket hoặc chỉ theo dõi. Đây là mức khẩn cấp của tín hiệu để định tuyến và phản hồi ban đầu, không phải [incident severity](incident-management.md#incident-severity) đã xác minh trong triage.

## Giảm nhiễu
Dùng rolling window, persistence, hysteresis; threshold dựa baseline, seasonality, capacity và SLO. Group/deduplicate theo service/incident/dependency. Suppress chỉ trong maintenance window được duyệt; không che security/critical alert trái policy.

## Routing
Routing theo ownership và mức ưu tiên alert; xác định primary/secondary on-call, escalation và backup contact. Không tự giả định response-time nếu chưa có on-call policy.

## Lifecycle
`Proposed → Reviewed → Enabled → Tuned → Deprecated`
Mọi thay đổi rule cần owner, lý do, version/change record và xác minh sau triển khai.

## Quality
Theo dõi actionable rate, false positive, duplicates, missed incident, acknowledge time và volume. AI được đề xuất tuning nhưng không tự disable alert quan trọng hoặc đổi routing/threshold production.
