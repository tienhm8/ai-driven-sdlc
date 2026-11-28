# Development Readiness Checklist (G1/G2/G3 + DoR)

Nguồn kiểm tra duy nhất trước coding. Stage 04 **xác minh**, không phê duyệt lại, baseline G1/G2/G3 và DoR. Thiếu hoặc mâu thuẫn → `Blocked`, trừ ngoại lệ hợp lệ theo [gate policy](../../governance/human-review-gates/gate-policy.md) hoặc chế độ [prototype-first](#chế-độ-prototype-first) của project.

## Requirement — G1
- [ ] Requirement/story đã duyệt có ID và version.
- [ ] Phạm vi, business rule và AC đo lường được đã rõ ràng.
- [ ] Đã xác định NFR và edge case liên quan.
- [ ] Đã ghi nhận tham chiếu phê duyệt của PO.

## Design — G2
- [ ] Có kiến trúc/thiết kế kỹ thuật đã duyệt.
- [ ] API, mô hình dữ liệu và luồng liên quan đã được đặc tả.
- [ ] Đã xem xét bảo mật, quyền riêng tư và authorization.
- [ ] Ràng buộc migration/tương thích đã được ghi lại.
- [ ] Đã đối chiếu phiên bản design package bàn giao với bằng chứng G2 `Approved` của Solution Architect và các phê duyệt chuyên môn bắt buộc nếu áp dụng.

## Planning — G3
- [ ] Đã đối chiếu ID/phiên bản baseline kế hoạch trong gói bàn giao với input manifest và bản ghi G3 `Approved` (định danh Tech Lead, timestamp và bằng chứng).
- [ ] Task thuộc đúng phạm vi đã duyệt; phiên bản kế hoạch chưa bị thay thế và không còn thay đổi thuộc nhóm `Cần duyệt lại G3` ảnh hưởng đến task mà chưa có quyết định G3 hợp lệ cho phiên bản mới.
- [ ] Nếu có bản đính chính, xác minh Tech Lead đã ghi nhận là `Đính chính` trong nhật ký kế hoạch, bản đính chính dẫn về đúng bản ghi G3 và không thay baseline. Xem [quy tắc thay đổi sau G3](../../03-task-planning/outputs/planning-output-contract.md#thay-đổi-sau-g3).
- [ ] Task đạt [DoR tối thiểu của framework](../../03-task-planning/templates/definition-of-ready.md) và tiêu chí bổ sung của dự án/tổ chức nếu có; ghi tham chiếu tiêu chí và bằng chứng kiểm tra.

## Chế độ prototype-first

Chỉ dùng khi `.ai-sdlc/project.yaml` có `delivery.mode: prototype_first`. Mục này thay cho phần G1/G2/G3 của các gate có trong `deferred_gates`; gate không có trong danh sách vẫn kiểm tra như trên. Xem [prototype-first](../../governance/delivery-modes/prototype-first.md).

- [ ] `delivery.decision_ref` trỏ tới quyết định `Accepted` trong decision log.
- [ ] Đã ghi phiên bản prototype và/hoặc SRS, commit base frontend sẽ dùng.
- [ ] Lát cắt chức năng của task được xác định trong nguồn.
- [ ] Hồ sơ của từng gate hoãn đã có bản `Draft` hoặc `In Review` cho lát cắt (dùng làm baseline tạm), hoặc ghi rõ hồ sơ nào sẽ lập song song.
- [ ] Câu hỏi mở ảnh hưởng tới task đã ghi vào open questions; phần chờ được đánh dấu, không tự điền logic.
- [ ] Task không thuộc phần giới hạn (bảo mật trọng yếu, migration dữ liệu thật, tích hợp có tác động thật).

## Môi trường
- [ ] Đã xác định repository, branch và base commit.
- [ ] Lệnh build/test và môi trường dev sẵn sàng.
- [ ] Coding/security standard và cấu hình autonomy sẵn sàng.
- [ ] Dữ liệu test an toàn và được phép sử dụng.

**Kết quả:** Ready / Blocked — **Blocker / owner / hạn xử lý:** — **Bản ghi waiver (nếu có):** — **Người kiểm tra / ngày:**
