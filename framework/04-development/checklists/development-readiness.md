# Development Readiness Checklist (G1/G2/G3 + DoR)

Nguồn kiểm tra duy nhất trước coding. Stage 04 **xác minh**, không phê duyệt lại, baseline G1/G2/G3 và DoR. Thiếu hoặc mâu thuẫn → `Blocked`, trừ ngoại lệ hợp lệ theo [gate policy](../../governance/human-review-gates/gate-policy.md).

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
- [ ] Task thuộc đúng phạm vi đã duyệt; phiên bản kế hoạch chưa bị thay thế và không có thay đổi trọng yếu nào chưa được phê duyệt lại.
- [ ] Task đạt [DoR tối thiểu của framework](../../03-task-planning/templates/definition-of-ready.md) và tiêu chí bổ sung của dự án/tổ chức nếu có; ghi tham chiếu tiêu chí và bằng chứng kiểm tra.

## Môi trường
- [ ] Đã xác định repository, branch và base commit.
- [ ] Lệnh build/test và môi trường dev sẵn sàng.
- [ ] Coding/security standard và cấu hình autonomy sẵn sàng.
- [ ] Dữ liệu test an toàn và được phép sử dụng.

**Kết quả:** Ready / Blocked — **Blocker / owner / hạn xử lý:** — **Bản ghi waiver (nếu có):** — **Người kiểm tra / ngày:**
