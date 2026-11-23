# Inputs – Testing & QA

## Mục đích
Danh mục tài liệu/evidence cần tham chiếu khi thực hiện giai đoạn 06. Đây là điểm intake, không phải kho sao chép tài liệu upstream.

## Nguồn đầu vào
| Giai đoạn | Inputs | Mục đích |
|---|---|---|
| 01 Requirement Analysis | Approved User Stories, Acceptance Criteria, business rules, NFR | Expected behavior và acceptance scope |
| 02 System Design | Architecture, API contracts, data model, integration/security design | Integration, data, security và system tests |
| 03 Task Planning | Approved task, scope, dependencies, Definition of Done | Phạm vi thay đổi và completion criteria |
| 04 Development | Build artifact, commit SHA, unit/component tests, config notes | Đối tượng test và evidence kỹ thuật |
| 05 Code Review | Review report, unresolved findings, PR decision, CI results | Risk, regression và điều kiện trước QA |

Có thể cần release target, supported platforms, operational constraints và project policies.

## Intake record
- Project/repository/release:
- Requirement version/reference:
- Design version/reference:
- Task/DoD reference:
- PR/code-review report:
- Build artifact/version and commit SHA:
- Unit/component test evidence:
- CI pipeline/run:
- Known defects/findings:
- Target environment:
- Missing/conflicting inputs:
- Intake owner/date:

## Quy tắc
Ưu tiên link nguồn chuẩn có version/commit. Nếu snapshot cần thiết, ghi source/version/timestamp/owner. Không tự chọn giữa tài liệu mâu thuẫn; yêu cầu owner xác nhận. Không lưu credential, secret, production dump hoặc PII không cần thiết. Thiếu AC hoặc build identity có thể khiến test bị Blocked.

## Kiến trúc
Inputs đi theo chuỗi giai đoạn, mỗi giai đoạn bổ sung một loại đầu vào cho 06:

```text
01 Requirement → 02 Design → 03 Task → 04 Development → 05 Code Review
  (AC, rules)    (API, data)  (DoD)     (build, SHA)      (findings, CI)
                                  ↓
                    Intake record (điểm vào của 06)
```

## Vai trò từng file
| File | Vai trò |
|---|---|
| `README.md` (này) | Xác định nguồn đầu vào theo giai đoạn, mẫu intake record và quy tắc tham chiếu |

Thư mục hiện chỉ có một file. Các tài liệu thực tế (AC, design, build…) được tham chiếu bằng link/version trong intake record, không sao chép vào đây.
