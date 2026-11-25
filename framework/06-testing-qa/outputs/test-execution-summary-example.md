# Example – Test Execution Summary

> Minh họa, không phải kết quả test thực tế.

- Project: `sample-app`
- Test run: `TESTRUN-0001`
- Artifact: `1.0.0-rc1` / SHA-256: `<digest minh họa>`
- Merge G4 / provenance: `<tham chiếu minh họa>`
- Environment: `QA`
- Test plan: Kế hoạch kiểm thử release `1.0.0-rc1`, v1

| Status | Count |
|---|---:|
| Total | 20 |
| Pass | 16 |
| Fail | 2 |
| Blocked | 1 |
| Not Run | 1 |

Số liệu chỉ minh họa định dạng, không dùng làm bằng chứng release. Ví dụ finding: `BUG-0001` High – cần điều tra authorization; `BUG-0002` Medium – boundary validation. Requirement/risk coverage cần traceability matrix thực tế.

**QA recommendation: No-Go** trong ví dụ do còn High defect và test chưa hoàn tất. Quyết định thật phải dựa trên evidence và policy dự án.
