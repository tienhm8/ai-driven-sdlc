# Merge Approval Checklist – G4 & Merge Verification

## G4 (trước khi merge)
- [ ] Đúng PR, repository và head commit đã được review.
- [ ] Requirement, design và task liên quan có thể truy vết.
- [ ] Không còn Critical/High finding chưa xử lý.
- [ ] Medium finding còn lại có quyết định xử lý/accepted risk đúng policy.
- [ ] Build, test và CI checks bắt buộc đạt.
- [ ] Security review hoàn tất nếu thuộc phạm vi bắt buộc.
- [ ] Migration, compatibility và rollback được xem xét khi liên quan.
- [ ] Có approval của reviewer con người đủ thẩm quyền.
- [ ] Lưu approver, timestamp, commit SHA, report version và CI evidence.
- [ ] Không có AI tự phê duyệt Gate G4.

## Sau G4 (trước khi bàn giao QA)
- [ ] PR đã merge bởi người/quy trình có quyền theo branch policy.
- [ ] Ghi merge commit SHA và link bằng chứng merge.
- [ ] Build/CI sau merge (nếu policy yêu cầu) truy vết về merge commit SHA.
- [ ] Rủi ro còn lại được ghi để bàn giao QA.
