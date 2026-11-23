# Kế hoạch Rollback / Recovery

## 1. Metadata
- Service/release:
- Environment:
- Current version:
- Target rollback version:
- Artifact digest(s):
- Plan owner:
- Decision authority:
- Last tested date:

## 2. Trigger rollback
Định nghĩa các ngưỡng đo được trước khi release, ví dụ:
- Health check quan trọng thất bại trong [window].
- Error rate vượt [threshold] trong [duration].
- Latency/saturation vi phạm SLO/ngưỡng đã thống nhất.
- Critical user journey hoặc data integrity check thất bại.
- Xảy ra sự cố bảo mật hoặc lộ dữ liệu ngoài ý muốn.

Không dùng các ngưỡng ví dụ khi chưa được service owner/SRE xác nhận.

## 3. Điều kiện tiên quyết và ràng buộc
- Executor được ủy quyền:
- Artifact cũ vẫn còn khả dụng:
- Backup/restore point:
- Tương thích schema database:
- Ảnh hưởng session/cache/queue:
- Side-effect bên ngoài:
- Rủi ro mất dữ liệu:

## 4. Quyết định và truyền thông
- Thẩm quyền quyết định rollback:
- Executor:
- Verifier:
- Kênh truyền thông:
- Escalation khẩn cấp:

## 5. Các bước rollback
| # | Action | Expected result | Owner | Verification |
|---|---|---|---|---|
| 1 | Tạm dừng rollout/traffic shift | Phạm vi phơi nhiễm không tăng thêm | | |
| 2 | Khôi phục app/config version trước khi an toàn | Version ổn định phục vụ traffic | | |
| 3 | Kiểm tra dữ liệu và dependencies | Trạng thái nhất quán | | |
| 4 | Chạy smoke tests và theo dõi metrics | Tiêu chí phục hồi đạt | | |

Điều chỉnh các bước theo nền tảng thực tế. Không chạy lệnh phá hủy chưa được kiểm thử.

## 6. Khôi phục database
- Loại migration:
- Có backward-compatible không?:
- Rollback script đã được test chưa?:
- Cách restore/forward-fix:
- Owner đối soát dữ liệu:
- Cảnh báo: rollback ứng dụng không tự động rollback dữ liệu.

## 7. Tiêu chí thành công
- Health checks:
- Ngưỡng error/latency:
- Luồng nghiệp vụ quan trọng:
- Tính toàn vẹn dữ liệu:
- Thời gian theo dõi:

## 8. Sau rollback
- Incident/change record:
- Theo dõi nguyên nhân gốc:
- Truyền thông với stakeholder:
- Evidence và timestamps:
- Điều kiện để triển khai lại:
