# G4 – Code Review & Merge Approval

**Thời điểm:** Sau code review và CI; trước merge vào protected branch.  
**Approver:** Reviewer/Senior Developer hoặc Tech Lead có thẩm quyền theo repository policy.

## AI chuẩn bị
Diff analysis, findings, security/performance review, test evidence, CI status và report gắn với head commit SHA.

## Điều kiện thông qua
- [ ] PR gắn requirement/task và đúng scope.
- [ ] Review đúng base/head SHA.
- [ ] Không còn Critical/High finding chưa xử lý.
- [ ] Finding còn lại có disposition hợp lệ; accepted risk có approver và lý do.
- [ ] CI, build và test bắt buộc đạt.
- [ ] Security review bổ sung hoàn tất nếu cần.
- [ ] API/schema/migration/compatibility được xem xét khi liên quan.
- [ ] Approval của người có thẩm quyền được ghi nhận.

## Quy tắc
AI review không thay human approval. Push commit mới sau approval phải kích hoạt re-review theo branch policy. AI không được merge hoặc bỏ required checks trái policy. Tác giả không tự approve nếu policy yêu cầu independent review.

**Audit:** PR/repository, base/head SHA, findings, CI run, reviewer, approver, timestamp và merge commit.
