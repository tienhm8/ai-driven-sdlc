# Kế hoạch Rollback / Recovery

> Template chuẩn của Stage 07. [File trong thư viện dùng chung](../../templates/deployment/rollback-plan.md) chỉ trỏ về mẫu này.

## 1. Metadata
- Plan ID: `RB-{{NUMBER}}`
- Release / Deployment ID:
- Service/release:
- Environment:
- Current version:
- Target rollback version:
- Artifact digest(s) (SHA-256):
- Plan owner:
- Người review kỹ thuật:
- Decision authority:
- Last tested date và bằng chứng diễn tập:

## 2. Trigger rollback
Định nghĩa các ngưỡng đo được trước khi release:

| Tín hiệu / điều kiện | Ngưỡng | Khoảng thời gian theo dõi | Người quyết định |
|---|---|---|---|
| Health check quan trọng thất bại | | | |
| Error rate | | | |
| Latency/saturation vi phạm SLO | | | |
| Critical user journey / data integrity check thất bại | | | |
| Sự cố bảo mật hoặc lộ dữ liệu ngoài ý muốn | | | |

Ngưỡng phải do service owner/SRE xác nhận theo SLO và policy; không dùng giá trị ví dụ làm mặc định cho production.

## 3. Tác động, điều kiện tiên quyết và ràng buộc
- Thành phần bị ảnh hưởng:
- Executor được ủy quyền:
- Artifact cũ vẫn còn khả dụng:
- Backup/restore point:
- Tương thích schema database:
- Ảnh hưởng session/cache/queue:
- Dependency bên ngoài và side-effect bên ngoài:
- Dữ liệu do phiên bản mới ghi ra:
- Thao tác không thể hoàn tác:
- Rủi ro mất dữ liệu:

## 4. Quyết định và truyền thông
- Thẩm quyền quyết định rollback:
- Executor / Verifier:
- Incident Commander:
- Kênh xử lý sự cố:
- Escalation khẩn cấp:
- Người chịu trách nhiệm thông điệp gửi khách hàng/stakeholder:

## 5. Các bước rollback ứng dụng
| # | Action | Expected result | Owner | Verification |
|---|---|---|---|---|
| 1 | Tạm dừng rollout/traffic shift | Phạm vi phơi nhiễm không tăng thêm | | |
| 2 | Khôi phục app/config version trước khi an toàn | Version ổn định phục vụ traffic | | |
| 3 | Kiểm tra dữ liệu và dependencies | Trạng thái nhất quán | | |
| 4 | Chạy smoke tests và theo dõi metrics | Tiêu chí phục hồi đạt | | |

Điều chỉnh các bước theo nền tảng thực tế. Không chạy lệnh phá hủy chưa được kiểm thử.

## 6. Khôi phục database / dữ liệu
> Cảnh báo: rollback ứng dụng không tự động rollback dữ liệu. Phải quyết định riêng cho dữ liệu.

- Loại migration:
- Có backward-compatible không?:
- Rollback script đã được test chưa?:
- Cách restore/forward-fix:
- Backup/snapshot và restore point:
- Khoảng thời gian có thể mất dữ liệu:
- Owner và phương pháp đối soát dữ liệu:
- Yêu cầu phê duyệt cho restore:

## 7. Tiêu chí thành công / xác minh sau rollback
- [ ] Health checks:
- [ ] Ngưỡng error/latency:
- [ ] Luồng nghiệp vụ quan trọng:
- [ ] Tính toàn vẹn/nhất quán dữ liệu:
- [ ] Monitoring ổn định trong khoảng thời gian theo dõi:
- [ ] Stakeholder đã được thông báo:

## 8. Sau rollback
- Incident/change record:
- Tham chiếu [Deployment Record](../../templates/deployment/deployment-record.md) đã ghi kết quả rollback:
- Theo dõi nguyên nhân gốc:
- Truyền thông với stakeholder:
- Evidence và timestamps:
- Điều kiện để triển khai lại:

## 9. Review
- Người review kỹ thuật:
- Release Manager review (không thay thế quyết định G6):
- Timestamp review:
