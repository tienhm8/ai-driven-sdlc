# G4 – Code Review & Merge Approval

**Thời điểm:** Sau code review và CI; trước merge vào protected branch.  
**Approver:** Reviewer/Senior Developer hoặc Tech Lead có thẩm quyền theo repository policy.

## AI chuẩn bị
Diff analysis, findings, security/performance review, test evidence, CI status và report gắn với head commit SHA.

## Điều kiện thông qua
- [ ] PR gắn requirement/task và đúng scope.
- [ ] Review đúng base/head SHA.
- [ ] Dùng [thang severity của Stage 05](../../05-code-review/human-review.md#4-phân-loại-finding). Finding Critical còn mở luôn chặn G4 và merge; phải sửa và review lại, không chấp nhận ngoại lệ.
- [ ] Finding High còn mở chặn theo mặc định; chỉ được giữ lại nếu policy cho phép, người có thẩm quyền chấp nhận rủi ro và ngoại lệ được ghi theo [gate policy](gate-policy.md#ngoại-lệ).
- [ ] Finding còn lại có quyết định xử lý phù hợp với severity; nếu follow-up cho Medium, ghi owner và deadline.
- [ ] CI, build và test bắt buộc đạt.
- [ ] Security review bổ sung hoàn tất nếu cần.
- [ ] API/schema/migration/compatibility được xem xét khi liên quan.
- [ ] Approval của người có thẩm quyền được ghi nhận.

## Quy tắc
AI review không thay human approval. Tác giả PR không được tự phê duyệt, theo [quy tắc chung của gate](gate-policy.md#quy-tắc), kể cả khi có vai trò approver phù hợp. Push commit mới sau approval phải kích hoạt re-review theo branch policy. AI không được merge hoặc bỏ required checks trái policy.

**Quyết định:** Áp dụng [policy chung về quyết định và trạng thái gate](gate-policy.md#reviewer-decision).

**Bằng chứng riêng của G4:** Repository/PR, base/head SHA, người review code nếu khác approver, findings và cách xử lý, CI run và merge commit từ kết quả merge đã xác minh.
