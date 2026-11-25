# Definition of Ready (DoR) — tiêu chí tối thiểu cho task

Stage 03 dùng các tiêu chí dưới đây khi chuẩn bị task. Stage 04 xác minh chúng trên **task và phiên bản kế hoạch thực tế** trước khi code, theo checklist Development Readiness của Stage 04. DoR không phải G3 và không thay thế kiểm tra phê duyệt G1/G2/G3. DoR kiểm tra task có thể bắt đầu; DoD quy định khi nào công việc hoàn thành.

- [ ] Có ID và owner, mức ưu tiên rõ, phạm vi đủ nhỏ để triển khai, deliverable và phần ngoài phạm vi được ghi khi cần.
- [ ] Có tham chiếu requirement/story, acceptance criteria (AC) và thiết kế liên quan; các nguồn nhất quán với phạm vi task.
- [ ] AC có thể kiểm chứng; đã xác định cách kiểm chứng, điều kiện liên quan (ví dụ NFR hoặc tình huống biên) và DoD áp dụng. Không cần có PR hoặc test case chi tiết trước khi bắt đầu.
- [ ] Có estimate kèm đơn vị và độ tin cậy, hoặc ghi `Not estimated` kèm lý do; giả định ảnh hưởng đến việc bắt đầu đã được làm rõ.
- [ ] Các phụ thuộc cần trước khi bắt đầu đã sẵn sàng. Không còn blocker chưa xử lý khiến task không thể triển khai đúng phạm vi đã duyệt.

Áp dụng thêm tiêu chí của dự án/tổ chức nếu có và dẫn chiếu phiên bản tương ứng. Ghi kết quả `Ready` hoặc `Blocked`, blocker và owner trong checklist Stage 04; không tạo thêm quyết định G3 cho từng task.
