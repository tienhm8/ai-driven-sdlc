# G3 — Checklist Phê duyệt Planning
Gate: trước khi bắt đầu code. **Tech Lead phê duyệt** theo [chính sách gate](../../governance/human-review-gates/gate-policy.md); PO xác nhận priority và trade-off sản phẩm; PM xác nhận lịch và nguồn lực. AI không tự phê duyệt G3.

G3 duyệt **một phiên bản kế hoạch với phạm vi task xác định**. Checklist này không thay DoR của từng task; Stage 04 xác minh DoR trước coding.

- [ ] Đã tham chiếu requirement baseline và bằng chứng G1.
- [ ] Đã tham chiếu design baseline (đúng phiên bản package) và bằng chứng G2.
- [ ] Phạm vi task được duyệt đã ghi rõ (danh sách/khoảng task ID, version) và task ngoài phạm vi được nêu nếu có.
- [ ] PO đã xác nhận priority; PM đã xác nhận lịch và nguồn lực.
- [ ] Task breakdown truy vết được, có scope, owner, deliverable và cách kiểm chứng.
- [ ] Estimate có đơn vị, phương pháp, độ tin cậy và được con người review.
- [ ] Dependency matrix có thứ tự thực hiện, owner và biện pháp giảm thiểu.
- [ ] Kế hoạch vừa với capacity hoặc ngoại lệ đã được phê duyệt.
- [ ] DoD đã được định nghĩa/tham chiếu.
- [ ] Task rủi ro cao có reviewer hoặc phê duyệt chuyên môn phù hợp theo policy; công việc kiểm chứng, tài liệu và bảo mật đã được tính đến khi áp dụng.
- [ ] Rủi ro, giả định và vấn đề còn mở đều có owner.
- [ ] Outputs được version hóa và có lịch sử thay đổi.

Lưu checklist đã điền làm bằng chứng; ghi phạm vi, kết luận PO/PM và quyết định trong [bản ghi phê duyệt chung](../../templates/review/approval-record.md), phần dành cho G3. Ghi rõ tên/định danh Tech Lead, vai trò, thời điểm, phiên bản và bằng chứng theo [gate policy](../../governance/human-review-gates/gate-policy.md).

Không có quyết định `Approved` kèm bằng chứng thì Stage 04 chưa được phép bắt đầu. Thay đổi trọng yếu sau duyệt (phạm vi task, priority, estimate/dependency ảnh hưởng lịch, baseline nguồn) cần đánh giá lại và phê duyệt G3 mới cho phiên bản mới.
