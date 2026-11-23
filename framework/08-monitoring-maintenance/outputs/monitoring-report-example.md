# Example – Monitoring Report

> Số liệu giả lập, không phải số liệu vận hành thực tế.

- Service: `sample-api`
- Environment: `staging`
- Period: `2026-11-01` – `2026-11-07 UTC`
- Status: Degraded (illustrative)
- Caveat: chưa có telemetry production hoặc SLO đã duyệt.

| Signal | Observation | Follow-up |
|---|---|---|
| Latency | p95 850 ms (sample only) | Kiểm tra trace/query latency |
| Availability | 99.9% (sample only) | Xác nhận SLI và target chính thức |
| Errors | Không có dữ liệu xác minh | Bổ sung error dashboard |
| Saturation | Chưa có dữ liệu | Kiểm tra pool/CPU/memory |

Không kết luận hệ thống thực tế đang degraded từ ví dụ này.
