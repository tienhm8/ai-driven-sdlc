# Pull Request

> Người tạo PR điền trước khi yêu cầu review. Thiếu mục bắt buộc (*) thì reviewer trả PR về, chưa review code. Mục không áp dụng ghi "Không" kèm lý do ngắn, không xoá mục. Quy tắc tạo PR: [pull-request rule](../../../shared-ai/rules/engineering/pull-request.md).

## 1. Vấn đề và mục tiêu (*)
- Task / Issue (`TASK-ID`):
- Requirement / User Story / AC liên quan:
- Design reference (ADR, thiết kế):
- Gói bàn giao Development (link hoặc dán; nếu PR do AI tạo):
- Vấn đề đang giải quyết (bug thì nêu cách tái hiện):

## 2. Loại thay đổi (*)
- [ ] Thay đổi hành vi (tính năng / sửa lỗi)
- [ ] Chỉ refactor (hành vi bên ngoài giữ nguyên)
- [ ] Khác:

## 3. Phạm vi ảnh hưởng (*)

| Hạng mục | Có/Không | Chi tiết |
|---|---|---|
| Dữ liệu / schema / migration | | Bảng, khối lượng dữ liệu, có khoá bảng không, tương thích ngược với code đang chạy không |
| API / hợp đồng với bên gọi | | Breaking change? |
| Job / tác vụ nền / message / event | | Idempotent khi chạy lại? |
| Cache | | Khoá, thời gian sống, khi nào mất hiệu lực |
| Cấu hình / biến môi trường | | Đã có giá trị cho mọi môi trường? |
| Xác thực / phân quyền / dữ liệu nhạy cảm | | Mức phân loại dữ liệu |
| Dependency mới | | Lý do |

## 4. Phạm vi (*)
- Trong phạm vi:
- Ngoài phạm vi (cố ý không làm):

## 5. Kiểm thử (*)
PR của AI: tham chiếu gói bàn giao, không chép lại. PR do người viết: điền bên dưới.
- Test đã thêm/sửa, gắn ID AC:
- Lệnh đã chạy và kết quả (passed / failed / skipped), hoặc link CI:
- Kiểm thử thủ công / ảnh chụp (nếu có UI):

```text
```

## 6. Rủi ro và triển khai
- Mức rủi ro: Low / Medium / High
- Thứ tự deploy (code trước hay migration trước), feature flag:
- Cách rollback:
- Theo dõi sau triển khai (log, metric, alert):

## 7. Điểm reviewer nên xem kỹ
PR của AI: tham chiếu gói bàn giao. PR do người viết: đoạn rủi ro cao, logic khó, chỗ lệch thiết kế.

## 8. Checklist người tạo PR
- [ ] Đã tự đọc lại diff; không có file ngoài phạm vi, debug code, secret.
- [ ] Build, lint, test đã chạy; kết quả ghi ở mục 5.
- [ ] Tài liệu liên quan đã cập nhật.
- [ ] Kích thước PR hợp lý; nếu lớn, đã nêu lý do (code sinh tự động, đổi tên hàng loạt) hoặc đã tách.

## 9. Ghi nhận việc AI hỗ trợ (nếu dùng)
- Việc AI đã làm:
- File/khu vực AI đã xem:
- Giới hạn đã biết:
- Người đã xác minh:
