# Tích hợp generic

Đích tham khảo: prompt workspace hoặc file hướng dẫn mà tool đang hỗ trợ. Xác nhận quy ước theo phiên bản client đang dùng. Đây là hướng dẫn tích hợp, không phải cấu hình tự kích hoạt.

1. Trong **code repo** đích, giữ nguyên hướng dẫn hiện có. Thêm bản tóm tắt rules chung, phạm vi project và tên các skill cần dùng từ phiên bản Shared AI đã chọn.
2. Nếu dùng skill có tài nguyên kèm theo, giữ nguyên cây tương đối trong skill. Các liên kết sang framework phải trỏ đến bản framework mà môi trường đích đọc được, không giả định repo dùng chung filesystem.
3. Giữ sandbox và quyền mặc định; routing, credentials và approval được quản lý ngoài nội dung prompt. Không đưa token vào instructions.
4. Mở phiên thử, yêu cầu công cụ nêu rule đang áp dụng và đọc một skill; nếu không tìm được, sửa đường dẫn thay vì nới quyền.
