# G5 – Testing & QA Approval

**Thời điểm:** Sau Testing & QA, trước nghiệm thu/release handoff.  
**Approvers (hai người riêng biệt):** QA Lead xác nhận chất lượng kiểm thử; Product Owner xác nhận đáp ứng nghiệp vụ/nghiệm thu. Cả hai duyệt cùng một phiên bản release candidate.

## AI chuẩn bị
Test plan/cases, execution results, coverage, defect list, regression evidence, NFR test results và known limitations.

## Điều kiện thông qua

Dùng QA Sign-off Checklist tại `framework/06-testing-qa/checklists/qa-signoff-checklist.md` trong repo framework để kiểm tra evidence. Hai người phê duyệt cùng artifact SHA-256 (`artifact_sha256`) và cùng gói review có tham chiếu và SHA-256 (`review_context_sha256`). Provenance đã xác minh phải liên kết artifact với kết quả merge G4 đã ghi nhận. Chốt và băm gói evidence trước khi trình; lưu quyết định/biên bản phê duyệt tham chiếu gói đã chốt, không sửa gói sau khi duyệt.

Ngưỡng defect và coverage phải được quy định trước trong test plan/release policy, phù hợp với loại dự án và mức rủi ro; không được nới lỏng điều kiện chặn của G5. Không che giấu defect nghiêm trọng hoặc tự hạ severity để thông qua gate.

- **Critical còn mở trong phạm vi phát hành luôn chặn G5:** QA khuyến nghị No-Go; không chấp nhận ngoại lệ. Tối thiểu, xếp Critical khi có bằng chứng về tác động nghiêm trọng như mất/hỏng dữ liệu không thể khôi phục, lỗ hổng có thể bị khai thác gây tác động nghiêm trọng, vi phạm nghĩa vụ pháp lý bắt buộc, hoặc luồng nghiệp vụ cốt lõi không thể sử dụng. Dự án có thể bổ sung tiêu chí Critical theo mức rủi ro, không được hạ chuẩn này.
- **High còn mở chặn theo mặc định:** chỉ được xem xét nếu release policy của dự án cho phép, người có thẩm quyền do policy chỉ định chấp nhận bằng văn bản và không vi phạm kiểm soát không thể miễn trừ. Các lỗi mức thấp hơn vẫn phải có disposition và đáp ứng ngưỡng release policy.
- Ngoại lệ/risk acceptance ghi đúng phạm vi, lý do, tác động, biện pháp giảm thiểu, owner, thời hạn và tham chiếu quyết định theo [gate policy](gate-policy.md). Ngoại lệ không thay một trong hai phê duyệt hoặc ghi đè quyết định Reject/Blocked hiện hành.

### Cách gỡ chặn đối với Critical

1. **Sửa lỗi:** nếu đổi source, quay lại 04 → G4 mới → build mới → QA retest/regression → G5 mới.
2. **Loại phần bị ảnh hưởng khỏi phạm vi phát hành:** lập yêu cầu thay đổi (change request) để Product Owner phê duyệt phạm vi phát hành mới trước khi trình G5. Nếu chỉ thu hẹp phạm vi phát hành, giữ nguyên baseline kế hoạch task đã duyệt tại G3; không sửa baseline để phản ánh quyết định không phát hành. Nếu cần thêm hoặc sửa công việc triển khai (ví dụ sửa code để vô hiệu hóa tính năng), dùng `return_to_development` và đi qua G4 mới → build mới → QA retest/regression → G5 mới. Gói review G5 ghi tham chiếu yêu cầu thay đổi, quyết định của PO và phiên bản phạm vi phát hành đã duyệt; nếu có thay đổi triển khai, ghi thêm tham chiếu G4 và bằng chứng kiểm thử mới. QA xác minh phần bị lỗi thực sự không thể sử dụng hoặc kích hoạt trong phạm vi đã duyệt, kể cả qua các đường truy cập khác. Nếu dùng feature flag, QA retest/regression trên đúng artifact và cấu hình flag dự kiến cho production; ghi và ràng buộc cấu hình đó trong gói review, bàn giao cho G6 để đối chiếu trước rollout. Không bật lại phần bị ảnh hưởng hoặc mở rộng scope nếu chưa quay lại QA và lấy G5 mới trước G6, kể cả khi digest không đổi. Defect vẫn mở và được ghi trong known issues.
3. **Phân loại lại qua triage:** chỉ khi bằng chứng mới cho thấy tác động thực tế không còn đáp ứng tiêu chí Critical trên ứng viên phát hành. Workaround không tự gỡ chặn. Ghi severity cũ/mới, lý do, bằng chứng và người quyết định theo policy; QA Lead và PO phải thấy lịch sử triage trong gói review, không cá nhân nào tự hạ severity để qua gate.

## Khuyến nghị QA và quyết định gate

Khuyến nghị QA: **Go / No-Go / Conditional Go / Blocked**. Conditional Go ghi điều kiện, owner, thời hạn và tham chiếu risk acceptance nếu áp dụng. Nếu điều kiện bắt buộc còn thiếu hoặc chưa có risk acceptance cần thiết, G5 chưa được Approve.

**Quyết định G5:** Approve / Reject / Blocked. Chỉ thông qua khi QA Lead và Product Owner (hai người riêng biệt) đều Approve trên cùng artifact và gói review. CI xanh, Conditional Go hoặc risk acceptance không phải phê duyệt G5. G5 chỉ duyệt release candidate; G6 mới cấp quyền triển khai production.

**Audit:** Lưu merge reference, artifact URI/version và SHA-256, provenance, gói review và SHA-256, TESTRUN/environment, report, defect disposition, từng approver/decision/timestamp và tham chiếu audit. Đổi artifact digest thì kiểm thử lại và duyệt G5 mới trước G6.
