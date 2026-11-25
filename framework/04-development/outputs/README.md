# Development Outputs

`outputs/` lưu artifact được tạo/cập nhật trong Development để bàn giao cho Code Review và downstream stages. Đây không phải nơi lưu source code thay Git repository.

## Kiến trúc

```text
outputs/
├── README.md                              # Quy định đầu ra và cách lưu theo task
├── implementation-summary-template.md     # Tóm tắt triển khai và ánh xạ AC
├── test-evidence-template.md              # Bằng chứng thực thi test và kiểm tra
└── development-handover-template.md       # Gói bàn giao sang 05 Code Review
```

Lưu theo task/release, ví dụ `outputs/TASK-123/`, gồm bản instance của các template trên cùng với tài liệu kỹ thuật được cập nhật.

Luồng bàn giao: `implementation-summary` và `test-evidence` là đầu vào của `development-handover`; cả ba cùng được kiểm tra trong [handover checklist](../checklists/handover-checklist.md), nơi ghi kết quả PR Readiness Check trước khi chuyển sang 05.

## Vai trò từng file

| File | Vai trò | Consumer |
|---|---|---|
| `README.md` | Quy định artifact nào cần có, cách đặt tên/lưu theo task, yêu cầu ghi ID/commit/date/author và nguyên tắc ghi Pass/Fail/Not run. | Developer, AI |
| `implementation-summary-template.md` | Mô tả thay đổi đã làm, ánh xạ từng AC với bằng chứng, tác động API/DB/config/bảo mật, phần AI hỗ trợ và known issues. | 05 Code Review |
| `test-evidence-template.md` | Ghi lệnh chính xác, môi trường, phiên bản và kết quả của từng loại test/check. Phân biệt rõ Pass, Fail và Not run; ghi lý do cho mọi kiểm tra bị loại trừ. | 05 Code Review, 06 Testing & QA |
| `development-handover-template.md` | Gói bàn giao chính: link PR, phạm vi đã giao, trọng tâm review, rủi ro và câu hỏi mở, Base SHA / Head SHA và liên kết đến kết quả DoD/readiness. Không đánh dấu G4 approved. | 05 Code Review |

Tài liệu kỹ thuật cập nhật (module/API/config docs) được lập theo `templates/code-documentation.md` và dùng bởi 05, 06, 07, 08.

## Quy tắc sử dụng

- Chỉ ghi Pass khi có evidence thực thi. Không suy ra test pass từ việc code biên dịch hoặc từ việc AI đọc code.
- Không lưu secret hoặc PII không cần thiết trong bất kỳ artifact nào.
- Mỗi artifact ghi rõ ID/version, commit SHA, ngày, tác giả và link nguồn để truy vết.
