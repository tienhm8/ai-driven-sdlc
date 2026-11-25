# Checklist sau triển khai

- [ ] Deployment dùng đúng artifact digest đã phê duyệt.
- [ ] Tất cả instances/nodes/regions dự kiến báo đúng version.
- [ ] Readiness/liveness/health checks đạt.
- [ ] Smoke tests và critical user journeys đạt.
- [ ] Error rate, latency, saturation và availability đạt ngưỡng đã thống nhất.
- [ ] Logs không có lỗi critical hoặc cảnh báo bảo mật mới.
- [ ] Background jobs, queues, scheduled tasks và integrations hoạt động bình thường.
- [ ] Kiểm tra migration và tính toàn vẹn dữ liệu đạt.
- [ ] Feature flags và traffic routing ở trạng thái dự kiến.
- [ ] Không có debug endpoint hoặc cấu hình test nào bị lộ ngoài ý muốn.
- [ ] Stakeholders đã được thông báo kết quả.
- [ ] [Deployment Record](../../templates/deployment/deployment-record.md) và bằng chứng kết quả đã được lưu; ghi đúng phiên bản thực tế và trạng thái xác minh.
- [ ] Runbooks, dashboards và service version inventory đã được cập nhật theo trạng thái thực tế.
- [ ] Chỉ bàn giao Stage 08 khi Production thành công đã xác minh; với rollback/thất bại/chưa rõ, ghi bàn giao thông tin sự cố nếu cần và giữ Stage 07.
