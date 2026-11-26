# 02 — System Design: Templates

## Mục đích

Thư mục này chứa **biểu mẫu trống** để tạo tài liệu thiết kế. Đây không phải đầu ra của dự án. Khi thiết kế thực tế được tạo, nội dung được điền vào `../outputs/` theo đúng ID và cấu trúc của template tương ứng.

## Kiến trúc

```
templates/
├── README.md                        # Hướng dẫn sử dụng và bảng ánh xạ template → output
├── system-architecture.md           # Kiến trúc hệ thống (ARCH-XXX)
├── architecture-decision-record.md  # Quyết định kiến trúc (ADR-XXX)
├── api-specification.md             # Đặc tả API (API-XXX)
├── database-design.md               # Thiết kế cơ sở dữ liệu (DB-XXX)
├── data-model.md                    # Mô hình dữ liệu (DM-XXX)
├── sequence-diagram.md              # Biểu đồ tuần tự / luồng chính (FLOW-XXX)
└── security-design.md               # Thiết kế bảo mật (SEC-DES-XXX)
```

## Vai trò từng file

| Template | Vai trò | Tạo ra output | Review bằng checklist |
|---|---|---|---|
| `system-architecture.md` | Khuôn mô tả kiến trúc tổng thể: bối cảnh, ranh giới, thành phần, tích hợp, triển khai và đánh đổi. Là tài liệu trung tâm của giai đoạn. | `outputs/architecture/` | `architecture-review-checklist.md` |
| `architecture-decision-record.md` | Khuôn ghi một quyết định kiến trúc trọng yếu: bối cảnh, phương án, quyết định, hệ quả và trạng thái. Mỗi quyết định một ADR. | `outputs/adr/` | `architecture-review-checklist.md` (mục công nghệ và đánh đổi) |
| `api-specification.md` | Khuôn đặc tả contract API: endpoint, schema, xác thực, phân quyền, lỗi, versioning và tương thích ngược. | `outputs/api/` | `api-review-checklist.md` |
| `database-design.md` | Khuôn thiết kế CSDL: engine, bảng, khóa, index, transaction, migration, backup và khôi phục. | `outputs/database/` | `database-data-review-checklist.md` |
| `data-model.md` | Khuôn mô hình dữ liệu theo miền nghiệp vụ: entity, quan hệ, ownership, phân loại dữ liệu và vòng đời. | `outputs/data-model/` | `database-data-review-checklist.md` |
| `sequence-diagram.md` | Khuôn mô tả luồng xử lý chính và ngoại lệ, kèm sơ đồ tuần tự. Liên kết với story và AC. | `outputs/flows/` | `architecture-review-checklist.md` |
| `security-design.md` | Khuôn thiết kế bảo mật: threat model, trust boundary, xác thực, phân quyền, mã hóa, secret và audit. | `outputs/security/` | `security-review-checklist.md` |

## Quy tắc sử dụng

- Điền đủ mục **Kiểm soát tài liệu** (ID, phiên bản, trạng thái, chủ sở hữu, requirement baseline) trước khi viết nội dung.
- Dùng ID theo quy ước `framework/standards/metadata/`, ví dụ `API-0001`, `ADR-0001`, `DB-0001`.
- Artifact không áp dụng phải ghi `N/A` và lý do trong `../outputs/design-package-index.md`.
- Template không được sửa để chứa dữ liệu dự án thật. Dữ liệu thật chỉ nằm trong `../outputs/`.
- Khi template và standard/policy đã duyệt mâu thuẫn, standard/policy có hiệu lực cao hơn (xem `../README.md`).
