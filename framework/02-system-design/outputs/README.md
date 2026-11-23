# Outputs — System Design

## Mục đích
Lưu **kết quả thiết kế thực tế của từng project**, được tạo từ `templates/` và đã rà soát bằng `checklists/`. Không lưu biểu mẫu trống ở đây.

## Bộ output điển hình
- System Architecture.
- ADR(s).
- API Specifications.
- Database Design.
- Data Model.
- Sequence Diagrams / Key Flow Designs.
- Security Design.
- Review evidence và G2 approval record.

## Cấu trúc khuyến nghị
```text
outputs/
├── design-package-index.md
├── architecture/
├── adr/
├── api/
├── database/
├── data-model/
├── flows/
├── security/
└── approvals/
```
Chỉ tạo thư mục con khi có artifact tương ứng.

## Lifecycle
`Draft → In Review → Approved → Baselined → Superseded`

- Draft/In Review không phải design baseline.
- Approved phải có approval reference và version.
- Baselined là đầu vào chính thức của `03-task-planning`.
- Thay đổi sau phê duyệt phải tăng version, đánh giá tác động và review/approval lại.

Mỗi artifact cần ID/version/status/owner/date và requirement references. Artifact không áp dụng phải ghi N/A và lý do trong index. Không lưu secret, credential hoặc dữ liệu cá nhân thật.

## Kiến trúc

```
outputs/
├── README.md                    # Quy tắc đầu ra, lifecycle và document control
├── design-package-index.md      # Chỉ mục gói thiết kế: artifact, bằng chứng, G2, bàn giao
├── architecture/                # ARCH-XXX — kiến trúc hệ thống      (tạo khi có artifact)
├── adr/                         # ADR-XXX — quyết định kiến trúc     (tạo khi có artifact)
├── api/                         # API-XXX — đặc tả API               (tạo khi có artifact)
├── database/                    # DB-XXX — thiết kế CSDL             (tạo khi có artifact)
├── data-model/                  # DM-XXX — mô hình dữ liệu           (tạo khi có artifact)
├── flows/                       # FLOW-XXX — luồng xử lý chính       (tạo khi có artifact)
├── security/                    # SEC-DES-XXX — thiết kế bảo mật     (tạo khi có artifact)
└── approvals/                   # G2-XXX — bản ghi review và phê duyệt (tạo khi có artifact)
```

Chỉ tạo thư mục con khi có artifact tương ứng. Thư mục rỗng không được giữ lại để tránh nhầm với trạng thái "thiếu".

## Vai trò từng thành phần

| Thành phần | Vai trò | Trạng thái được phép |
|---|---|---|
| `README.md` | Quy định lifecycle, document control và quyền phê duyệt của output. | — |
| `design-package-index.md` | Điểm vào duy nhất của gói thiết kế. Liệt kê artifact, phiên bản, trạng thái, bằng chứng review, truy vết requirement, rủi ro tồn dư, quyết định G2 và bàn giao sang 03. | Draft / In Review / Approved / Baselined |
| `architecture/` | Chứa bản kiến trúc hệ thống đã điền theo `templates/system-architecture.md`. | Draft → Approved → Baselined |
| `adr/` | Chứa từng ADR, một file cho một quyết định. Quyết định bị loại cũng được giữ lại để truy vết. | Proposed / Accepted / Rejected / Deprecated / Superseded |
| `api/` | Chứa đặc tả API và contract sự kiện. | Draft → Approved → Baselined |
| `database/` | Chứa thiết kế CSDL, chiến lược migration và backup. | Draft → Approved → Baselined |
| `data-model/` | Chứa mô hình dữ liệu và data dictionary theo miền. | Draft → Approved → Baselined |
| `flows/` | Chứa luồng chính, luồng thay thế và ngoại lệ, kèm sơ đồ tuần tự. | Draft → Approved → Baselined |
| `security/` | Chứa thiết kế bảo mật và threat model. | Draft → Approved → Baselined |
| `approvals/` | Chứa bằng chứng review và bản ghi G2: người phê duyệt, thời điểm, phiên bản đã duyệt. Chỉ con người được ghi quyết định. | Pending / Passed / Failed |

## Quy tắc đầu ra

- Artifact được tạo từ `../templates/` và đã qua `../checklists/` trước khi đưa vào đây.
- Artifact `Approved` phải có tham chiếu phê duyệt và số phiên bản.
- Chỉ artifact `Baselined` mới là đầu vào chính thức cho `03-task-planning`.
- Sau khi duyệt, không sửa âm thầm. Tăng phiên bản, ghi lý do thay đổi, đánh giá tác động và trình duyệt lại.
- Không lưu secret, credential hoặc dữ liệu cá nhân thật trong bất kỳ artifact nào.
