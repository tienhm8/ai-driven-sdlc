# Responsible AI Guidelines

## Nguyên tắc
- Human accountability: quyết định quan trọng có owner là con người.
- Fairness: xem xét thiên lệch trong dữ liệu, đánh giá và quyết định.
- Transparency: nêu giới hạn, giả định và độ chắc chắn.
- Privacy: giảm thiểu dữ liệu, bảo vệ thông tin cá nhân/bí mật.
- Safety: ưu tiên phương án giảm thiểu tác động ngoài dự kiến.
- Reliability: kiểm chứng bằng test, nguồn và review phù hợp.
- Contestability: cho phép con người phản biện, sửa và đảo ngược khi có thể.

## Chất lượng đầu ra
Phân biệt sự kiện có bằng chứng, giả định, đề xuất và nội dung chưa xác minh. Không trình bày suy đoán như sự thật; không bịa trích dẫn, test result hoặc nguồn dữ liệu.

## Tác động và fairness
Với hệ thống ảnh hưởng người dùng/khách hàng/nhân viên, xác định nhóm chịu tác động, hậu quả lỗi và nguy cơ kết quả bất công/loại trừ. Yêu cầu domain owner đánh giá khi tác động không thể tự xác minh bằng kỹ thuật.

## Privacy và IP
Tuân thủ [quy tắc bảo vệ dữ liệu đầu vào](ai-security-policy.md#secret-và-dữ-liệu). Kiểm tra license và nguồn gốc dependency/code; xác minh đầu ra không chứa dữ liệu hoặc mã không được phép sử dụng.

## Giám sát
Theo dõi lỗi AI, false positive/negative, sự cố, khiếu nại và tỷ lệ phải sửa output. Đánh giá lại model, prompt, tool và policy khi thay đổi đáng kể.
