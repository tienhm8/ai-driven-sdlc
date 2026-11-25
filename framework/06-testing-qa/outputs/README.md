# Outputs – Testing & QA

## Mục đích
Thư mục framework chỉ mô tả hồ sơ và chứa ví dụ. Lưu sản phẩm và evidence thực tế trong `docs/06-testing-qa/outputs/` của dự án, không lưu vào framework.

## Artifacts
- Test strategy áp dụng và risk assessment.
- Test plan và test case suite.
- Test data specification/reference.
- Test execution report và evidence links.
- Defect reports và retest results.
- Requirement/risk traceability matrix và coverage report.
- Residual risks, known issues, test limitations.
- QA sign-off và G5 approval record.

## Tổ chức
Lưu theo `docs/06-testing-qa/outputs/<project>/<release-or-cycle>/` tính từ root dự án. Không ghi đè report cũ; tạo version mới khi build/plan thay đổi và liên kết phiên bản trước.

## Metadata & safety
Ghi project, release, cycle, TESTRUN, requirement version, artifact URI/version/SHA-256, merge G4, provenance, environment, plan/report version, executor/reviewer, timestamp, evidence, defect status và hồ sơ G5 (review ID, tham chiếu và SHA-256 gói review, quyết định và audit). Che secret/token/PII; ưu tiên link hệ thống test/CI có kiểm soát truy cập.

## Kiến trúc
Cấu trúc thư mục đề xuất theo project và cycle; mỗi cycle giữ nguyên các version cũ:

```text
docs/06-testing-qa/outputs/                    ← trong repository dự án
└── <project>/<release-or-cycle>/
    ├── test-plan vN
    ├── test-execution-report vN
    ├── bug reports
    ├── traceability / coverage matrix
    └── qa-signoff vN
```

## Vai trò từng file
| File | Vai trò |
|---|---|
| `README.md` (này) | Quy định loại artifact, cách tổ chức thư mục và metadata bắt buộc |
| `qa-signoff-example.md` | Minh họa cách điền QA sign-off với khuyến nghị No-Go và G5 chưa có quyết định; không phải approval |
| `test-execution-summary-example.md` | Minh họa cách trình bày execution summary và recommendation; số liệu chỉ để tham khảo format |

Hai file example chỉ minh họa; không dùng làm bằng chứng release hay copy số liệu sang báo cáo thật.
