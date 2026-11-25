# Giả định, ràng buộc, phụ thuộc và rủi ro

## 1. Thông tin tài liệu

| Trường | Giá trị |
|---|---|
| Mã tài liệu | ACDR-0001 |
| Dự án | [Tên dự án] |
| Phiên bản | 0.1 |
| Trạng thái | Draft |
| Owner | [Business Analyst/Project Owner] |
| Ngày cập nhật | [YYYY-MM-DD] |

## 2. Giả định (Assumptions)

| ID | Giả định | Căn cứ/nguồn | Tác động nếu sai | Owner xác minh | Hạn | Trạng thái |
|---|---|---|---|---|---|---|
| ASM-0001 | [Giả định chưa xác nhận] | [Nguồn] | [Tác động] | [Owner] | [Ngày] | Unverified |

Trạng thái gợi ý: `Unverified`, `Confirmed`, `Rejected`, `Superseded`.

## 3. Ràng buộc (Constraints)

| ID | Loại | Ràng buộc | Nguồn/căn cứ | Tác động | Owner | Trạng thái |
|---|---|---|---|---|---|---|
| CON-0001 | [Business/Technical/Legal/Budget/Time/Other] | [Nội dung] | [Nguồn] | [Tác động] | [Owner] | Draft |

## 4. Phụ thuộc (Dependencies)

| ID | Phụ thuộc vào | Mô tả/giao diện | Bên cung cấp/owner | Hạn hoặc mốc | Tác động nếu trễ/thay đổi | Trạng thái |
|---|---|---|---|---|---|---|
| DPN-0001 | [Hệ thống/nhóm/quyết định] | [Nội dung] | [Owner] | [Ngày/mốc] | [Tác động] | Identified |

## 5. Rủi ro (Risks)

| ID | Sự kiện rủi ro và nguyên nhân | Xác suất | Tác động | Mức độ | Giảm thiểu/ứng phó | Owner | Trạng thái |
|---|---|---|---|---|---|---|---|
| RISK-0001 | [Mô tả] | [Thấp/Trung bình/Cao] | [Mô tả] | [Mức] | [Hành động] | [Owner] | Open |

## 6. Tham chiếu câu hỏi mở

Câu hỏi được quản lý duy nhất trong `../outputs/10-assumptions-constraints-risks/open-questions.md`; ghi OQ ID liên quan tại đây khi cần liên kết với assumption, constraint, dependency hoặc risk.

- OQ IDs liên quan: [Danh sách ID]

## 7. Lịch sử thay đổi

| Phiên bản | Ngày | Người cập nhật | Mô tả | Nguồn/quyết định |
|---|---|---|---|---|
| 0.1 | [YYYY-MM-DD] | [Owner] | Bản nháp ban đầu | [Nguồn] |
