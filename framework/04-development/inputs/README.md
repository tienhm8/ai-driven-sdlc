# Development Inputs

Thư mục này mô tả/tập hợp đầu vào được Development tiêu thụ từ 01–03. Ưu tiên tham chiếu nguồn chuẩn bằng ID, version, URL/path; chỉ snapshot khi cần reproducibility hoặc policy yêu cầu.

## Kiến trúc

```text
inputs/
├── README.md                    # Quy định về đầu vào và điều kiện sử dụng
└── input-manifest-template.md   # Mẫu manifest, lập cho từng task
```

Luồng sử dụng: trước khi code, Developer lập một `input-manifest-template.md` cho task, liệt kê các artifact đã duyệt từ 01–03 kèm version và approval reference. Manifest này là căn cứ để kiểm tra `checklists/development-readiness.md`.

## Vai trò từng file

| File | Vai trò | Ai dùng |
|---|---|---|
| `README.md` | Quy định đầu vào tối thiểu từ 01, 02, 03 và điều kiện G1/G2/G3 phải đạt. Quy định cách tham chiếu (ID/version/commit), xử lý mâu thuẫn và loại dữ liệu không được lưu. | Developer, AI, Tech Lead |
| `input-manifest-template.md` | Ghi lại đầu vào thực tế của từng task: artifact đã duyệt, version, approval, bối cảnh kỹ thuật, trạng thái Ready/Blocked. | Developer lập; Tech Lead xác nhận |

## Quy tắc sử dụng

- Chỉ dùng artifact ở trạng thái Approved. Không dùng Draft thay thế nếu không có waiver được phê duyệt.
- Nếu các nguồn mâu thuẫn, kết quả là Blocked và owner phải giải quyết trước khi tiếp tục.
- Không lưu secret hoặc dữ liệu production nhạy cảm trong manifest.

## Đầu vào theo giai đoạn

| Nguồn | Tài liệu tối thiểu | Điều kiện |
|---|---|---|
| 01 Requirement Analysis | Approved requirements, stories, AC, NFR, business rules, scope | G1 passed |
| 02 System Design | Approved architecture, component design, API, data model, flows, security decisions, ADR | G2 passed |
| 03 Task Planning | Approved backlog/task, priority, estimate, dependencies, owner, DoD | G3 passed |

Đầu vào bổ sung: repository conventions, stack, coding/security/test standards, related code/PR, dependency docs, feature flags, migration/compatibility constraints và autonomy config.
