# Example – Postmortem

> Ví dụ giả lập, không phải RCA của hệ thống thực tế.

## Incident
`INC-SAMPLE-001` – error spike sau deployment.

## Summary
Thay đổi giả lập làm lỗi tăng sau deploy; rollback khôi phục dịch vụ staging.

## Timeline
| Time UTC | Event |
|---|---|
| 10:00 | Deploy v2 |
| 10:05 | Error alert |
| 10:10 | Incident declared |
| 10:20 | Rollback |
| 10:30 | Health validated |

## Root cause
Giả thuyết minh họa: timeout config không phù hợp với latency dependency. Cần trace và config diff để xác minh; chưa phải kết luận có bằng chứng.

## Contributing factors
- Canary coverage có thể chưa đủ.
- Alert phát hiện sau khi lỗi tăng.
- Dashboard dependency latency chưa rõ.

## Actions
| Action | Type | Priority | Owner | Verification |
|---|---|---|---|---|
| Bổ sung canary cho dependency timeout | Prevent | High | Release team | Canary evidence |
| Dashboard dependency latency | Detect | Medium | SRE | Dashboard review |
| Rà soát timeout policy | Prevent | Medium | Service team | Load test |

RCA cuối cùng phải được nhóm kỹ thuật xác minh bằng evidence.
