# Human Review Gate Policy

## Mục đích
Gate là điểm kiểm soát bắt buộc trước bước chuyển hoặc hành động được bảo vệ. Số gate không phải số thứ tự stage. Development chỉ có kiểm tra bàn giao; Monitoring thường kỳ không có gate chặn. AI không được tự chuyển qua gate nếu chưa có quyết định hợp lệ.

| Gate | Thời điểm | Approver | Điều kiện cốt lõi |
|---|---|---|---|
| G1 | Sau Requirement Analysis | Product Owner | Yêu cầu rõ, không mâu thuẫn; scope và Acceptance Criteria được xác nhận |
| G2 | Sau System Design | Solution Architect | Kiến trúc, bảo mật, dữ liệu và quyết định kỹ thuật được duyệt |
| G3 | Trước coding | Tech Lead | Task, scope, dependency và DoD rõ |
| [G4](G4-code-approval.md) | Trước merge | Reviewer, Senior Developer hoặc Tech Lead có thẩm quyền | Review hoàn tất, finding xử lý, CI đạt |
| G5 | Trước nghiệm thu | QA Lead **và** Product Owner (hai người riêng biệt) | Cùng xác nhận một release candidate: chất lượng kiểm thử và tiêu chí nghiệm thu nghiệp vụ |
| G6 | Trước production | Release Manager | Có release approval, kiểm tra an toàn và rollback plan |
| G7 | Khi xử lý incident nghiêm trọng | Incident Commander | Phương án ứng phó được đánh giá và phê duyệt |

## Quy tắc
1. Lưu approver, timestamp, artifact version, decision và evidence.
2. Chỉ người có vai trò và thẩm quyền phù hợp mới được ghi quyết định tại Gate bắt buộc; AI không được phê duyệt. Người được ghi nhận là tác giả của artifact đang được review không được ghi quyết định cho lần review đó, kể cả khi có vai trò approver phù hợp.
3. Từ chối phải có lý do; quay lại bước cần điều chỉnh.
4. Im lặng, timeout hoặc CI xanh không phải human approval.
5. Automated checks không thay thế phê duyệt nghiệp vụ/rủi ro.
6. Approval chỉ có hiệu lực với đúng phiên bản artifact.
7. Thay đổi trọng yếu sau approval làm mất hiệu lực approval liên quan và cần đánh giá lại.

## Lifecycle

### Reviewer decision

Người có thẩm quyền ghi quyết định cho đúng artifact và gói review đang mở:

| Quyết định | Ý nghĩa |
|---|---|
| `approved` | Đồng ý với nội dung đã review; phải kèm tham chiếu bằng chứng. |
| `rejected` | Không chấp nhận nội dung đã review. |
| `blocked` | Chưa thể quyết định đồng ý vì còn trở ngại, ví dụ thiếu đầu vào hoặc bằng chứng. |
| `changes_requested` | Yêu cầu chỉnh sửa trước khi chấp nhận. |

Mọi quyết định không phải `approved` đều phải ghi lý do.

### Trạng thái tổng hợp của gate

Platform dùng **quyết định hợp lệ mới nhất của từng approver** trong lần review đang mở:

| Trạng thái | Khi nào áp dụng |
|---|---|
| `blocked` | Có ít nhất một quyết định hiện hành là `rejected`, `blocked` hoặc `changes_requested`, kể cả khi người khác đã đồng ý hoặc có ngoại lệ. |
| `approved` | Không có quyết định chặn và đã đủ phê duyệt theo vai trò. G5 cần hai người riêng biệt thuộc hai vai trò bắt buộc. |
| `exception_authorized` | Không có quyết định chặn, chưa đủ phê duyệt nhưng có ngoại lệ hợp lệ, chưa hết hạn, và policy cho phép. |
| `awaiting_approval` | Không có quyết định chặn, nhưng chưa đủ phê duyệt hoặc ngoại lệ hợp lệ. |

`blocked` và `awaiting_approval` đều không cho qua gate. Trạng thái tổng hợp không thay thế checklist và tiêu chí riêng của từng gate. Với gate chặn hành động, `approved` hoặc `exception_authorized` là căn cứ để cấp quyền, không phải bằng chứng hành động đã chạy hay hoàn tất.

### Tiếp tục hoặc mở lại review

- Nếu review vẫn mở và artifact/gói review không đổi, người đã ghi quyết định chặn có thể cập nhật quyết định. Phê duyệt của người khác hoặc gửi lại cùng một gói không xóa quyết định chặn đó.
- Nếu digest của artifact hoặc gói review thay đổi, mở review mới; không chuyển phê duyệt hay ngoại lệ cũ sang. Lưu lịch sử để audit.
- Review đóng khi stage hoàn tất hoặc khi hành động được cấp quyền. Với G4/G6, chỉ mở review mới để thử lại sau khi có kết quả thất bại an toàn đã xác minh (không thay đổi đích, hoặc G6 đã rollback). Với G7, nếu quyền dựa trên ngoại lệ hết hạn trước khi ghi nhận bắt đầu, platform cho mở review mới; hết hạn sau khi đã ghi nhận bắt đầu không tự mở lại.
- Khi cần build lại từ cùng source, quay từ Deployment về QA để duyệt lại G5/G6. Nếu phải sửa source, quay từ QA hoặc Deployment về Development rồi qua G4/G5/G6 mới. Ghi người thực hiện và lý do; không quay lui khi quyền triển khai Production chưa có kết quả kết thúc đã xác minh.

## Approval record
Gate ID, project/workflow, artifact version/hash, ID và phiên bản/hash của gói review, requester, approver/role, quyết định từng người và lý do, trạng thái tổng hợp, conditions/exceptions, timestamp, evidence link và audit event ID. Với gate chặn hành động, ghi đích đã duyệt (ví dụ repo/PR/nhánh đích hoặc môi trường production). G4/G6 chỉ hoàn tất stage sau khi có kết quả đã xác minh; G5 cần bằng chứng build từ kết quả merge G4.

## Ngoại lệ
Chỉ người có thẩm quyền theo policy tổ chức được chấp nhận; phải ghi phạm vi, lý do, rủi ro, giảm thiểu, thời hạn và owner. Ngoại lệ chỉ áp dụng cho đúng gate, phiên bản và lần review đã ghi nhận; không ghi đè quyết định chặn hiện hành (kể cả `changes_requested`). Không miễn trừ yêu cầu pháp luật hoặc kiểm soát không thể miễn trừ, bao gồm quy tắc chặn merge khi còn finding Critical mở theo [G4](G4-code-approval.md), yêu cầu hai người phê duyệt G5 và quy tắc chặn G5 khi còn defect Critical mở trong phạm vi phát hành theo [G5](G5-qa-approval.md).
