# Outputs – Testing & QA

## Mục đích
Lưu sản phẩm và evidence tạo ra trong giai đoạn 06. Các file example chỉ minh họa, không phải kết quả thực tế.

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
Gợi ý `outputs/<project>/<release-or-cycle>/`. Không ghi đè report cũ; tạo version mới khi build/plan thay đổi và liên kết phiên bản trước.

## Metadata & safety
Ghi project, release, cycle, requirement version, build SHA, environment, plan/report version, executor/reviewer, timestamp, evidence, defect status và G5 decision. Che secret/token/PII; ưu tiên link hệ thống test/CI có kiểm soát truy cập.

## Kiến trúc
Cấu trúc thư mục đề xuất theo project và cycle; mỗi cycle giữ nguyên các version cũ:

```text
outputs/
├── README.md                              ← (này)
├── qa-signoff-example.md                  ← ví dụ, không phải approval thật
├── test-execution-summary-example.md      ← ví dụ, không phải kết quả thật
└── <project>/<release-or-cycle>/          ← kết quả thật (tạo khi chạy test)
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
| `qa-signoff-example.md` | Minh họa cách điền QA sign-off với trạng thái Not Ready và G5 Pending; không phải approval |
| `test-execution-summary-example.md` | Minh họa cách trình bày execution summary và recommendation; số liệu chỉ để tham khảo format |

Hai file example chỉ minh họa; không dùng làm bằng chứng release hay copy số liệu sang báo cáo thật.
