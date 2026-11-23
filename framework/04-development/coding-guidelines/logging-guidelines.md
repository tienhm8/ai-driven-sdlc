# Logging Guidelines

## Structured log
- Ưu tiên các field có cấu trúc, tên và kiểu dữ liệu ổn định. Dùng timestamp nhất quán (khuyến nghị UTC).
- Truyền correlation/request/trace ID qua các ranh giới service. Bổ sung service, môi trường, build và operation khi hữu ích.
- Tránh nối chuỗi tự do khi đã có structured logging.

## Mức độ nghiêm trọng
| Mức | Sử dụng khi |
|---|---|
| TRACE | Chi tiết chẩn đoán sâu, được kiểm soát |
| DEBUG | Phát triển / khắc phục sự cố |
| INFO | Hoạt động bình thường có ý nghĩa |
| WARN | Bất thường có thể phục hồi hoặc cần chú ý |
| ERROR | Thao tác thất bại và cần điều tra |
| FATAL/CRITICAL | Service/chức năng quan trọng không thể tiếp tục |

Không log lặp lại cùng một exception mà không bổ sung ngữ cảnh. Tránh biến các kết quả nghiệp vụ bình thường thành nhiễu ERROR.

## Dữ liệu nhạy cảm
Không bao giờ log mật khẩu, token, API key, private key, chuỗi kết nối có credential, dữ liệu xác thực thanh toán hoặc PII nhạy cảm nếu không có cơ sở pháp lý/chính sách rõ ràng. Redact/mask theo chính sách. Mặc định không log toàn bộ request/response body; chỉ log các field an toàn đã được cho phép.

## Vận hành
- Dùng tên event/mã code rõ ràng; chỉ ghi chi tiết exception ở nơi được kiểm soát truy cập.
- Ngăn log injection bằng cách encode/chuẩn hóa giá trị không đáng tin. Tránh payload lớn và log tần suất cao trong vòng lặp chặt.
- Áp dụng chính sách lưu giữ, kiểm soát truy cập, mã hóa và xóa. Tách audit log khi yêu cầu về tính toàn vẹn khác nhau.
- Kiểm tra việc truyền correlation, redaction secret/PII, thời gian lưu giữ và khối lượng/cardinality.

Ví dụ: `level=INFO event=order.created correlation_id=... order_id=... duration_ms=...` (không chứa credential/PII).
