# Câu hỏi mở (Open Questions)

Các câu hỏi có lifecycle chi tiết được ghi tại đây và liên kết với Assumptions/Constraints/Dependencies/Risks bằng ID. Đây là register bắt buộc; không bỏ câu hỏi critical vào ghi chú tự do.

## Phân nhóm và mức quyết định

Mỗi câu hỏi có một **Nhóm** (ai quyết định) và một **Mức quyết định** (mức [autonomy](../../../governance/ai-governance/ai-autonomy-levels.md) áp dụng khi trả lời). Cả hai do AI hoặc BA đề xuất; người có thẩm quyền có thể đổi. Dùng hai cột này thay cho một file phân loại riêng; không tạo thêm artifact ngoài bộ chuẩn của giai đoạn.

| Nhóm | Ai quyết định | Mức | Ý nghĩa |
|---|---|---|---|
| A | PO / stakeholder nghiệp vụ | L4 | Quyết định nghiệp vụ, chính sách, ngoại lệ. AI chỉ nêu phương án. |
| B | BA chuẩn bị phương án, PO chốt | L4 | Luồng hoặc hồ sơ chưa có nơi xử lý, cần phương án trước khi quyết. |
| C | Tech Lead (BA phối hợp) | L3 | Ràng buộc kỹ thuật và tích hợp; chủ yếu chặn thiết kế. |
| D | BA xác nhận | L3 | Đầu vào mâu thuẫn hoặc thiếu logic; PO duyệt khi vào baseline. |

Câu hỏi sinh ra từ lỗi của tài liệu đầu vào (ví dụ đầu vào do AI sinh có quy tắc chép sai màn) thuộc nhóm D; phần còn lại phân theo người có thẩm quyền quyết định.

## Danh sách câu hỏi

| OQ ID | Câu hỏi cần quyết định/xác minh | Nguồn/Artifact bị ảnh hưởng | Tác động nếu chưa giải quyết | Critical với G1/Design? | Nhóm | Mức quyết định | Owner | Hạn | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| OQ-0001 | | | | [Yes/No] | [A/B/C/D] | [L3/L4] | | | OPEN |

## Chi tiết câu hỏi

### OQ-0001 — [Tóm tắt]

- Câu hỏi:
- Bối cảnh/nguồn:
- Lý do cần làm rõ:
- Các phương án (nếu có):
- Tác động:
- Owner quyết định/trả lời:
- Bên liên quan chịu trách nhiệm:
- Hạn/ngày dự kiến giải quyết:
- Artifact/ID liên quan:
- Quyết định/câu trả lời:
- Bằng chứng/nguồn xác nhận:
- Trạng thái: OPEN

Quy tắc giải quyết: AI có thể đề xuất câu trả lời khả dĩ nhưng không được coi đề xuất là sự thật đã phê duyệt. Stakeholder nghiệp vụ có thẩm quyền phải xác nhận quyết định nghiệp vụ; ghi câu trả lời và bằng chứng giải quyết. Trạng thái gợi ý: `OPEN`, `ANSWERED`, `ACCEPTED`, `CLOSED`. Câu hỏi critical ngăn cản thiết kế phải được giải quyết trước khi hoàn thành Stage 01; câu hỏi khác cần owner, hạn và được PO chấp nhận nếu vẫn mở lúc G1.

## Lịch sử thay đổi

| Ngày | OQ ID | Thay đổi | Người cập nhật |
|---|---|---|---|
