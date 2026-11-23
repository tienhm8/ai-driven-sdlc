# Xử lý ngoại lệ

Giữ HTTP status và error code ổn định. Map lỗi domain đã biết sang 4xx theo contract; lỗi bất ngờ trả 500 chung. Filter/log dùng request ID và lọc token, stack trace hoặc thông tin DB khỏi response.
