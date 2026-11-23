# Xác thực và phân quyền

Dùng guard/strategy đã duyệt để xác minh danh tính từ issuer tin cậy. Sau xác thực, kiểm tra action và phạm vi tenant ở từng tài nguyên. Thử 401 khi thiếu hoặc không hợp lệ, 403 hoặc 404 khi ngoài phạm vi theo contract; không log credential.
