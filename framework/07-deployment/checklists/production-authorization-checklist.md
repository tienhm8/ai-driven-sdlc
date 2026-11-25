# Kiểm tra quyền thực thi Production

Chỉ dùng cho Production, sau [kiểm tra readiness](pre-deployment-checklist.md) và quyết định G6. Checklist này không thay thế kiểm tra của Workflow Engine.

- [ ] Release Manager đã phê duyệt G6 cho đúng artifact SHA-256, môi trường đích và SHA-256 của gói review đã chốt; hồ sơ tham chiếu G5 hợp lệ trên cùng artifact.
- [ ] Không có thay đổi trọng yếu về plan, cấu hình hoặc bằng chứng so với gói review. Nếu có, dừng và xin review mới kể cả khi artifact không đổi. Nếu mở rộng phạm vi G5 đã duyệt, quay lại QA trước.
- [ ] Quyền thực thi được cấp bằng `authorize_action` cho đúng review và bộ giá trị đã duyệt.
- [ ] Ngay trước khi gửi lệnh chạy, adapter gọi `check_action_start` với authorization và bộ giá trị hiện tại. Nếu bị từ chối hoặc quyền hết hiệu lực, không chạy. Không đưa lệnh vào hàng đợi sau khi đã ghi nhận lượt bắt đầu; nếu chạy trì hoãn ở hệ thống khác, adapter tin cậy phải kiểm tra hạn tại thời điểm thực thi.
- [ ] Lưu tham chiếu review, authorization và lượt bắt đầu (`start_event_id`) vào [Deployment Record](../../templates/deployment/deployment-record.md) để đối chiếu kết quả.
