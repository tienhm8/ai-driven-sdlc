# Development Inputs

Thư mục này mô tả/tập hợp đầu vào được Development tiêu thụ từ 01–03. Ưu tiên tham chiếu nguồn chuẩn bằng ID, version, URL/path; chỉ snapshot khi cần reproducibility hoặc policy yêu cầu.

## Kiến trúc

```text
inputs/
├── README.md                    # Quy định về đầu vào và điều kiện sử dụng
└── input-manifest-template.md   # Mẫu manifest, lập cho từng task
```

Luồng sử dụng: trước khi code, Developer lập một `input-manifest-template.md` cho task, ghi ID/phiên bản baseline được bàn giao và bằng chứng G1/G2/G3 tương ứng. Manifest này là căn cứ để kiểm tra `checklists/development-readiness.md`.

## Vai trò từng file

| File | Vai trò | Ai dùng |
|---|---|---|
| `README.md` | Quy định đầu vào tối thiểu từ 01, 02, 03 và điều kiện G1/G2/G3 phải đạt. Quy định cách tham chiếu (ID/version/commit), xử lý mâu thuẫn và loại dữ liệu không được lưu. | Developer, AI, Tech Lead |
| `input-manifest-template.md` | Ghi lại đầu vào thực tế của từng task: artifact đã duyệt, version, approval, bối cảnh kỹ thuật và tham chiếu kết quả readiness. | Developer lập; Tech Lead xác nhận |

## Quy tắc sử dụng

- Đối chiếu đúng phiên bản baseline và bằng chứng phê duyệt cho phiên bản đó. Không dùng bản nháp thay thế; ghi tham chiếu waiver hợp lệ (nếu có) và xử lý theo [development readiness checklist](../checklists/development-readiness.md).
- Nếu các nguồn mâu thuẫn, kết quả là Blocked và owner phải giải quyết trước khi tiếp tục.
- Không lưu secret hoặc dữ liệu production nhạy cảm trong manifest.

## Đầu vào theo giai đoạn

| Nguồn | Tài liệu tối thiểu | Điều kiện |
|---|---|---|
| 01 Requirement Analysis | Approved requirements, stories, AC, NFR, business rules, scope | G1 passed |
| 02 System Design | Approved architecture, component design, API, data model, flows, security decisions, ADR | G2 passed |
| 03 Task Planning | [Baseline kế hoạch đã chốt](../../03-task-planning/outputs/planning-output-contract.md#bàn-giao-cho-stage-04), phạm vi task, priority, estimate, dependencies, owner, DoR/DoD | G3 `Approved` đúng phiên bản bàn giao; task thuộc phạm vi duyệt và đạt DoR |

Đầu vào bổ sung: repository conventions, stack, coding/security/test standards, related code/PR, dependency docs, feature flags, migration/compatibility constraints và autonomy config.
