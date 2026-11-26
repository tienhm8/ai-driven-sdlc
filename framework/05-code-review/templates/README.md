# Templates – Code Review

`templates/` chứa biểu mẫu dùng trong giai đoạn Code Review, từ phía developer (PR) đến phía reviewer (báo cáo, checklist, đánh giá bảo mật).

## Kiến trúc
```text
templates/
├── pull-request-template.md      # Developer điền khi mở PR (đầu vào)
├── code-review-checklist.md      # Checklist tổng hợp cho reviewer
├── security-review.md            # Biểu mẫu đánh giá bảo mật
└── review-report.md              # Báo cáo review đầu ra (đầu ra)
```

Luồng sử dụng:
1. Developer điền `pull-request-template.md` → PR được tạo.
2. Reviewer (người hoặc AI) dùng `code-review-checklist.md` và `security-review.md` khi cần.
3. Kết quả ghi vào `review-report.md` và lưu trong `outputs/`.
4. Quyết định G4 được ghi trong mục *Human decision & G4* của báo cáo, theo `human-review.md`.

## Vai trò từng file
| File | Vai trò | Người dùng chính | Đầu ra lưu ở |
|---|---|---|---|
| `pull-request-template.md` | Chuẩn hóa mô tả PR: summary, requirement/task/design, scope, thay đổi, test evidence, rủi ro, reviewer checklist, phần ghi nhận việc AI hỗ trợ | Developer / Author | Mô tả PR trên hệ thống quản lý mã nguồn |
| `code-review-checklist.md` | Checklist theo nhóm: Correctness, Design, Reliability & performance, Testing, Security & data, Compatibility & release | Reviewer | Ghi Pass/Fail/N/A vào `review-report.md` |
| `security-review.md` | Metadata, trust boundary, 13 nhóm kiểm tra bảo mật, bảng finding, xác minh và quyết định (Pass / Changes Required / Blocked) | Security reviewer | Phụ lục của báo cáo hoặc `outputs/` |
| `review-report.md` | Báo cáo chính: metadata, scope, input & evidence, executive summary, findings (CR-0001), checks, quyết định human & G4, sign-off | AI reviewer lập; Human reviewer ký | `outputs/<project>/<PR>/` |

## Quy ước
- Không điền secret, token, PII hay dữ liệu production vào template.
- Mỗi finding dùng một ID riêng theo chuẩn, ví dụ `CR-0001`, và phải có vị trí, bằng chứng, tác động, khuyến nghị.
- Báo cáo mới được tạo khi head SHA thay đổi; không ghi đè báo cáo cũ (tăng *Report version*).
- Các file `outputs/*-example.md` là ví dụ minh họa, không phải kết quả review thực tế.
