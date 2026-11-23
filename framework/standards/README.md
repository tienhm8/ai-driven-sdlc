# Tiêu chuẩn kỹ thuật (Engineering Standards)

## 1. Mục đích

Thư mục này định nghĩa các tiêu chuẩn kỹ thuật chung áp dụng cho tất cả dự án sử dụng AI-Driven SDLC Framework.

Các tiêu chuẩn này thiết lập thực hành nhất quán cho:

- Kiến trúc phần mềm và thiết kế hệ thống.
- Thiết kế API và cơ sở dữ liệu.
- Phát triển mã nguồn.
- Kiểm thử phần mềm và đảm bảo chất lượng.
- Tài liệu kỹ thuật.
- Bảo mật ứng dụng và hạ tầng.

Các tiêu chuẩn là tài liệu tham chiếu chung cho cả kỹ sư và AI Agent trong suốt vòng đời phát triển phần mềm.

## 2. Nội dung của từng nhóm

| Nhóm | File | Nội dung quy định |
|---|---|---|
| `architecture/` | `api-standards.md` | REST/GraphQL conventions, API naming, HTTP methods, response format, error handling, pagination, versioning API, authentication |
| | `database-standards.md` | Database naming, schema, table/column conventions, data types, indexing, relationships, migration, transaction |
| `coding/` | `coding-standards.md` | Code style, naming trong source code, folder/package structure, error handling, logging, exception handling, code quality |
| | `testing-standards.md` | Test pyramid, unit/integration/e2e testing, test naming, test data, coverage, mocking, test quality |
| `documentation/` | `documentation-standards.md` | Cấu trúc tài liệu, Markdown conventions, cách viết, heading, table, diagram, documentation structure, cách liên kết tài liệu |
| `security/` | `security-standards.md` | Authentication, authorization, secrets management, encryption, input validation, OWASP, dependency security, secure coding |
| `metadata/` | `id-conventions.md` | ID format, prefix, uniqueness, relationship giữa các ID, quy tắc không tái sử dụng ID |
| | `status-conventions.md` | Trạng thái vòng đời của artifact và work item, quy tắc chuyển trạng thái |
| | `naming-conventions.md` | Quy tắc đặt tên file, folder, artifact, branch và các thành phần quản lý |
| | `versioning-conventions.md` | Versioning cho framework, template, document và các artifact |

## 3. Phạm vi áp dụng

Các tiêu chuẩn này áp dụng cho:

- Tất cả dự án áp dụng framework này.
- Tất cả giai đoạn của vòng đời phát triển phần mềm.
- Kỹ sư, người review kỹ thuật và các bên liên quan của dự án.
- AI Agent, trợ lý lập trình và công cụ phát triển tự động.
- Các artifact phần mềm được tạo ra hoặc chỉnh sửa trong quá trình thực hiện dự án.

## 4. Mức độ tuân thủ

Mỗi yêu cầu trong tiêu chuẩn cần được hiểu theo các mức sau:

| Mức | Ý nghĩa |
|---|---|
| MUST | Yêu cầu bắt buộc. Dự án phải tuân thủ trừ khi có ngoại lệ đã được phê duyệt. |
| SHOULD | Thực hành khuyến nghị. Mọi sai lệch cần có lý do được ghi nhận. |
| MAY | Thực hành tùy chọn, có thể áp dụng tùy theo nhu cầu dự án. |

## 5. Mở rộng riêng cho từng dự án

Dự án có thể định nghĩa thêm tiêu chuẩn trong repository của dự án.

Tiêu chuẩn riêng của dự án phải:

1. Nhất quán với framework chung.
2. Không làm suy yếu các yêu cầu bắt buộc về bảo mật hoặc governance.
3. Ghi rõ các yêu cầu riêng của dự án.
4. Được review và phê duyệt bởi người có thẩm quyền kỹ thuật phụ trách.
5. Được quản lý phiên bản và có khả năng truy vết.

Khi dự án cần sai lệch so với tiêu chuẩn bắt buộc, sai lệch đó phải được ghi nhận và phê duyệt thông qua quy trình governance của dự án.

## 6. Cách kết nối các standards với 8 SDLC stages

