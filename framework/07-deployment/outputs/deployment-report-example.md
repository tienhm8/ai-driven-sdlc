# Ví dụ – Báo cáo triển khai

> Dữ liệu minh họa; không phải deployment thực tế. Dùng [Deployment Record](../../templates/deployment/deployment-record.md) cho biên bản thật.

## Metadata
- Service: `sample-api`
- Release: `v2.4.0`
- Environment: `staging`
- Commit: `abc1234` (placeholder)
- Artifact digest: placeholder
- Pipeline run: placeholder
- Plan version: `1`

## Summary
- Result: Succeeded (chỉ minh họa)
- Strategy: Rolling (ví dụ)
- G6: Không áp dụng cho ví dụ staging này
- Verification: Thay placeholder bằng evidence thực tế.

## Execution
| Step | Result | Evidence |
|---|---|---|
| Artifact verification | Pass (ví dụ) | Registry/provenance link |
| Deployment | Pass (ví dụ) | Pipeline log |
| Health checks | Pass (ví dụ) | Dashboard/query |
| Smoke tests | Pass (ví dụ) | Test report |

## Issues and deviations
- Không ghi nhận issue trong ví dụ này.

## Handover
- Không chuyển Stage 08: đây chỉ là lần triển khai staging.
- Phiên bản đang chạy: `v2.4.0` tại staging (minh họa)
- Dashboard/runbook:
- On-call owner:
- Known risks:
- Operations acceptance:
- Report owner/date:
