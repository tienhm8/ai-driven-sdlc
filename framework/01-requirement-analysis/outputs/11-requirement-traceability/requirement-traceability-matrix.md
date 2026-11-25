# Ma trận truy vết yêu cầu (Requirement Traceability Matrix — RTM)

## 1. Thông tin tài liệu

| Trường | Giá trị |
|---|---|
| Mã tài liệu | RTM-0001 |
| Dự án | [Tên dự án] |
| Phiên bản | 0.1 |
| Trạng thái | Draft |
| Owner | [Business Analyst] |
| Ngày cập nhật | [YYYY-MM-DD] |

## 2. Phạm vi Stage 01

Truy vết từ **Nguồn / Mục tiêu nghiệp vụ → BRQ → FR/NFR**, rồi qua **User Story (US) hoặc Use Case (UC)** khi áp dụng, đến **Acceptance Criteria (AC)** cho yêu cầu cần nghiệm thu. Nếu không dùng US/UC, liên kết FR/NFR trực tiếp với AC khi cần nghiệm thu. **BR (Business Rule)** có ID riêng, liên kết với FR/NFR, US/UC hoặc AC mà nó chi phối; không thay cho BRQ và không phải một tầng bắt buộc.

Thiết kế, task, implementation, Test Case, kết quả kiểm thử và release/deployment được nối theo ID ở các stage sau. Không yêu cầu các liên kết này để đạt G1.

## 3. Ma trận truy vết Stage 01

| Chiều kiểm tra | Nguồn (ID/tham chiếu) | Đích (ID) | Trạng thái | Lý do / căn cứ / tham chiếu quyết định |
|---|---|---|---|---|
| | | | | |

- Ghi một dòng cho mỗi liên kết hoặc mỗi kiểm tra không có liên kết; dùng ID ổn định. Với nguồn chưa có ID, dùng tham chiếu cụ thể đến tài liệu/mục, stakeholder hoặc quyết định. Với BRQ phát sinh, đánh dấu là **phát sinh** và tham chiếu căn cứ/quyết định; không dùng `N/A` để thay thế nguồn.
- Kiểm tra nhánh FR và NFR **riêng** cho từng BRQ. Ví dụ: `BRQ-0001 → FR-0001: Linked`; nhánh NFR có thể là `N/A` nếu đã đánh giá và có lý do được chấp nhận.
- Với mỗi FR/NFR, chọn US, UC, cả hai hoặc không dùng hình thức nào. Không bắt buộc cả US lẫn UC. Nếu cả hai không áp dụng, ghi `N/A` và lý do; vẫn kiểm tra AC trực tiếp. Nếu không cần AC, ghi `N/A` riêng cho bước nghiệm thu và giải thích; không suy ra `N/A` cho AC từ `N/A` của US/UC.
- Với mỗi NFR, ghi ở cột căn cứ hoặc tham chiếu đến mục cụ thể trong danh mục NFR có tiêu chí đo (chỉ số, ngưỡng, điều kiện đo khi cần) hoặc phương pháp kiểm chứng với kết quả đạt/không đạt rõ ràng. Ví dụ, “hệ thống phải nhanh” chưa đủ; “P95 dưới 500 ms ở 1.000 requests/phút” có cơ sở kiểm chứng khi đã xác định điều kiện đo cần thiết.
- Đối chiếu danh mục artifact trong phạm vi với RTM theo cả hai hướng. Không suy ra đủ độ bao phủ chỉ từ các dòng đã có: kiểm tra cả artifact chưa xuất hiện trong ma trận và các ID sai, không tồn tại hoặc không thuộc baseline đang review.

## 4. Trạng thái và xử lý khoảng trống

| Trạng thái | Ý nghĩa | Đánh giá |
|---|---|---|
| `Linked` | Có liên kết hợp lệ đến đúng artifact trong baseline. | Đạt đối với liên kết đó; vẫn kiểm chất lượng nội dung. |
| `N/A` | Đã đánh giá và xác định liên kết hoặc hình thức đặc tả không áp dụng. | Chỉ đạt khi có lý do cụ thể và tham chiếu chấp nhận của người review. |
| `Missing` | Đã biết cần liên kết nhưng chưa có liên kết hợp lệ. | Chưa đạt. |
| `TBD` | Chưa đủ thông tin để xác định liên kết, tính áp dụng hoặc tiêu chí kiểm chứng. | Chưa đạt đối với mục đó. |
| `Orphan` | Artifact trong phạm vi không có liên kết nguồn hoặc đích bắt buộc. | Chưa đạt; ghi rõ đầu liên kết còn thiếu. |

Ô trống không phải `N/A`. Khi review, phân loại ô trống theo các trạng thái trên. Ghi `Missing`, `TBD`, `Orphan` và các đề xuất `N/A` chưa được chấp nhận vào bảng xử lý. Sau khi xử lý, cập nhật cả dòng truy vết lẫn tham chiếu quyết định; không đổi sang `N/A` chỉ để đóng gap.

| Artifact/ID | Liên kết hoặc thông tin thiếu | Trạng thái truy vết | Tác động / chặn G1? | Owner / hạn xử lý | Hành động / tham chiếu quyết định |
|---|---|---|---|---|---|
| | | | | | |

## 5. Độ bao phủ và điều kiện RTM đạt G1

Đánh giá **từng chiều**, trên danh mục artifact thuộc phiên bản baseline trình duyệt. Đơn vị kiểm tra là từng artifact/nhánh nêu dưới đây, không phải số dòng liên kết (một artifact có thể có nhiều liên kết). Ghi kết quả `PASS / FAIL / PENDING` và tham chiếu các ID hoặc gap liên quan cho từng chiều. Nếu đếm, báo riêng số mục đã kiểm tra theo trạng thái; không tính `N/A` là `Linked` và không dùng một tỷ lệ tổng hợp để quyết định G1.

| Chiều kiểm tra | Điều kiện PASS | Kết quả | Bằng chứng / gap |
|---|---|---|---|
| Nguồn / mục tiêu → BRQ | Mỗi BRQ trong phạm vi có nguồn/mục tiêu tham chiếu được hoặc được ghi là yêu cầu phát sinh kèm căn cứ/quyết định. | | |
| BRQ → FR | Mỗi BRQ có liên kết FR hợp lệ hoặc `N/A` được chấp nhận cho nhánh FR. | | |
| BRQ → NFR | Mỗi BRQ có liên kết NFR hợp lệ hoặc `N/A` được chấp nhận cho nhánh NFR. | | |
| FR/NFR → US/UC | Mỗi FR/NFR có liên kết đến hình thức đặc tả phù hợp hoặc `N/A` được chấp nhận. | | |
| US/UC → AC hoặc FR/NFR → AC trực tiếp | Mỗi yêu cầu cần nghiệm thu có AC rõ ràng, kiểm chứng được và truy vết được; trường hợp không cần AC có `N/A` được chấp nhận. | | |
| BR liên quan | Mỗi BR trong phạm vi liên kết với artifact mà nó chi phối; không dùng BR thay cho BRQ. | | |
| Chất lượng NFR | Mỗi NFR trong phạm vi có tiêu chí đo hoặc cách kiểm chứng đủ để xác định đạt/không đạt. | | |
| Liên kết thiếu và yêu cầu mồ côi | Không còn `Missing` ở liên kết bắt buộc hoặc `Orphan` chưa xử lý; không còn `N/A` chưa được chấp nhận. | | |
| Thông tin chưa xác định | Không còn `TBD` ảnh hưởng đến phạm vi, tính đúng đắn, liên kết bắt buộc hoặc khả năng kiểm chứng của yêu cầu. Mục không chặn G1 phải có tác động, owner, hạn và quyết định chấp nhận được ghi lại. | | |

**Kết luận RTM:** [PASS / FAIL / PENDING] · **Phiên bản baseline / tham chiếu review:** [Tham chiếu].

RTM chỉ `PASS` khi từng chiều đều `PASS`. `FAIL` hoặc `PENDING` do còn tiêu chí bắt buộc chưa đạt hoặc chưa được kiểm tra thì chưa sẵn sàng trình G1. RTM đạt không thay thế quyết định phê duyệt G1 của Product Owner.

## 6. Thay đổi và tác động trong Stage 01

| Change/Decision ID | Artifact/ID thay đổi | Artifact/ID bị ảnh hưởng | Tác động | Owner |
|---|---|---|---|---|

## 7. Bàn giao truy vết cho các stage sau

| Stage | Liên kết bổ sung tại stage tương ứng (không kiểm ở G1) | Owner |
|---|---|---|
| System Design | Requirement → design/ADR/API/data artifacts | Solution Architect |
| Task Planning/Development | Requirement/US → task và implementation | Delivery/Engineering |
| Testing & QA (Stage 06) | Requirement/AC → Test Case và test evidence | QA |
| Deployment | Requirement/AC → release/deployment evidence khi áp dụng | Release owner |

## 8. Lịch sử thay đổi

| Phiên bản | Ngày | Người cập nhật | Mô tả | Nguồn/quyết định |
|---|---|---|---|---|
| 0.1 | [YYYY-MM-DD] | [Owner] | Bản nháp ban đầu | [Nguồn] |
