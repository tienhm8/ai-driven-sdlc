# Human Review Gate Policy

## Mục đích
Gate là điểm kiểm soát bắt buộc trước bước chuyển hoặc hành động được bảo vệ. Số gate không phải số thứ tự stage. Development chỉ có kiểm tra bàn giao; Monitoring thường kỳ không có gate chặn. AI không được tự chuyển qua gate nếu chưa có quyết định hợp lệ.

| Gate | Thời điểm | Approver | Điều kiện cốt lõi |
|---|---|---|---|
| G1 | Sau Requirement Analysis | Product Owner | Yêu cầu rõ, không mâu thuẫn; scope và Acceptance Criteria được xác nhận |
| G2 | Sau System Design | Solution Architect | Kiến trúc, bảo mật, dữ liệu và quyết định kỹ thuật được duyệt |
| G3 | Trước coding | Tech Lead | Task, scope, dependency và DoD rõ |
| G4 | Trước merge | Reviewer/Tech Lead | Review hoàn tất, finding xử lý, CI đạt |
| G5 | Trước nghiệm thu | QA Lead **và** Product Owner (hai người riêng biệt) | Cùng xác nhận một release candidate: chất lượng kiểm thử và tiêu chí nghiệm thu nghiệp vụ |
| G6 | Trước production | Release Manager | Có release approval, kiểm tra an toàn và rollback plan |
| G7 | Khi xử lý incident nghiêm trọng | Incident Commander | Phương án ứng phó được đánh giá và phê duyệt |

## Quy tắc
1. Lưu approver, timestamp, artifact version, decision và evidence.
2. AI không phê duyệt công việc do chính AI tạo tại Gate bắt buộc.
3. Từ chối phải có lý do; quay lại bước cần điều chỉnh.
4. Im lặng, timeout hoặc CI xanh không phải human approval.
5. Automated checks không thay thế phê duyệt nghiệp vụ/rủi ro.
6. Approval chỉ có hiệu lực với đúng phiên bản artifact.
7. Thay đổi trọng yếu sau approval làm mất hiệu lực approval liên quan và cần đánh giá lại.

## Lifecycle
`Pending → In Review → Approved | Rejected | Blocked | Changes Requested`. Approved chỉ khi đủ điều kiện và approval hợp lệ. Thiếu đầu vào/quyền/approver/evidence thì Blocked. Changes Requested yêu cầu chỉnh sửa và chặn chuyển tiếp cho đến khi có quyết định hợp lệ.

## Approval record
Gate ID, project/workflow, artifact version/hash, phiên bản gói review, requester, approver/role, decision/reason, conditions/exceptions, timestamp, evidence link và audit event ID. Với gate chặn hành động, ghi đích đã duyệt (ví dụ repo/PR/nhánh đích hoặc môi trường production). G4/G6 chỉ hoàn tất stage sau khi có kết quả đã xác minh; G5 cần bằng chứng build từ kết quả merge G4.

## Ngoại lệ
Chỉ người có thẩm quyền theo policy tổ chức được chấp nhận; phải ghi phạm vi, lý do, rủi ro, giảm thiểu, thời hạn và owner. Ngoại lệ chỉ áp dụng cho đúng gate, phiên bản và lần review đã ghi nhận; không xóa quyết định Reject/Blocked hiện hành. Không miễn trừ yêu cầu pháp luật hoặc kiểm soát không thể miễn trừ, bao gồm yêu cầu hai người phê duyệt G5.
