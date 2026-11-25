# G7 – Critical Incident Approval

**Thời điểm:** Khi xử lý incident nghiêm trọng hoặc hành động có tác động lớn trong incident response.  
**Approver:** Incident Commander (IC); Security/Service Owner/Business Continuity Owner tham gia theo loại sự cố.

## AI hỗ trợ
Tổng hợp timeline, alerts, logs/metrics được phép truy cập; nêu giả thuyết/root cause kèm độ tin cậy; đề xuất containment, mitigation, recovery và communication draft.

## Hành động cần phê duyệt
- Production change có tác động lớn/khó đảo ngược.
- Cô lập hệ thống, tắt chức năng trọng yếu hoặc thay đổi quyền diện rộng.
- Restore dữ liệu, failover, chuyển vùng hoặc thao tác có nguy cơ mất dữ liệu.
- Communication bên ngoài theo thẩm quyền tổ chức.

## Điều kiện thông qua
- [ ] Severity, phạm vi ảnh hưởng và owner xác định.
- [ ] Phân biệt evidence với hypothesis.
- [ ] Phương án, rủi ro, tác động phụ và rollback/mitigation được trình bày.
- [ ] IC/người được ủy quyền phê duyệt hành động.
- [ ] Có executor, người giám sát và tiêu chí dừng.
- [ ] Timeline và quyết định được ghi nhận.

## Emergency action
Break-glass phải được tổ chức định nghĩa riêng: người kích hoạt, điều kiện, phạm vi, thời hạn, logging và hậu kiểm. Không suy diễn AI có quyền break-glass. Nếu policy cho phép hành động trước approval, phải có người chịu trách nhiệm và hậu kiểm theo thời hạn tổ chức quy định.

**Quyết định:** Áp dụng [policy chung về quyết định và trạng thái gate](gate-policy.md#reviewer-decision).

**Bằng chứng riêng của G7:** Incident ID, severity, timeline ứng phó, hành động, executor, kết quả và post-incident review.
