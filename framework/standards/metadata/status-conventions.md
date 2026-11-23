# Quy ước trạng thái (Status Conventions)

## 1. Mục đích

Tài liệu này định nghĩa các trạng thái vòng đời chuẩn dùng để quản lý artifact và work item trong AI-Driven SDLC Framework.

Mục tiêu:

- Chuẩn hóa các giá trị trạng thái vòng đời.
- Giúp dễ hiểu tiến độ của artifact qua các giai đoạn SDLC.
- Hỗ trợ kiểm tra workflow tự động.
- Ngăn chặn chuyển trạng thái không hợp lệ.
- Làm rõ trách nhiệm của AI Agent và người review.

## 2. Các nhóm trạng thái

Framework phân biệt các nhóm trạng thái sau:

1. **Artifact Status**: Mô tả vòng đời của tài liệu hoặc artifact chính thức.
2. **Work Item Status**: Mô tả tiến độ của task hoặc work item.
3. **Gate Decision Status**: Mô tả kết quả của một Human Review Gate.

Artifact Status và Work Item Status được định nghĩa trong tài liệu này.

Gate Decision Status được quản lý riêng tại:

`framework/governance/human-review-gates/`

Các nhóm trạng thái này KHÔNG ĐƯỢC coi là có thể thay thế cho nhau.

## 3. Artifact Status

Trạng thái artifact áp dụng cho yêu cầu, tài liệu thiết kế, đặc tả kiểm thử, tài liệu release và các artifact chính thức khác.

| Trạng thái | Mô tả |
|---|---|
| Draft | Artifact đang được tạo mới hoặc cập nhật. |
| In Review | Artifact đã được gửi để review. |
| Changes Requested | Người review yêu cầu chỉnh sửa. |
| Approved | Artifact đã được người có thẩm quyền phê duyệt chính thức. |
| Rejected | Artifact bị từ chối và không thể tiếp tục ở dạng hiện tại. |
| Deprecated | Artifact không còn được khuyến nghị sử dụng nhưng được giữ lại để tham khảo lịch sử. |

### 3.1 Vòng đời Artifact Status

Vòng đời điển hình:

`Draft → In Review → Approved`

Các chuyển trạng thái thay thế:

- `In Review → Changes Requested`
- `Changes Requested → Draft`
- `In Review → Rejected`
- `Approved → Draft` khi artifact đã duyệt được mở lại thông qua quy trình thay đổi được ủy quyền.
- `Approved → Deprecated` khi artifact được thay thế hoặc không còn áp dụng.

### 3.2 Quy tắc phê duyệt

1. AI Agent có thể tạo và cập nhật artifact ở trạng thái Draft.
2. AI Agent có thể chuẩn bị artifact để review.
3. AI Agent KHÔNG ĐƯỢC tự ý đặt artifact thành Approved.
4. Chỉ vai trò con người được ủy quyền mới được phê duyệt artifact chính thức.
5. Việc phê duyệt PHẢI được ghi nhận với danh tính người review, thời điểm, phiên bản artifact và quyết định.
6. Artifact đã được phê duyệt KHÔNG ĐƯỢC bị sửa đổi một cách âm thầm.
7. Mọi thay đổi có ý nghĩa đối với artifact đã được phê duyệt PHẢI kích hoạt quy trình review áp dụng.

## 4. Work Item Status

Trạng thái work item áp dụng cho task, công việc phát triển, điều tra kỹ thuật, lỗi và các bản ghi thực thi khác.

| Trạng thái | Mô tả |
|---|---|
| Backlog | Work item đã được xác định nhưng chưa sẵn sàng để bắt đầu. |
| Ready | Work item đáp ứng các tiêu chí sẵn sàng đã định nghĩa. |
| In Progress | Công việc đang được thực hiện. |
| Blocked | Công việc không thể tiếp tục do phụ thuộc hoặc vấn đề chưa được giải quyết. |
| In Review | Công việc đang chờ review. |
| Done | Công việc đã đáp ứng tiêu chí hoàn thành. |
| Cancelled | Công việc đã được dừng có chủ đích và sẽ không tiếp tục. |

