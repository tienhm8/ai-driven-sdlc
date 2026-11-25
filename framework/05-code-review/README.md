# 05 – Code Review

## Mục tiêu
Đánh giá thay đổi mã nguồn so với yêu cầu, thiết kế và tiêu chuẩn kỹ thuật đã được phê duyệt; phát hiện lỗi logic, rủi ro bảo mật, vấn đề hiệu năng, khả năng bảo trì và thiếu sót kiểm thử trước khi merge.

## Vai trò
- **AI Code Reviewer:** phân tích diff, đối chiếu tài liệu đầu vào, chạy/đọc kết quả kiểm tra được cấp quyền, ghi nhận phát hiện và đề xuất sửa.
- **Developer/Author:** giải trình, cập nhật code và phản hồi từng nhận xét.
- **Senior Developer/Tech Lead/Reviewer:** xác nhận phát hiện, quyết định chấp nhận hoặc yêu cầu sửa, duyệt G4 (quyền merge là quyền riêng, không đồng nghĩa quyền duyệt G4).
- **Security/Domain reviewer:** tham gia khi thay đổi liên quan đến bảo mật hoặc nghiệp vụ nhạy cảm.

## Cấu trúc
- `workflow.md`: quy trình và trạng thái review.
- `ai-instructions.md`: chỉ dẫn thực thi cho AI.
- `human-review.md`: trách nhiệm và điểm phê duyệt của con người.
- `templates/`: biểu mẫu đầu vào/đầu ra dùng khi review.
- `checklists/`: danh sách kiểm tra theo từng khía cạnh.
- `inputs/`: quy ước tiếp nhận tài liệu từ các giai đoạn trước và PR.
- `outputs/`: kết quả review, báo cáo và bằng chứng.

## Nguyên tắc
1. Review theo diff và phạm vi PR; không suy đoán phần code không có bằng chứng.
2. Đối chiếu yêu cầu và thiết kế đã được phê duyệt; ghi rõ khi thiếu đầu vào.
3. Mỗi finding phải có vị trí, bằng chứng, tác động và hướng xử lý.
4. Không tự ý sửa code, merge PR, thay đổi cấu hình production hoặc phê duyệt G4 nếu không có quyền và phê duyệt rõ ràng.
5. Không đưa secret, token, dữ liệu cá nhân hoặc dữ liệu production vào báo cáo.
6. Kết quả kiểm tra tự động không thay thế review của con người.

## Mức tự chủ
- **L1:** format, lint và kiểm tra tự động đã cấu hình.
- **L2:** phân tích diff, đề xuất refactor nhỏ trong phạm vi được giao.
- **L3:** thay đổi logic nghiệp vụ, API, schema, phân quyền hoặc xử lý dữ liệu phải có người review và phê duyệt.
- **L4:** quyết định bảo mật/rủi ro cao, ngoại lệ policy thuộc con người.

Mức áp dụng theo từng hành động, không gán cho cả stage. L1/L2 không miễn G4.

## Human Review Gate
G4 – Trước khi merge code. Quy định chi tiết: [G4-code-approval.md](../governance/human-review-gates/G4-code-approval.md); thao tác: [merge-approval-checklist.md](checklists/merge-approval-checklist.md).

Luồng: **G4 Approved → merge theo policy → xác minh merge (merge commit SHA + bằng chứng) → bàn giao QA.** Stage chưa hoàn tất nếu PR chưa merge.

## Bắt đầu nhanh
1. Thu thập đầu vào theo `inputs/README.md`.
2. Thực hiện quy trình trong `workflow.md`.
3. Ghi nhận kết quả theo `templates/review-report.md`.
4. Dùng checklist phù hợp trong `checklists/`.
5. Hoàn tất xác nhận G4 theo `human-review.md`.
