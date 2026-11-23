# Kiểm thử

Dùng unit test cho invariant và adapter giả, integration test cho DB và e2e cho HTTP contract. E2E phải khởi tạo pipes/guards/filters như ứng dụng thật; gọi `app.close()` sau test. Kiểm tra cả validation thất bại và truy cập sai phạm vi.
