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
| ID Requirement / NFR | Artifact / mục thiết kế | Kiểm chứng / việc cần theo dõi |
|---|---|---|

## 5. Quyết định mở và rủi ro tồn dư
| ID | Mô tả | Mức độ | Người phụ trách | Hạn xử lý | Phê duyệt / cách xử lý |
|---|---|---|---|---|---|

## 6. Tham chiếu quyết định G2

Hồ sơ chính thức được liên kết tại trường **Tham chiếu phê duyệt G2** ở mục 1; hồ sơ xác định quyết định, người có thẩm quyền và đúng ID/phiên bản gói đã chốt làm baseline. Không ghi lại quyết định hoặc trạng thái gate tại đây. Đối chiếu phiên bản gói ở mục 1 và danh mục artifact với hồ sơ trước bàn giao; action không chặn và waiver được ghi riêng trong hồ sơ G2.

Chỉ bàn giao khi hồ sơ G2 là `Approved` cho đúng phiên bản gói, sau khi đủ điều kiện và phê duyệt chuyên môn bắt buộc.

**Nếu dự án dùng workflow engine:** trước khi vận hành luồng G2, đơn vị vận hành dịch vụ phải thiết lập kênh tra cứu chỉ đọc có kiểm soát quyền hoặc quy trình xuất bằng chứng có xác thực từ kho sự kiện. Phản hồi hoàn tất stage và màn hình tiến độ mặc định không cung cấp đầy đủ bằng chứng này. Sau khi Stage 02 hoàn tất, bên bàn giao lấy ID sự kiện và bằng chứng từ đơn vị vận hành, rồi gửi cho người nhận cùng approval record; không cấp quyền truy cập trực tiếp kho sự kiện cho người nhận.

Hồ sơ G2 ghi execution ID, review ID, `review_context_sha256`, `artifact_sha256`, ID các quyết định phê duyệt và ID sự kiện hoàn tất Stage 02. Người nhận đối chiếu các giá trị này với bằng chứng từ dịch vụ và xác minh sự kiện hoàn tất qua G2 có `basis: approved`. Hồ sơ Markdown không thay thế bằng chứng audit. Nếu thiếu kênh xác minh, thiếu bằng chứng, có sai lệch hoặc sự kiện có `basis: exception_authorized`, không bàn giao.

**Phạm vi băm:** hồ sơ G2 tham chiếu manifest bất biến dùng tại lần review và quy tắc tính digest của adapter. Manifest bao phủ toàn bộ nội dung thuộc baseline giao cho Stage 03, kể cả dependency map, risk register hay thiết kế triển khai nếu chúng là đầu vào bàn giao. Bổ sung mục vào danh mục artifact nếu cần. Metadata quản lý sau duyệt (trạng thái gói, ngày hiệu lực, tham chiếu phê duyệt và thông tin bàn giao) nằm ngoài manifest; không loại trừ nội dung baseline chỉ vì nó được lưu riêng.

Người nhận dùng cùng quy tắc với adapter để kiểm tra nội dung **thực nhận**: tính lại digest từng artifact từ bản giao khi manifest chứa hash thành phần, rồi tính lại digest của gói theo manifest và so với `artifact_sha256` của sự kiện hoàn tất. Không chỉ đối chiếu hai hash đã ghi sẵn. Thiếu nội dung baseline hoặc digest không khớp thì không bàn giao.

## 7. Bàn giao sang 03 — Task Planning
- [ ] Kiến trúc và ranh giới component đã có sẵn.
- [ ] Công việc liên quan API, dữ liệu, migration và tích hợp đã xác định được.
- [ ] Công việc triển khai bảo mật và NFR đã được xác định.
- [ ] Phụ thuộc, rủi ro và spike/PoC kỹ thuật đã được ghi nhận.
- [ ] Baseline thiết kế và bằng chứng phê duyệt đã được liên kết.

**Người nhận bàn giao:** `[PM / Tech Lead]`  
**Ngày bàn giao:**
