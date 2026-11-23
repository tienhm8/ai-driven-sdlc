# Root Cause Analysis (RCA)

## Khái niệm
- **Trigger:** sự kiện khởi phát gần nhất.
- **Root cause:** nguyên nhân nền tảng có thể xử lý để giảm tái diễn.
- **Contributing factors:** yếu tố làm tăng xác suất hoặc tác động.
- **Detection gap:** vì sao phát hiện/cảnh báo chưa đủ sớm.
- **Recovery gap:** vì sao khôi phục chậm/khó.

Một incident có thể có nhiều nguyên nhân và yếu tố góp phần.

## Quy trình
1. Xác định phạm vi, incident ID, service/version và câu hỏi RCA.
2. Bảo toàn logs, metrics, traces, deploy/config events, timeline; tuân thủ privacy/retention.
3. Lập timeline thống nhất timezone; phân biệt event time và detection time.
4. Đối chiếu giả thuyết với evidence và tìm bằng chứng phản bác.
5. Dùng 5 Whys, fault tree hoặc causal graph khi phù hợp.
6. Đánh giá detection, response, mitigation và recovery.
7. Tạo actions theo prevention/detection/mitigation/recovery.
8. Review với các nhóm liên quan và cập nhật backlog.

## Chất lượng kết luận
Nêu evidence/reference, confidence và unknowns. Không kết luận chỉ từ tương quan; không quy kết cá nhân. Phân tích quyết định trong bối cảnh thông tin tại thời điểm xảy ra.

## Action items
Mỗi action có outcome, owner, priority, due date, dependency, verification và status. Ưu tiên loại bỏ nguyên nhân/rào chắn hệ thống thay vì chỉ nhắc nhở.

AI có thể tóm tắt timeline và đề xuất giả thuyết; con người xác minh quan hệ nhân quả và chấp nhận kết luận.
