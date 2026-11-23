# Shared AI

Tài nguyên AI dùng chung cho các dự án áp dụng [SDLC Framework](../framework/README.md).

| Nhóm | Dùng khi |
|---|---|
| [Rules](rules/core/README.md) | Áp dụng ràng buộc chung, [SDLC](rules/sdlc/README.md) và [engineering](rules/engineering/README.md). |
| [Skills](skills/) | Nạp `SKILL.md` theo công việc và stack thực tế; không nạp toàn bộ thư viện. |
| [Agents](agents/) | Chọn `AGENT.md` theo vai trò; đây là hướng dẫn, không phải quyền thực thi. |
| [Model routing](model-routing/README.md) | Chọn profile và effort; ánh xạ runtime phải được cấu hình riêng. |
| [Knowledge](knowledge/) | Tra cứu quyết định kiến trúc, dữ liệu, bảo mật và vận hành. |
| [Tool configs](tool-configs/generic/README.md) | Tích hợp thủ công theo công cụ khi loader chưa có. |

## Bắt đầu

1. Đọc project context, stack, phạm vi và phiên bản framework/shared resources được dự án chọn.
2. Áp dụng governance của framework, rules chung, rồi rules dự án tương thích. Khi xung đột về quyền, chọn giới hạn nghiêm hơn; nếu không xác định được, dừng hành động liên quan và báo người phụ trách.
3. Chọn vai trò và skill theo task. Ví dụ: thay endpoint NestJS → Developer + NestJS + Testing; đọc quy trình Development và yêu cầu review tương ứng.
4. Ghi lại kết quả, lệnh kiểm tra đã chạy, việc chưa xác minh và gate cần con người quyết định.

Không tự cài adapter, cấp quyền, gửi dữ liệu ra ngoài hay gọi provider chỉ vì tài nguyên này được nạp. Khi cập nhật, giữ ID ổn định, kiểm tra liên kết và ghi rõ thay đổi không tương thích trước khi dự án nâng phiên bản.
