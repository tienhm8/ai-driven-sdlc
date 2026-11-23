# Example – Incident Report

> Tình huống staging giả lập.

- Incident ID: `INC-SAMPLE-001`
- Service: `sample-api`
- Severity: SEV-3 (illustrative only)
- Status: Resolved (example)

## Summary
Một lần deploy giả lập làm tăng lỗi request; rollback về phiên bản trước giúp tín hiệu lỗi trở lại baseline.

## Timeline (UTC)
| Time | Event | Evidence |
|---|---|---|
| 10:00 | Deploy v2 | Change record sample |
| 10:05 | Error alert | Alert sample |
| 10:10 | Incident declared | Incident log sample |
| 10:20 | Rollback | Approval/change record sample |
| 10:30 | Health validation | Dashboard sample |

Impact người dùng thực tế chưa xác minh. Approval/timestamps là placeholder; production cần lưu approver thực tế.