Để tránh việc tạo ra nhiều tài liệu nhưng AI không biết lúc nào cần đọc, cần có quy tắc tham chiếu rõ ràng.

| SDLC Stage | Standards cần áp dụng |
|---|---|
| 01. Requirement Analysis | Documentation, Security |
| 02. System Design | Architecture, API, Database, Security, Documentation |
| 03. Task Planning | Documentation, Metadata, Security |
| 04. Development | Coding, Architecture, API, Database, Security, Documentation |
| 05. Code Review | Coding, Testing, Security |
| 06. Testing & QA | Testing, Security, Documentation |
| 07. Deployment | Security, Database, Documentation |
| 08. Monitoring & Maintenance | Security, Coding, Testing, Documentation |

Đây là ma trận tham chiếu ban đầu. Mỗi stage có thể bổ sung các tiêu chuẩn cụ thể theo phạm vi công việc.

### 6.1 Nguyên tắc: tham chiếu, không nhúng nội dung

Không nên nhúng toàn bộ nội dung các standards vào `ai-instructions.md` của từng stage.

Thay vào đó, mỗi stage chỉ cần khai báo những tiêu chuẩn bắt buộc phải đọc.

Như vậy, `standards/` trở thành nguồn quy định chuẩn duy nhất, còn các stage chỉ xác định tiêu chuẩn nào cần áp dụng. Cách này giúp framework mở rộng thêm project, ngôn ngữ lập trình và AI Agent mà không phải sao chép hoặc duy trì nhiều phiên bản quy định giống nhau.

> **Lưu ý:** Các đường dẫn trong ví dụ dưới đây là đường dẫn logic từ cấu trúc framework. Khi triển khai thực tế, cần thống nhất cách tham chiếu theo vị trí repository và cơ chế loader.

Ví dụ trong `04-development/ai-instructions.md`:

```markdown
## Applicable Engineering Standards

Before implementing any code, AI MUST read and comply with:

- `framework/standards/coding/coding-standards.md`
- `framework/standards/architecture/api-standards.md`
- `framework/standards/architecture/database-standards.md`
- `framework/standards/security/security-standards.md`
- `framework/standards/documentation/documentation-standards.md`

Technology-specific coding guidelines MUST also be loaded from the project configuration.
```

## 7. Yêu cầu tuân thủ đối với AI

AI Agent PHẢI:

- Đọc các tiêu chuẩn liên quan trước khi thực hiện tác vụ có liên quan.
- Tuân thủ các yêu cầu bắt buộc khi tạo hoặc chỉnh sửa artifact.
- Nhận diện các vi phạm tiềm ẩn trong quá trình review.
- Không tự đặt ra quy ước riêng của dự án.
- Báo cáo xung đột giữa chỉ dẫn của dự án và tiêu chuẩn của framework.
- Ghi nhận hoặc báo cáo các sai lệch cần con người phê duyệt.

AI Agent KHÔNG ĐƯỢC tự ý phê duyệt ngoại lệ đối với tiêu chuẩn bắt buộc.

## 8. Trách nhiệm sở hữu tiêu chuẩn

| Tiêu chuẩn | Vai trò chịu trách nhiệm |
|---|---|
| Architecture | Solution Architect |
| API and Database | Solution Architect / Technical Lead |
| Coding | Technical Lead |
| Testing | QA Lead |
| Documentation | Technical Writer / Technical Lead |
| Security | Security Engineer / Security Lead |
| Metadata | Framework Maintainer |

## 9. Bảo trì

Tiêu chuẩn cần được review định kỳ và mỗi khi có thay đổi đáng kể về:

- Công nghệ sử dụng.
- Yêu cầu bảo mật.
- Nguyên tắc kiến trúc.
- Thực hành kỹ thuật.
- Nghĩa vụ pháp lý hoặc tuân thủ quy định.

Mọi thay đổi phải được quản lý phiên bản và thông báo cho các dự án bị ảnh hưởng.

## 10. Governance liên quan

- `../governance/ai-governance/`
- `../governance/autonomy-levels/`
- `../governance/human-review-gates/`
- `../standards/metadata/`
