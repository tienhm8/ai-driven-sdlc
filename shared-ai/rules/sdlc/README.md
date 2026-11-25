# Rules: sdlc

`sdlc/` là nhóm rule bắt buộc được [rule loader bảo vệ mặc định](../../../platform/rule-loader/README.md), cùng với `core/`.

- Xác định giai đoạn từ [Framework](../../../framework/README.md). Đọc workflow, checklist và human review của giai đoạn; không đoán ánh xạ gate.
- Liên kết yêu cầu → thay đổi → bằng chứng kiểm thử → quyết định review; khi yêu cầu đổi, cập nhật liên kết.
- Theo [Governance](../../../framework/governance/README.md), ghi trạng thái gate thực tế và người phê duyệt; thiếu phê duyệt thì đánh dấu chờ thay vì đi tiếp.
