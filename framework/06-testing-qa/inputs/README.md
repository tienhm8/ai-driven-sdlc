# Inputs – Testing & QA

## Mục đích
Danh mục tài liệu/evidence cần tham chiếu khi thực hiện giai đoạn 06. Đây là điểm intake, không phải kho sao chép tài liệu upstream.

## Nguồn đầu vào
| Giai đoạn | Inputs | Mục đích |
|---|---|---|
| 01 Requirement Analysis | Approved User Stories, Acceptance Criteria, business rules, NFR | Expected behavior và acceptance scope |
| 02 System Design | Architecture, API contracts, data model, integration/security design | Integration, data, security và system tests |
| 03 Task Planning | Approved task, scope, dependencies, Definition of Done | Phạm vi thay đổi và completion criteria |
| 04 Development | Build artifact và commit trước merge, unit/component tests, config notes | Tham chiếu kỹ thuật; không thay build đã tích hợp dùng làm bằng chứng G5 |
| 05 Code Review | Review report, quyết định G4, merge commit SHA đã xác minh, link bằng chứng merge, test/CI evidence, findings và rủi ro bàn giao QA | Xác nhận kết quả tích hợp và xác định phạm vi regression |

Có thể cần release target, supported platforms, operational constraints và project policies.

## Intake record
- Project/repository/release:
- Requirement version/reference:
- Design version/reference:
- Task/DoD reference:
- PR/code-review report:
- G4 review/merge reference, repository, verified merge commit SHA và link bằng chứng merge:
- Integrated artifact URI/version và SHA-256 (`artifact_sha256`):
- CI build/run và tham chiếu provenance đã xác minh (`provenance_ref`), liên kết digest với repository và merge commit G4:
- Rủi ro bàn giao từ Code Review:
- Unit/component test evidence:
- Known defects/findings:
- Target environment:
- Missing/conflicting inputs:
- Intake owner/date:

## Quy tắc
Ưu tiên link nguồn chuẩn có version/commit. Nếu snapshot cần thiết, ghi source/version/timestamp/owner. Không tự chọn giữa tài liệu mâu thuẫn; yêu cầu owner xác nhận. Không lưu credential, secret, production dump hoặc PII không cần thiết. Thiếu AC, định danh artifact hoặc provenance đã xác minh thì ghi `Missing`/`Blocked` cho intake và báo owner; link build run không thay thế provenance. Sau intake, dùng [readiness checklist](../checklists/test-readiness-checklist.md) trước execution.

## Kiến trúc
Inputs đi theo chuỗi giai đoạn, mỗi giai đoạn bổ sung một loại đầu vào cho 06:

```text
01 Requirement → 02 Design → 03 Task → 04 Development → 05 Code Review
  (AC, rules)    (API, data)  (DoD)     (test evidence)   (merge SHA, findings)
                                  ↓
                    Intake record (điểm vào của 06)
```

## Vai trò từng file
| File | Vai trò |
|---|---|
| `README.md` (này) | Xác định nguồn đầu vào theo giai đoạn, mẫu intake record và quy tắc tham chiếu |

Thư mục hiện chỉ có một file. Các tài liệu thực tế (AC, design, build…) được tham chiếu bằng link/version trong intake record, không sao chép vào đây.
