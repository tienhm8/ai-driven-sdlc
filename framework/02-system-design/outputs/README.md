# Outputs — System Design

## Mục đích
Lưu **kết quả thiết kế thực tế của từng project**, được tạo từ `../templates/` và đã rà soát bằng `../checklists/`. Không lưu biểu mẫu trống ở đây.

## Cấu trúc

```
outputs/
├── README.md                    # Quy tắc đầu ra, lifecycle và document control
├── design-package-index.md      # Chỉ mục gói thiết kế: artifact, bằng chứng, G2, bàn giao
├── architecture/                # ARCH-XXX — kiến trúc hệ thống
├── adr/                         # ADR-XXX — quyết định kiến trúc
├── api/                         # API-XXX — đặc tả API
├── database/                    # DB-XXX — thiết kế CSDL
├── data-model/                  # DM-XXX — mô hình dữ liệu
├── flows/                       # FLOW-XXX — luồng xử lý chính
├── security/                    # SEC-DES-XXX — thiết kế bảo mật
└── approvals/                   # G2-XXX — checklist đã điền, bản ghi review và phê duyệt
```

Chỉ tạo thư mục con khi có artifact tương ứng. Thư mục rỗng không được giữ lại để tránh nhầm với trạng thái "thiếu". Artifact không áp dụng ghi N/A và lý do trong index.

## Vai trò từng thành phần

| Thành phần | Vai trò | Trạng thái được phép |
|---|---|---|
| `README.md` | Quy định cấu trúc, lifecycle và document control của output. | — |
| `design-package-index.md` | Điểm vào duy nhất của gói thiết kế. Liệt kê artifact, phiên bản, trạng thái, bằng chứng review, truy vết requirement, rủi ro tồn dư, tham chiếu hồ sơ quyết định G2 và bàn giao sang 03. | Draft / In Review / Approved / Superseded |
| `architecture/` | Bản kiến trúc hệ thống đã điền theo `templates/system-architecture.md`. | Draft → In Review → Approved → Superseded |
| `adr/` | Từng ADR, một file cho một quyết định. Quyết định bị loại cũng được giữ lại để truy vết. | Proposed / Accepted / Rejected / Deprecated / Superseded |
| `api/` | Đặc tả API và contract sự kiện. | Draft → In Review → Approved → Superseded |
| `database/` | Thiết kế CSDL, chiến lược migration và backup. | Draft → In Review → Approved → Superseded |
| `data-model/` | Mô hình dữ liệu và data dictionary theo miền. | Draft → In Review → Approved → Superseded |
| `flows/` | Luồng chính, luồng thay thế và ngoại lệ, kèm sơ đồ tuần tự. | Draft → In Review → Approved → Superseded |
| `security/` | Thiết kế bảo mật và threat model. | Draft → In Review → Approved → Superseded |
| `approvals/` | Checklist đã điền, bằng chứng review, hồ sơ blocker và bản ghi G2 (người phê duyệt, thời điểm, phiên bản đã duyệt). | Pending / In Review / Approved / Rejected / Blocked / Changes Requested |

## Bằng chứng review

- Checklist trong `../checklists/` là mẫu dùng chung. Sao chép bản cần dùng vào `approvals/`, đặt tên theo gói và phiên bản (ví dụ `approvals/G2-001-v1.0-security-review.md`), rồi điền trên bản sao.
- Liên kết mọi checklist đã điền và bằng chứng từ `design-package-index.md`, mục Bằng chứng review.
- Bản ghi quyết định G2 dùng mẫu `framework/templates/review/approval-record.md` và lưu trong `approvals/`. Ai được ghi quyết định: xem [human-review.md](../human-review.md#2-vai-trò-và-trách-nhiệm).

## Lifecycle và document control

`Draft → In Review → Approved → Superseded`

- Mỗi artifact có ID/version/status/owner/date và requirement references.
- Draft/In Review không phải design baseline. Artifact `Approved` phải có tham chiếu phê duyệt và số phiên bản.
- Baseline là vai trò của phiên bản design package đã chốt, không phải trạng thái artifact riêng. Package index tham chiếu approval record; điều kiện chốt baseline xem [human-review.md](../human-review.md#6-điều-kiện-quyết-định-g2).
- Chỉ bàn giao sang `03-task-planning` đúng phiên bản gói đã chốt làm baseline cùng bằng chứng G2 hợp lệ cho phiên bản đó.
- Sau khi duyệt, không sửa âm thầm. Tăng phiên bản, ghi lý do thay đổi, đánh giá tác động và trình duyệt lại; phiên bản mới không tự động kế thừa G2 của phiên bản cũ.
- Không lưu secret, credential hoặc dữ liệu cá nhân thật trong bất kỳ artifact nào.
