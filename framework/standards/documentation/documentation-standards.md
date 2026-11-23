# Tiêu chuẩn tài liệu (Documentation Standards)

## 1. Mục đích

Định nghĩa các quy tắc nhất quán cho việc tạo, tổ chức, định dạng, review và bảo trì tài liệu trong mọi dự án sử dụng AI-Driven SDLC Framework.

## 2. Nguyên tắc tài liệu

Mọi tài liệu PHẢI:

- Chính xác: Phản ánh đúng trạng thái hệ thống đã được phê duyệt và trạng thái thực tế.
- Rõ ràng: Dễ hiểu đối với người đọc mục tiêu.
- Nhất quán: Tuân theo thuật ngữ và định dạng chung.
- Có khả năng truy vết: Liên kết các yêu cầu, thiết kế, task, test và release liên quan.
- Dễ bảo trì: Dễ cập nhật và review.
- Đúng trọng tâm: Chứa thông tin cần thiết, tránh trùng lặp không cần thiết.
- Được quản lý phiên bản: Mọi thay đổi phải có khả năng truy vết.

## 3. Định dạng tài liệu

Markdown (`.md`) NÊN là định dạng mặc định cho tài liệu kỹ thuật dạng văn bản.

Có thể sử dụng định dạng khác khi cần thiết, ví dụ:

- PDF cho tài liệu đã xuất bản hoặc phân phát chính thức.
- DOCX cho tài liệu nghiệp vụ cần cộng tác với bên ngoài.
- XLSX cho các sổ đăng ký (register) có cấu trúc hoặc dữ liệu bảng chi tiết.
- PNG, SVG hoặc Mermaid cho sơ đồ.
- YAML hoặc JSON cho cấu hình có thể đọc bằng máy.

Khi một tài liệu tồn tại ở nhiều định dạng, nguồn dữ liệu chính (source of truth) PHẢI được xác định rõ ràng.

## 4. Tổ chức file và thư mục

Tài liệu PHẢI tuân theo cấu trúc thư mục tài liệu của dự án.

Quy tắc chung:

- Dùng chữ thường cho tên.
- Dùng kebab-case cho tên file.
- Dùng tên mô tả rõ ràng.
- Tránh viết tắt mơ hồ.
- Tránh lồng thư mục không cần thiết.
- Tách biệt tiêu chuẩn chung của framework khỏi tài liệu riêng của dự án.

Ví dụ:

```text
docs/
├── 01-requirement-analysis/
│   ├── business-requirements.md
│   ├── user-stories/
│   └── acceptance-criteria/
├── 02-system-design/
│   ├── solution-design.md
│   └── architecture-decisions/
└── project-management/
    ├── risk-register.md
    └── decision-log.md
```

## 5. Cấu trúc tài liệu

Tài liệu NÊN sử dụng cấu trúc nhất quán phù hợp với mục đích của nó.

Khi áp dụng được, tài liệu NÊN gồm:

1. Tiêu đề.
2. Mục đích.
3. Phạm vi.
4. Nội dung.
5. Giả định và ràng buộc.
6. Tài liệu tham chiếu.
7. Thông tin phê duyệt hoặc review.
8. Lịch sử thay đổi.

Không phải tài liệu nào cũng cần đủ mọi mục. Template PHẢI định nghĩa cấu trúc bắt buộc cho từng loại artifact.

## 6. Định dạng Markdown

### 6.1 Tiêu đề

- Dùng một tiêu đề H1 (`#`) cho tiêu đề tài liệu.
- Dùng H2 (`##`) cho các mục lớn.
- Dùng H3 (`###`) cho các mục con.
- Tránh bỏ qua cấp tiêu đề mà không có lý do.
- Dùng tiêu đề mô tả rõ nội dung.

### 6.2 Danh sách

Dùng danh sách đánh số cho các bước hoặc chuỗi có thứ tự.

Dùng danh sách gạch đầu dòng cho thông tin không có thứ tự.

Dùng checklist cho các mục review cần thực hiện.

### 6.3 Bảng

Dùng bảng cho thông tin có cấu trúc, dễ so sánh theo hàng và cột.

Bảng NÊN:

- Có tên cột rõ ràng.
- Tránh quá rộng.
- Tránh chứa đoạn văn dài.
- Dùng thuật ngữ nhất quán.

### 6.4 Khối code

Khối code PHẢI chỉ rõ ngôn ngữ khi áp dụng được.

Ví dụ:

```python
def calculate_total(items):
    return sum(item.price for item in items)
```

### 6.5 Sơ đồ

Dùng Mermaid hoặc công cụ vẽ sơ đồ đã được phê duyệt khi sơ đồ giúp làm rõ nội dung.

Sơ đồ NÊN:

