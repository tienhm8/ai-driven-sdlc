# G1 - Checklist phê duyệt yêu cầu (Requirement Approval Checklist)

## 1. Kiểm tra nghiệp vụ

- [ ] Mục tiêu nghiệp vụ rõ ràng.
- [ ] Phạm vi dự án đã được định nghĩa.
- [ ] Nội dung trong phạm vi và ngoài phạm vi đã được tài liệu hóa.
- [ ] Kỳ vọng của bên liên quan đã được xác nhận.
- [ ] Yêu cầu nghiệp vụ đã được review.

## 2. Kiểm tra yêu cầu

- [ ] FR, NFR và quy tắc nghiệp vụ áp dụng đã được tài liệu hóa.
- [ ] Hình thức đặc tả phù hợp (User Story, Use Case hoặc không áp dụng có lý do được chấp nhận) đã được xác định cho FR/NFR.
- [ ] Các yêu cầu cần nghiệm thu có Acceptance Criteria kiểm chứng được.
- [ ] Độ ưu tiên của yêu cầu đã được xác định.

## 3. Kiểm tra chất lượng

- [ ] Không còn mơ hồ quan trọng chưa được giải quyết.
- [ ] Không còn mâu thuẫn quan trọng chưa được giải quyết.
- [ ] Giả định đã được tài liệu hóa.
- [ ] Câu hỏi còn mở đã được tài liệu hóa.

## 4. Kiểm tra RTM trước G1

Dùng [template RTM Stage 01](../templates/requirement-traceability.md#5-độ-bao-phủ-và-điều-kiện-rtm-đạt-g1) để ghi kết quả từng chiều trên đúng phiên bản baseline trình duyệt. Không dùng một tỷ lệ tổng hợp thay cho kiểm tra này.

- [ ] Nguồn/mục tiêu → BRQ: mỗi BRQ có nguồn/mục tiêu hoặc căn cứ phát sinh.
- [ ] BRQ → FR và BRQ → NFR: kiểm tra riêng từng nhánh, có liên kết hợp lệ hoặc `N/A` được chấp nhận kèm lý do.
- [ ] FR/NFR → US/UC: có liên kết đặc tả phù hợp hoặc `N/A` được chấp nhận kèm lý do.
- [ ] US/UC → AC (hoặc FR/NFR → AC trực tiếp nếu không dùng US/UC): mọi yêu cầu cần nghiệm thu có AC rõ ràng, kiểm chứng được.
- [ ] BR trong phạm vi có ID riêng và liên kết với artifact chịu tác động; NFR có tiêu chí đo hoặc cách kiểm chứng đủ để xác định đạt/không đạt.
- [ ] Đã đối chiếu cả baseline và ma trận; không còn `Missing` ở liên kết bắt buộc, `Orphan` chưa xử lý, `N/A` chưa được chấp nhận hoặc `TBD` chặn G1. Phần không chặn đã có tác động, owner, hạn và quyết định xử lý.
- [ ] RTM `PASS` ở mọi chiều. Thiết kế, task, implementation, Test Case, kết quả kiểm thử và release không phải điều kiện G1.

## 5. Điều kiện phê duyệt

- [ ] Tất cả mục bắt buộc trong checklist đạt (PASS).
- [ ] Các vấn đề quan trọng đã được giải quyết.
- [ ] Product Owner đã review các artifact.
- [ ] Product Owner đã phê duyệt G1 một cách tường minh.

## 6. Ghi nhận kết quả kiểm tra và bàn giao

- Kết quả checklist: [PASS / FAIL / PENDING]
- Phiên bản RTM và tham chiếu kết quả kiểm tra từng chiều:
- Findings/gap còn lại: [Artifact/ID, owner, hạn]
- Tham chiếu checklist run/evidence:
- Hồ sơ review: `../outputs/12-requirement-review/requirement-review-record.md`
- Quyết định G1 chính thức được ghi duy nhất tại: `../outputs/12-requirement-review/G1-approval.md`

Checklist này xác nhận điều kiện sẵn sàng trình duyệt, không ghi quyết định thay Product Owner. AI KHÔNG được phê duyệt G1.
