# Chiến lược triển khai (Deployment Strategy)

## 1. Lựa chọn
Chọn dựa trên kiến trúc, tính stateful, traffic, hạ tầng, đặc điểm rollback, chi phí và thời gian downtime chấp nhận được. Ghi nhận lý do lựa chọn.

## 2. Các chiến lược phổ biến

### Recreate
Dừng phiên bản cũ rồi khởi động phiên bản mới.
- Ưu điểm: đơn giản, ít overhead hạ tầng.
- Rủi ro: có downtime; rollback cần deploy lại phiên bản cũ.
- Dùng khi chấp nhận được downtime.

### Rolling
Thay thế instances dần dần.
- Ưu điểm: rollout từng bước, nhu cầu tài nguyên vừa phải.
- Rủi ro: chạy song song nhiều version; yêu cầu backward compatibility và readiness checks.
- Phù hợp với service stateless có nhiều replica.

### Blue-Green
Duy trì hai môi trường cũ và mới; chuyển traffic sau khi xác nhận.
- Ưu điểm: chuyển traffic lại nhanh nếu môi trường cũ còn khỏe.
- Rủi ro: tốn thêm capacity/chi phí; database và side-effect bên ngoài làm việc đảo ngược phức tạp.
- Phù hợp khi có sẵn môi trường song song.

### Canary
Gửi một phần nhỏ traffic đến phiên bản mới, sau đó tăng dần.
- Ưu điểm: giới hạn phạm vi ảnh hưởng và đánh giá dựa trên metrics.
- Rủi ro: cần telemetry tin cậy, khả năng kiểm soát traffic và quan sát có ý nghĩa.
- Phù hợp với service có monitoring trưởng thành.

### Feature flags
Deploy code với tính năng đang tắt, sau đó bật dần.
- Ưu điểm: tách việc deploy khỏi việc release tính năng.
- Rủi ro: flag cũ và code path ẩn; trạng thái flag cần governance.
- Phù hợp khi ứng dụng hỗ trợ bật/tắt an toàn.

## 3. So sánh định tính
| Tiêu chí | Recreate | Rolling | Blue-Green | Canary |
|---|---|---|---|---|
| Mức chấp nhận downtime | Cao | Thấp | Thấp | Thấp |
| Capacity bổ sung | Thấp | Vừa | Cao | Thay đổi |
| Chạy nhiều version | Không/ngắn | Có | Thường tách biệt | Có |
| Kiểm soát traffic | Hạn chế | Theo batch | Chuyển đổi | Chi tiết |
| Nhu cầu telemetry | Cơ bản | Vừa | Vừa | Cao |

Đối chiếu hướng dẫn này với nền tảng thực tế trước khi áp dụng.

## 4. Hệ thống stateful và database
- Ưu tiên expand-and-contract: thêm schema tương thích, deploy code tương thích, backfill/migrate, xóa schema cũ ở release sau.
- Đảm bảo phiên bản ứng dụng cũ và mới cùng tồn tại khi cần.
- Không giả định rollback schema an toàn sau khi đã có ghi dữ liệu.
- Xác định phương án backup, restore, reconciliation và forward-fix.
- Biến đổi dữ liệu không thể đảo ngược là rủi ro cao và cần con người phê duyệt rõ ràng.

## 5. Kiểm soát progressive rollout
Trước khi deploy phải xác định: batch/traffic ban đầu, khoảng thời gian quan sát, health/business metrics, ngưỡng error/latency/saturation, tiêu chí pause/abort, thẩm quyền quyết định và thời lượng rollout tối đa.

## 6. Quyết định rollback
Dùng các trigger đã định nghĩa trước và người ra quyết định được ủy quyền. Với một số thay đổi stateful, mitigation hoặc forward-fix an toàn hơn rollback. Ghi nhận quyết định và evidence.

## 7. Các trường bắt buộc trong plan
Mọi plan phải nêu: chiến lược đã chọn, lý do, điều kiện tiên quyết, trình tự rollout, tiêu chí health, abort triggers, đường rollback/mitigation, owner và kế hoạch truyền thông.
