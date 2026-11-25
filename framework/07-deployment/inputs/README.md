# Inputs – Deployment

## Kiến trúc
Thư mục không chứa file tiêu chuẩn, mà là **điểm tiếp nhận dữ liệu bàn giao** cho giai đoạn Deployment. Dữ liệu đến từ các giai đoạn trước và CI/CD platform; thư mục chỉ tham chiếu (link, version, commit, digest), không sao chép toàn bộ repository.

```
Giai đoạn 01–06 + CI/CD platform + Operations
                  │
                  ▼
        inputs/README.md  (nguồn + intake checklist + quy tắc)
                  │
                  ▼
   templates/  →  ci-cd/  →  checklists/  →  outputs/
```

## Vai trò từng file
| File | Vai trò |
|---|---|
| `README.md` | Định nghĩa nguồn đầu vào theo từng giai đoạn (01–06, CI/CD, Operations) và mục đích sử dụng; cung cấp intake checklist để xác nhận đủ dữ liệu trước khi lập plan; nêu quy tắc về tham chiếu, secret và xử lý dữ liệu thiếu (`Missing`/`Not Approved`). |

## Mục đích
Tập hợp hoặc tham chiếu tài liệu và evidence cần thiết để lập kế hoạch, phê duyệt và triển khai release. Đây là dữ liệu bàn giao từ các giai đoạn trước và CI/CD platform; không phải nơi sao chép toàn bộ repository.

## Nguồn đầu vào
| Nguồn | Dữ liệu | Mục đích |
|---|---|---|
| 01 – Requirement Analysis | Business scope, acceptance criteria, release constraints | Xác định thay đổi và tác động |
| 02 – System Design | Architecture, topology, API/DB design, NFR | Xác định target và phụ thuộc |
| 03 – Task Planning | Release scope, dependencies, schedule, owners | Lập thứ tự triển khai |
| 04 – Development | Commit, build config, Dockerfile, IaC, app config | Xác định source và packaging |
| 05 – Code Review | PR approval, review findings, security review | Xác nhận thay đổi đã review |
| 06 – Testing & QA | Artifact URI/version/SHA-256 đã duyệt, provenance và merge G4, hồ sơ G5 (gói review/hash, hai phê duyệt), test report, coverage, defect status, known issues/residual risks và tiêu chí smoke | Xác nhận readiness và dùng đúng artifact; lập release notes và chuẩn bị smoke test |
| CI/CD platform | Pipeline run, artifact URI/digest, provenance, scan | Xác minh artifact/automation |
| Operations | Environment inventory, monitoring, backup/restore, runbooks | Xác nhận vận hành/recovery |

## Intake checklist
- [ ] Release ID, service, repository và owner.
- [ ] Release scope và requirement/task links.
- [ ] Commit SHA và artifact version/digest.
- [ ] Merge G4, provenance đã xác minh và hồ sơ G5 trên đúng artifact SHA-256.
- [ ] CI/build/test/security scan evidence, defect status, known issues/residual risks và tiêu chí smoke đã thống nhất.
- [ ] Environment/configuration references; nếu QA giới hạn scope bằng feature flag, đối chiếu cấu hình đích với hồ sơ G5 trước rollout.
- [ ] Dependencies và infrastructure changes.
- [ ] Migration/backup/restore impact.
- [ ] Deployment strategy và rollback constraints.
- [ ] Maintenance window, communication và on-call.

## Quy tắc
- Tham chiếu tài liệu gốc bằng link/version/commit; snapshot phải có source và timestamp.
- Không lưu plaintext secret, private key, token, production dump hoặc PII không cần thiết.
- Secret chỉ tham chiếu qua secret manager/path/identifier được phép.
- Thiếu hoặc chưa duyệt thì đánh dấu `Missing`/`Not Approved`; không suy diễn.
- Nếu artifact SHA-256 đổi, quay lại QA, kiểm thử trên artifact mới và lấy G5 mới trước G6. Nếu source đổi, quay lại 04 và G4 trước khi đưa build mới vào QA. Nếu cấu hình thay đổi làm mở rộng scope đã duyệt, quay lại QA và lấy G5 mới trước G6, kể cả khi digest không đổi.
