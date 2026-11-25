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
`Draft → In Review → Approved → Superseded`

- Draft/In Review không phải design baseline; Approved phải có approval reference và version.
- Baseline là vai trò của phiên bản design package đã chốt, không phải trạng thái artifact riêng. G2 chỉ hoàn tất với quyết định Approved và đủ các phê duyệt chuyên môn bắt buộc. Điều kiện cần đóng được ghi là Changes Requested; thiếu bằng chứng hoặc phê duyệt bắt buộc là Blocked. Không bàn giao trước khi G2 Approved. Khi G2 Approved, Solution Architect chốt phiên bản gói đã duyệt làm baseline; approval record G2 ghi phiên bản, quyết định, waiver hợp lệ (nếu có), người duyệt và thời điểm; package index chỉ tham chiếu hồ sơ quyết định.
- Đầu vào chính thức của `03-task-planning` là đúng phiên bản gói đã chốt làm baseline cùng bằng chứng G2 hợp lệ cho phiên bản đó. G2 → Stage 03 Task Planning → G3 → coding tại Stage 04.
- Thay đổi sau phê duyệt phải tăng version, đánh giá tác động và review/approval lại; phiên bản mới không tự động kế thừa G2 của phiên bản cũ.

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
| `design-package-index.md` | Điểm vào duy nhất của gói thiết kế. Liệt kê artifact, phiên bản, trạng thái, bằng chứng review, truy vết requirement, rủi ro tồn dư, tham chiếu hồ sơ quyết định G2 và bàn giao sang 03. | Draft / In Review / Approved / Superseded |
| `architecture/` | Chứa bản kiến trúc hệ thống đã điền theo `templates/system-architecture.md`. | Draft → In Review → Approved → Superseded |
| `adr/` | Chứa từng ADR, một file cho một quyết định. Quyết định bị loại cũng được giữ lại để truy vết. | Proposed / Accepted / Rejected / Deprecated / Superseded |
| `api/` | Chứa đặc tả API và contract sự kiện. | Draft → In Review → Approved → Superseded |
| `database/` | Chứa thiết kế CSDL, chiến lược migration và backup. | Draft → In Review → Approved → Superseded |
| `data-model/` | Chứa mô hình dữ liệu và data dictionary theo miền. | Draft → In Review → Approved → Superseded |
| `flows/` | Chứa luồng chính, luồng thay thế và ngoại lệ, kèm sơ đồ tuần tự. | Draft → In Review → Approved → Superseded |
| `security/` | Chứa thiết kế bảo mật và threat model. | Draft → In Review → Approved → Superseded |
| `approvals/` | Chứa bằng chứng review và bản ghi G2: người phê duyệt, thời điểm, phiên bản đã duyệt. Chỉ con người được ghi quyết định. | Pending / In Review / Approved / Rejected / Blocked / Changes Requested |

## Quy tắc đầu ra

- Artifact được tạo từ `../templates/` và đã qua `../checklists/` trước khi đưa vào đây.
- Artifact `Approved` phải có tham chiếu phê duyệt và số phiên bản.
- Chỉ bàn giao đúng phiên bản design package đã chốt làm baseline và có bằng chứng G2 hợp lệ cho phiên bản đó sang `03-task-planning`.
- Sau khi duyệt, không sửa âm thầm. Tăng phiên bản, ghi lý do thay đổi, đánh giá tác động và trình duyệt lại.
- Không lưu secret, credential hoặc dữ liệu cá nhân thật trong bất kỳ artifact nào.
