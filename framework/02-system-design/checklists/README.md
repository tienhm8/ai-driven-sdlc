# 02 — System Design: Checklists

## Mục đích

Thư mục này chứa các checklist kiểm tra chất lượng và tính đầy đủ của thiết kế trước khi trình G2. Mỗi checklist có kết quả, người review, bằng chứng và ngoại lệ được ghi lại.

## Kiến trúc

```
checklists/
├── README.md                          # Hướng dẫn thực hiện và trạng thái
├── architecture-review-checklist.md   # Review kiến trúc tổng thể, ADR, luồng
├── api-review-checklist.md            # Review đặc tả API
├── database-data-review-checklist.md  # Review CSDL và mô hình dữ liệu
├── security-review-checklist.md       # Review thiết kế bảo mật
└── g2-design-approval-checklist.md    # Tổng hợp điều kiện G2 (chỉ con người phê duyệt)
```

## Vai trò từng file

| Checklist | Vai trò | Kiểm tra output | Người review chính |
|---|---|---|---|
| `architecture-review-checklist.md` | Kiểm tra kiến trúc có truy vết về requirement baseline, ranh giới rõ, failure mode, observability, topology triển khai và ADR cho công nghệ. | `outputs/architecture/`, `outputs/adr/`, `outputs/flows/` | Solution Architect, Tech Lead |
| `api-review-checklist.md` | Kiểm tra API: đặt tên, schema, xác thực và phân quyền ở mức object và field, error model, versioning, idempotency, rate limit và contract test. | `outputs/api/` | API / Integration Owner |
| `database-data-review-checklist.md` | Kiểm tra CSDL và mô hình dữ liệu: khóa, ràng buộc, index, transaction, phân loại PII, lưu giữ, migration, backup và RPO/RTO. | `outputs/database/`, `outputs/data-model/` | DBA / Data Architect |
| `security-review-checklist.md` | Kiểm tra bảo mật: trust boundary, threat model, xác thực, least privilege, mã hóa, quản lý secret, audit và rủi ro tồn dư. | `outputs/security/` | Security Architect / Security Engineer |
| `g2-design-approval-checklist.md` | Tổng hợp điều kiện G2: đầy đủ, chất lượng, findings Critical/High đã xử lý, handoff sang Task Planning và liên kết hồ sơ phê duyệt. | `outputs/design-package-index.md`, `outputs/approvals/` | Solution Architect (approver chính) |

## Quy tắc thực hiện

- Mỗi mục kiểm tra ghi một trong các kết quả: **Pass**, **Pass with actions**, **Fail** hoặc **N/A**.
- Mục **Fail** hoặc **N/A** phải ghi bằng chứng hoặc lý do. Mục N/A không được để trống.
- Phát hiện **blocking** (Critical/High) phải có hành động, người phụ trách và hạn xử lý.
- AI có thể điền sẵn các mục dựa trên tài liệu, nhưng **không được tự kết luận Pass cho mục cần chuyên gia xác nhận**.
- Các file trong thư mục này là mẫu dùng chung, không điền trực tiếp. Bản đã điền được lưu theo [quy định đầu ra](../outputs/README.md#bằng-chứng-review).
- Checklist chỉ ghi tiêu chí, kết quả và bằng chứng. Thẩm quyền quyết định G2 và cách xử lý khi thiếu approver: xem [human-review.md](../human-review.md#6-điều-kiện-quyết-định-g2).
