# Example – Test Execution Summary

> Minh họa, không phải kết quả test thực tế.

- Project: `sample-app`
- Test cycle: `TCYCLE-001`
- Build: `1.0.0-rc1` / SHA `example-sha`
- Environment: `QA`
- Test plan: `TP-001 v1`

| Status | Count |
|---|---:|
| Total | 20 |
| Pass | 16 |
| Fail | 2 |
| Blocked | 1 |
| Not Run | 1 |

Số liệu chỉ minh họa định dạng, không dùng làm bằng chứng release. Ví dụ finding: `BUG-001` High – cần điều tra authorization; `BUG-002` Medium – boundary validation. Requirement/risk coverage cần traceability matrix thực tế.

**Recommendation: Not Ready** trong ví dụ do còn High defect và test chưa hoàn tất. Quyết định thật phải dựa trên evidence và policy dự án.
