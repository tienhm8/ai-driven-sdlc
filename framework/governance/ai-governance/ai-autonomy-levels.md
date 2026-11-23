# AI Autonomy Levels Policy

## Mục đích
Xác định mức tự chủ AI trong AI-Driven SDLC. Level gắn với từng task/action và rủi ro, không gán cứng cho toàn bộ giai đoạn.

| Level | Mô hình | Ví dụ |
|---|---|---|
| L1 | AI tự thực hiện tác vụ rủi ro thấp trong phạm vi cho phép; không review từng lần | Format code, bản nháp tài liệu, phân loại log, automated checks |
| L2 | AI thực hiện; con người review theo checklist, sampling hoặc trigger | Unit test, refactor nhỏ, tối ưu cục bộ |
| L3 | AI thực hiện/đề xuất; con người bắt buộc review và approve trước khi áp dụng/chuyển bước | Logic nghiệp vụ, API, schema, authorization, xử lý dữ liệu |
| L4 | Con người quyết định; AI chỉ tư vấn, phân tích và đưa phương án | Quyết định bảo mật trọng yếu, production rủi ro cao, migration quan trọng, incident nghiêm trọng |

## Quy tắc
- Mức kiểm soát tăng theo tác động, độ nhạy dữ liệu, phạm vi quyền và khả năng đảo ngược.
- Nếu thiếu thông tin hoặc không xác định được rủi ro, dừng để owner phân loại và áp dụng kiểm soát nghiêm ngặt hơn.
- Quyền đọc không đồng nghĩa quyền ghi; tạo PR không đồng nghĩa merge; chạy test không đồng nghĩa deploy; đề xuất không đồng nghĩa phê duyệt.
- L1/L2 không miễn trừ Gate G1–G7.
- Chi tiết vận hành: `../autonomy-levels/`.
