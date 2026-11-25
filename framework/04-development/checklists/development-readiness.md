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
- [ ] Đã ghi nhận tham chiếu phê duyệt của Architect/Tech Lead.

## Planning — G3
- [ ] Task có ID, owner, priority, estimate và dependency.
- [ ] Task truy vết được về requirement/AC và thiết kế.
- [ ] Tiêu chí Acceptance/Done rõ ràng.
- [ ] Bản ghi G3 `Approved` bởi Tech Lead, gồm người phê duyệt, timestamp và phiên bản kế hoạch.
- [ ] Task thuộc phạm vi task đã ghi trong bản ghi G3 và kế hoạch chưa có thay đổi trọng yếu nào chưa được phê duyệt lại.
- [ ] Task đạt Definition of Ready (DoR).

## Môi trường
- [ ] Đã xác định repository, branch và base commit.
- [ ] Lệnh build/test và môi trường dev sẵn sàng.
- [ ] Coding/security standard và cấu hình autonomy sẵn sàng.
- [ ] Dữ liệu test an toàn và được phép sử dụng.

**Kết quả:** Ready / Blocked — **Blocker / owner / hạn xử lý:** — **Bản ghi waiver (nếu có):** — **Người kiểm tra / ngày:**
