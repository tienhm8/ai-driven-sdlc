# Performance Checklist

- [ ] Không phát sinh N+1 query hoặc truy vấn không giới hạn.
- [ ] Có pagination/limit cho tập dữ liệu lớn khi phù hợp.
- [ ] Index và query plan được xem xét cho truy vấn quan trọng.
- [ ] Không có blocking I/O hoặc công việc nặng trên critical path không cần thiết.
- [ ] Cache có invalidation/TTL phù hợp nếu được sử dụng.
- [ ] Resource (connection, stream, file, lock) được giải phóng đúng cách.
- [ ] Timeout, retry và concurrency limit được cân nhắc.
- [ ] Benchmark/metric có bằng chứng khi thay đổi được tuyên bố là tối ưu.
