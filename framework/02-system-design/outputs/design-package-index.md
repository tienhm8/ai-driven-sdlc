# Chỉ mục Gói Thiết kế Hệ thống

> Danh mục quản lý tài liệu thiết kế đầu ra của dự án. Cập nhật đường dẫn, phiên bản và trạng thái thực tế.

## 1. Thông tin gói
| Trường | Giá trị |
|---|---|
| Dự án / Hệ thống | `[Tên dự án]` |
| ID gói thiết kế | `[DES-PKG-XXX]` |
| Phiên bản gói | `[1.0]` |
| Requirement baseline | `[ID/phiên bản REQ-BASELINE]` |
| Chủ sở hữu gói | `[Architect]` |
| Trạng thái | `Draft / In Review / Approved / Superseded` |
| Tham chiếu phê duyệt G2 | `[Link]` |
| Ngày có hiệu lực | `[YYYY-MM-DD]` |

Trạng thái gói chỉ được là `Approved` khi hồ sơ G2 là `Approved` cho đúng ID và phiên bản gói; trạng thái này không thay thế việc đối chiếu hồ sơ G2.

## 2. Danh mục artifact
| Loại artifact | ID artifact | File / URL | Phiên bản | Trạng thái | Chủ sở hữu |
|---|---|---|---|---|---|
| System Architecture (Kiến trúc hệ thống) | `ARCH-XXX` | `architecture/...` | | | |
| ADR (Quyết định kiến trúc) | `ADR-XXX` | `adr/...` | | | |
| API Specification (Đặc tả API) | `API-XXX` | `api/...` | | | |
| Database Design (Thiết kế CSDL) | `DB-XXX` | `database/...` | | | |
| Data Model (Mô hình dữ liệu) | `DM-XXX` | `data-model/...` | | | |
| Sequence Diagram(s) (Biểu đồ tuần tự) | `FLOW-XXX` | `flows/...` | | | |
| Security Design (Thiết kế bảo mật) | `SEC-DES-XXX` | `security/...` | | | |
| Phê duyệt G2 | `G2-XXX` | `approvals/...` | | | |

Ghi `N/A` và lý do nếu không áp dụng; không để lẫn trạng thái thiếu với không áp dụng.

## 3. Bằng chứng review
| Checklist | Người review | Kết quả | Bằng chứng / liên kết |
|---|---|---|---|
| Review kiến trúc | | | |
| Review API | | | |
| Review database & dữ liệu | | | |
| Review bảo mật | | | |
| Checklist phê duyệt G2 | | | |

## 4. Truy vết yêu cầu
| ID Requirement / NFR | Artifact / mục thiết kế | Kiểm chứng / việc cần theo dõi |
|---|---|---|

## 5. Quyết định mở và rủi ro tồn dư
| ID | Mô tả | Mức độ | Người phụ trách | Hạn xử lý | Phê duyệt / cách xử lý |
|---|---|---|---|---|---|

## 6. Tham chiếu quyết định G2

Hồ sơ chính thức được liên kết tại trường **Tham chiếu phê duyệt G2** ở mục 1; hồ sơ xác định quyết định, người có thẩm quyền và đúng ID/phiên bản gói đã chốt làm baseline. Không ghi lại quyết định hoặc trạng thái gate tại đây. Đối chiếu phiên bản gói ở mục 1 và danh mục artifact với hồ sơ trước bàn giao; action không chặn và waiver được ghi riêng trong hồ sơ G2.

Chỉ bàn giao khi hồ sơ G2 là `Approved` cho đúng phiên bản gói, sau khi đủ điều kiện và phê duyệt chuyên môn bắt buộc.

## 7. Bàn giao sang 03 — Task Planning
- [ ] Kiến trúc và ranh giới component đã có sẵn.
- [ ] Công việc liên quan API, dữ liệu, migration và tích hợp đã xác định được.
- [ ] Công việc triển khai bảo mật và NFR đã được xác định.
- [ ] Phụ thuộc, rủi ro và spike/PoC kỹ thuật đã được ghi nhận.
- [ ] Baseline thiết kế và bằng chứng phê duyệt đã được liên kết.

**Người nhận bàn giao:** `[PM / Tech Lead]`  
**Ngày bàn giao:**
