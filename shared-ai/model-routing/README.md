# Model routing

Các YAML v1 đặc tả **chính sách**, không phải tên model hay cấu hình SDK. [Model router](../../platform/model-router/README.md) chưa thực thi chính sách này. Dự án phải ánh xạ từng profile tới model đã duyệt theo provider/môi trường, capability, giới hạn ngân sách và phạm vi xử lý dữ liệu. Không hard-code credential hoặc truyền nguyên effort nội bộ sang API.

1. Đọc task trong [mapping](task-model-mapping.yaml) và risk đã phân loại. Task/risk không xác định → chuyển xử lý thủ công.
2. Tra capability của [profile](model-profiles.yaml); áp dụng mức cao hơn giữa effort của task và sàn rủi ro theo [effort policy](effort-policy.yaml). Thiếu binding hoặc effort không được hỗ trợ → chọn thủ công trong các lựa chọn được duyệt; không hạ effort ngầm.
3. Kiểm tra quyền gửi dữ liệu và ngân sách trước cả lần đầu, retry và fallback. Chỉ retry lỗi tạm thời được liệt kê trong [fallback policy](fallback-policy.yaml), tối đa số lần nêu trong policy; tôn trọng thời gian chờ của provider. Nếu vẫn lỗi tạm thời, dùng tối đa một fallback đã duyệt (không đi theo chuỗi), giữ effort và tối thiểu đủ capability. Không retry/fallback khi gặp từ chối, lỗi ngoài danh sách hoặc có nguy cơ lặp hành động có side effect.
4. Ghi task, risk, profile, model được chọn, effort, kết quả và lý do chuyển tuyến; không ghi payload nhạy cảm. Routing không cấp quyền thực thi hay thay phê duyệt SDLC.

Ví dụ: `documentation` mặc định `routine/low`; nếu công việc được phân loại rủi ro `high`, dùng `routine/high` nếu binding được duyệt hỗ trợ, nếu không thì chọn thủ công.