- Có tiêu đề hoặc mục đích rõ ràng.
- Dùng tên nhất quán.
- Tránh phức tạp không cần thiết.
- Được cập nhật khi thiết kế nền tảng thay đổi.

## 7. Metadata của tài liệu

Tài liệu NÊN chứa metadata phù hợp với loại artifact.

Metadata thường gặp gồm:

| Trường | Mô tả |
|---|---|
| ID | Định danh duy nhất của artifact |
| Title | Tiêu đề tài liệu |
| Status | Trạng thái vòng đời hiện tại |
| Version | Phiên bản tài liệu |
| Owner | Người hoặc vai trò chịu trách nhiệm |
| Created Date | Ngày tạo |
| Updated Date | Ngày cập nhật gần nhất |
| Related Artifacts | Các requirement, thiết kế, task hoặc test liên quan |

Quy tắc chính xác về ID, status, đặt tên và version PHẢI tuân theo:

- `../metadata/id-conventions.md`
- `../metadata/status-conventions.md`
- `../metadata/naming-conventions.md`
- `../metadata/versioning-conventions.md`

Tài liệu này chỉ định nghĩa cách trình bày metadata, không định nghĩa quy tắc vòng đời của metadata.

## 8. Ngôn ngữ và thuật ngữ

Dự án PHẢI xác định ngôn ngữ tài liệu chính.

Thuật ngữ kỹ thuật NÊN nhất quán xuyên suốt dự án.

Khi thuật ngữ kỹ thuật không có cách dịch rõ ràng sang ngôn ngữ chính, có thể giữ nguyên thuật ngữ gốc.

Nên duy trì bảng thuật ngữ (glossary) cho các thuật ngữ đặc thù của domain khi cần thiết.

## 9. Truy vết và tham chiếu chéo

Tài liệu PHẢI cung cấp khả năng truy vết khi áp dụng được.

Ví dụ:

- Business Requirement → User Story.
- User Story → Acceptance Criteria.
- Requirement → Thiết kế.
- Thiết kế → Development Task.
- Requirement → Test Case.
- Kết quả test → Release.
- Incident → Defect hoặc Change.

Tham chiếu chéo NÊN dùng ID artifact ổn định thay vì chỉ dựa vào tên file.

Liên kết PHẢI được cập nhật khi tài liệu bị di chuyển hoặc đổi tên.

## 10. Bảo trì tài liệu

Tài liệu PHẢI được cập nhật khi có thay đổi liên quan trong:

- Yêu cầu nghiệp vụ.
- Kiến trúc.
- Contract API.
- Schema cơ sở dữ liệu.
- Hành vi của mã nguồn.
- Chiến lược kiểm thử.
- Quy trình triển khai.
- Quy trình vận hành.

Tài liệu đã lỗi thời NÊN được đánh dấu deprecated hoặc superseded theo quy ước metadata.

## 11. Review và phê duyệt

Tài liệu PHẢI tuân theo quy trình review và phê duyệt áp dụng.

Yêu cầu phê duyệt phụ thuộc vào loại tài liệu và Human Review Gate liên quan.

AI Agent CÓ THỂ tạo, cập nhật và review tài liệu nhưng KHÔNG ĐƯỢC khẳng định đã có phê duyệt của con người.

## 12. Quy tắc tài liệu cho AI

AI Agent PHẢI:

- Dùng template đã được phê duyệt khi có sẵn.
- Tuân theo quy ước Markdown.
- Giữ nguyên cấu trúc tài liệu hiện có khi phù hợp.
- Dùng ID artifact hợp lệ.
- Duy trì khả năng truy vết.
- Phân biệt sự kiện với giả định.
- Đánh dấu rõ các thông tin chưa được giải quyết.
- Không bịa đặt phê duyệt, quyết định hoặc bằng chứng.
- Cập nhật tài liệu liên quan khi cần.
- Kiểm tra liên kết nội bộ và tham chiếu khi có công cụ hỗ trợ.

Tài liệu do AI tạo ra PHẢI được review theo governance của dự án.

## 13. Checklist chất lượng tài liệu

- [ ] Mục đích và phạm vi rõ ràng.
- [ ] Nội dung chính xác và đầy đủ.
- [ ] Sử dụng đúng template.
- [ ] Tiêu đề và định dạng nhất quán.
- [ ] Metadata tuân theo quy ước của framework.
- [ ] Các artifact liên quan đã được liên kết.
- [ ] Giả định và câu hỏi còn mở đã được nêu rõ.
- [ ] Các yêu cầu phê duyệt đã được đáp ứng.
- [ ] Không lộ secret hoặc dữ liệu nhạy cảm.
- [ ] Tài liệu phản ánh đúng trạng thái hiện tại của dự án.

## 14. Tài liệu tham chiếu

- `../metadata/`
- `../architecture/`
- `../coding/`
- `../security/security-standards.md`