### 4.1 Vòng đời Work Item

Vòng đời điển hình:

`Backlog → Ready → In Progress → In Review → Done`

Các chuyển trạng thái thay thế:

- `In Progress → Blocked`
- `Blocked → In Progress`
- `In Review → In Progress` khi có yêu cầu chỉnh sửa.
- `Backlog → Cancelled`
- `Ready → Cancelled`
- `In Progress → Cancelled` khi có quyết định được ủy quyền.

### 4.2 Quy tắc hoàn thành

Work item CHỈ được đánh dấu Done khi:

- Tiêu chí nghiệm thu hoặc hoàn thành đã được đáp ứng.
- Phần triển khai hoặc tài liệu bắt buộc đã hoàn tất.
- Các review bắt buộc đã hoàn thành.
- Các test liên quan đã pass, khi áp dụng được.
- Bằng chứng và tham chiếu bắt buộc đã sẵn sàng.

AI Agent KHÔNG ĐƯỢC đánh dấu công việc là Done chỉ vì đã tạo mã nguồn hoặc hoàn thành một bản nháp.

## 5. Quy tắc chuyển trạng thái

Mọi chuyển trạng thái PHẢI tuân thủ:

1. Chuyển trạng thái được vòng đời tương ứng cho phép.
2. Người thực hiện có quyền thực hiện chuyển trạng thái đó.
3. Các điều kiện bắt buộc đã được đáp ứng.
4. Việc chuyển trạng thái PHẢI được ghi nhận.
5. Chuyển trạng thái không hợp lệ PHẢI bị từ chối hoặc được đánh dấu.

Với các chuyển trạng thái có kiểm soát, cần ghi nhận:

- ID của artifact hoặc work item
- Trạng thái trước đó
- Trạng thái mới
- Người thực hiện thay đổi
- Thời điểm thay đổi
- Lý do hoặc ghi chú
- Bản ghi phê duyệt hoặc review liên quan, nếu có

## 6. Trách nhiệm của AI

AI Agent CÓ THỂ:

- Tạo artifact ở trạng thái Draft.
- Cập nhật artifact ở trạng thái Draft.
- Đề xuất chuyển trạng thái.
- Chuyển work item qua các trạng thái thực thi được phép khi được ủy quyền.
- Nhận diện trạng thái không hợp lệ hoặc không nhất quán.
- Chuẩn bị artifact để con người review.

AI Agent KHÔNG ĐƯỢC:

- Phê duyệt artifact thay mặt người có thẩm quyền.
- Bỏ qua yêu cầu review bắt buộc.
- Đánh dấu công việc là Done khi chưa kiểm tra tiêu chí hoàn thành.
- Thay đổi trạng thái của artifact đã được phê duyệt mà không tuân theo quy trình thay đổi.
- Sửa đổi bản ghi lịch sử trạng thái.

## 7. Mở rộng cho dự án

Dự án CÓ THỂ định nghĩa thêm trạng thái cho các workflow cụ thể.

Mọi trạng thái mở rộng PHẢI xác định:

- Tên trạng thái
- Mô tả
- Loại artifact hoặc work item áp dụng
- Các trạng thái trước được phép
- Các trạng thái tiếp theo được phép
- Vai trò chịu trách nhiệm
- Có yêu cầu phê duyệt của con người hay không

Trạng thái riêng của dự án KHÔNG ĐƯỢC làm thay đổi ý nghĩa của các trạng thái bắt buộc của framework.

## 8. Kiểm tra (Validation)

Công cụ kiểm tra tự động NÊN kiểm tra:

- Giá trị trạng thái hợp lệ.
- Chuyển trạng thái được phép.
- Các trường bắt buộc đã có.
- Có bằng chứng phê duyệt cho artifact ở trạng thái Approved.
- Tiêu chí hoàn thành đã được đáp ứng đối với work item ở trạng thái Done.
- Artifact Deprecated không bị tham chiếu nhầm như phiên bản hiện tại.
