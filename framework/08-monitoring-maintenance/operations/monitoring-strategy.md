# Monitoring Strategy

## Mục tiêu
Giám sát trải nghiệm người dùng và sức khỏe dịch vụ để phát hiện suy giảm, hỗ trợ điều tra và cung cấp bằng chứng vận hành.

## Golden signals
- **Latency:** p50/p90/p95/p99, không chỉ average.
- **Traffic:** request rate, throughput, queue ingress/egress.
- **Errors:** tỷ lệ lỗi theo loại, endpoint và dependency.
- **Saturation:** CPU, memory, disk, connection/thread pool, queue depth và quota.

Bổ sung business metrics, dependency health, capacity và security signals theo đặc thù.

## SLI/SLO
Service Owner xác định user journey và SLI. SLO target, measurement window, exclusions và error budget phải được phê duyệt; AI không tự đặt mục tiêu. Phân biệt SLI (đo lường), SLO (mục tiêu nội bộ), SLA (cam kết).

## Telemetry
- Metrics: tên/đơn vị/labels rõ; tránh high-cardinality như user ID/email/raw URL.
- Logs: structured, timestamp có timezone, severity, correlation/trace ID; redact secrets/PII.
- Traces: instrument critical path và dependency; sampling phù hợp.
- Events: deploy, config, scaling, failover và maintenance phải tương quan được.

## Dashboard
Mỗi service nên có overview SLI/traffic/latency/errors/saturation; dependency view; runtime/capacity; business journey; release/change markers. Hiển thị environment, time range, units, owner và runbook link.

## Data governance
Xác định access, retention, redaction, encryption, export và audit. Chỉ thu thập dữ liệu cần thiết.

## Coverage
Đánh giá critical services, user journeys, dependencies và failure modes. Monitoring pipeline lỗi/mất dữ liệu phải có cảnh báo riêng; missing data không đồng nghĩa healthy.
