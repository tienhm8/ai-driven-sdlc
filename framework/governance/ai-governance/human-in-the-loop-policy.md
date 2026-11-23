# Human-in-the-Loop Policy

## Mục tiêu
Bảo đảm con người tham gia đúng mức vào quyết định ảnh hưởng nghiệp vụ, bảo mật, dữ liệu, khách hàng và vận hành.

## Bắt buộc có con người
- Tại các Gate G1–G7.
- Với thay đổi logic nghiệp vụ, API, schema, phân quyền hoặc dữ liệu nhạy cảm.
- Khi rủi ro cao, tác động rộng, khó đảo ngược hoặc thiếu bằng chứng.
- Khi AI không chắc chắn, có xung đột yêu cầu hoặc vượt phạm vi.
- Khi chấp nhận rủi ro, xin ngoại lệ hoặc quyết định production/incident trọng yếu.

## Approval hợp lệ
Phải xác định approver và thẩm quyền; phạm vi; artifact/commit/config version; decision và điều kiện; timestamp và bằng chứng xác thực. Approval không gắn phiên bản cụ thể không đủ mở Gate.

## Giới hạn AI
AI có thể chuẩn bị tài liệu, kiểm tra điều kiện và nêu rủi ro; không tự approve output do mình tạo tại Gate bắt buộc, giả lập danh tính, coi im lặng là đồng ý hoặc tiếp tục khi chưa có approval hợp lệ.

## Từ chối/escalation
Khi bị từ chối, ghi lý do, cập nhật artifact và gửi review lại. Nếu bất đồng/không rõ thẩm quyền, chuyển owner/Tech Lead/Incident Commander. Không tự chọn phương án rủi ro hơn. Project phải chỉ định approver thay thế; không có approver thì trạng thái Blocked.
