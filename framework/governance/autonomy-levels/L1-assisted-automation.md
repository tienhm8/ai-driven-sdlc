# L1 – Controlled Automation

AI tự thực hiện tác vụ lặp lại, rủi ro thấp, phạm vi hẹp và có thể kiểm chứng; không cần review từng lần.

**Ví dụ:** format code; tạo nháp tài liệu/changelog; phân loại log không nhạy cảm; chạy lint/test read-only đã được phê duyệt.

**Điều kiện:** input/output rõ; tool/quyền allowlist; validation tự động và log; có cách phát hiện lỗi/dừng; không tác động production hoặc dữ liệu nhạy cảm.

**Không thuộc L1:** merge, deploy, thay đổi quyền, xóa dữ liệu, thay đổi logic nghiệp vụ hoặc bỏ qua Gate. Theo dõi lỗi/sampling; khi sai lệch thì nâng mức kiểm soát.
