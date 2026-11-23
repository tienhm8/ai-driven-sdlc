# Mẫu Effort Estimation
| Dự án/kế hoạch | Ngày/phiên bản | Người ước lượng | Phương pháp | Đơn vị | Baseline đầu vào |
|---|---|---|---|---|---|
| | | | `Planning Poker/T-shirt/Three-point/Expert` | `Hours/Days/Points` | |

Không cộng story points với giờ/ngày. Story points mang tính tương đối; muốn quy đổi cần dữ liệu lịch sử và chính sách của team.

| Task ID | Mô tả | O | M | P | Estimate | Đơn vị | Độ tin cậy | Giả định/độ không chắc chắn |
|---|---|---:|---:|---:|---:|---|---|---|
| | | | | | | | `High/Medium/Low` | |

PERT tùy chọn: `E=(O+4M+P)/6`; ghi rõ có dùng hay không.

| Yếu tố | Đánh giá | Ảnh hưởng đến estimate |
|---|---|---|
| Độ rõ ràng của requirement | | |
| Độ phức tạp kỹ thuật | | |
| Tích hợp/dependency | | |
| Migration/chất lượng dữ liệu | | |
| Bảo mật/tuân thủ | | |
| Testing/review/tài liệu | | |

| Hạng mục | Tổng | Đơn vị |
|---|---:|---|
| Phân tích/spike | | |
| Phát triển | | |
| Review/rework | | |
| Testing | | |
| Tài liệu | | |
| Hỗ trợ triển khai | | |
| Tổng | | |

Độ không chắc chắn → spike/hành động xác thực → owner → hạn xử lý. Rà soát: đơn vị nhất quán; effort bao trọn vòng đời; giả định và độ tin cậy được nêu rõ; estimate đã được con người review.
