# Chỉ mục Gói Thiết kế Hệ thống

> Danh mục quản lý tài liệu thiết kế đầu ra của dự án. Cập nhật đường dẫn, phiên bản và trạng thái thực tế.

## 1. Thông tin gói
| Trường | Giá trị |
|---|---|
| Dự án / Hệ thống | `[Tên dự án]` |
| ID gói thiết kế | `[DES-PKG-XXX]` |
| Phiên bản gói | `[1.0]` |
| Requirement baseline | `[ID/phiên bản REQ-BASELINE]` |
| Tham chiếu input manifest | `[Link tới manifest nhận baseline và RTM đã duyệt ở G1]` |
| Chủ sở hữu gói | `[Architect]` |
| Trạng thái | `Draft / In Review / Approved / Superseded` |
| Tham chiếu phê duyệt G2 | `[Approval record ID / link]` |
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

Ghi `N/A` và lý do nếu không áp dụng; không để lẫn trạng thái thiếu với không áp dụng. Hồ sơ G2 chỉ được tham chiếu ở mục 1 và mục 6, không liệt kê ở đây để tránh một trạng thái thứ hai.

## 3. Bằng chứng review
| Checklist | Người review | Kết quả | Bằng chứng / liên kết |
|---|---|---|---|
| Review kiến trúc | | | |
| Review API | | | |
| Review database & dữ liệu | | | |
| Review bảo mật | | | |
| Checklist phê duyệt G2 | | | |

## 4. Truy vết yêu cầu

Đây là bảng truy vết thiết kế chính thức của Stage 02. Dùng ID từ đúng baseline G1 ở mục 1; không sửa RTM đã duyệt để thêm liên kết thiết kế.

| ID FR/NFR | ID AC (khi áp dụng) | Artifact / mục thiết kế | Cách kiểm chứng dự kiến |
|---|---|---|---|

Đối chiếu các FR/NFR trong phạm vi với bảng, không chỉ kiểm những dòng đã điền. Nếu AC không áp dụng theo baseline G1, ghi `N/A` và dẫn chiếu lý do đã được chấp nhận. Ghi gap thiếu liên kết, thiếu thiết kế hoặc yêu cầu mâu thuẫn ở mục 5; chuyển BA/PO xử lý nếu cần thay đổi baseline. Cách kiểm chứng dự kiến không phải kết quả kiểm chứng; không cần ID task ở Stage 02.

## 5. Quyết định mở và rủi ro tồn dư
| ID | Mô tả | Mức độ | Người phụ trách | Hạn xử lý | Phê duyệt / cách xử lý |
|---|---|---|---|---|---|

## 6. Tham chiếu quyết định G2

Hồ sơ chính thức được liên kết tại trường **Tham chiếu phê duyệt G2** ở mục 1; hồ sơ xác định quyết định, người có thẩm quyền và đúng ID/phiên bản gói đã chốt làm baseline. Không ghi lại quyết định hoặc trạng thái gate tại đây. Đối chiếu phiên bản gói ở mục 1 và danh mục artifact với hồ sơ trước bàn giao; action không chặn và waiver được ghi riêng trong hồ sơ G2.

Chỉ bàn giao khi hồ sơ G2 là `Approved` cho đúng phiên bản gói, sau khi đủ điều kiện và phê duyệt chuyên môn bắt buộc.

**Nếu dự án dùng workflow engine**, hồ sơ G2 phải ghi: execution ID, review ID, `review_context_sha256`, `artifact_sha256` của gói đã duyệt, ID các quyết định phê duyệt tham chiếu và ID sự kiện hoàn tất Stage 02. Người nhận xác minh bằng tra cứu chỉ đọc do dịch vụ cung cấp hoặc bản xuất có xác thực, không truy cập trực tiếp kho sự kiện, rằng sự kiện hoàn tất có `basis: approved` và khớp từng giá trị trên. Chỉ `basis: approved` được chấp nhận; `exception_authorized` hoặc thiếu sự kiện thì không bàn giao.

**Phạm vi băm:** hồ sơ G2 ghi rõ manifest được băm, gồm các artifact và phiên bản ở mục 2. Các trường quản lý sau duyệt (trạng thái gói, ngày hiệu lực, tham chiếu phê duyệt, mục 7 và ngày bàn giao) nằm ngoài phạm vi băm; không sửa nội dung artifact sau khi duyệt. Hồ sơ Markdown là bằng chứng hỗ trợ, không thay thế xác minh này; nếu thiếu hoặc không khớp, chưa bàn giao.

## 7. Bàn giao sang 03 — Task Planning
- [ ] Kiến trúc và ranh giới component đã có sẵn.
- [ ] Công việc liên quan API, dữ liệu, migration và tích hợp đã xác định được.
- [ ] Công việc triển khai bảo mật và NFR đã được xác định.
- [ ] Phụ thuộc, rủi ro và spike/PoC kỹ thuật đã được ghi nhận.
- [ ] Baseline thiết kế và bằng chứng phê duyệt đã được liên kết.
- [ ] Bảng truy vết ở mục 4 đã được đối chiếu với baseline G1 và sẵn sàng cho Stage 03 sử dụng.

Stage 03 phân rã các hạng mục bàn giao thành task, xác định người phụ trách và nối task về requirement và mục thiết kế.

**Người nhận bàn giao:** `[PM / Tech Lead]`  
**Ngày bàn giao:**
