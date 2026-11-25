# Development Checklists

`checklists/` chứa các danh sách kiểm tra chất lượng cho giai đoạn 04 Development. AI dùng để tự kiểm tra trước khi báo cáo; Developer và Tech Lead dùng để đối chiếu bằng chứng và ghi kết quả kiểm tra; các checklist này không phải gate.

## Kiến trúc

```text
checklists/
├── development-readiness.md   # Xác minh G1/G2/G3 và DoR trước khi code
├── ai-safety-checklist.md     # Kiểm soát an toàn AI, áp dụng xuyên suốt
├── implementation-dod.md      # Definition of Done của từng task
└── handover-checklist.md      # Kiểm tra bàn giao sang 05 Code Review
```

Luồng sử dụng theo thời điểm trong vòng đời task:

| Thời điểm | Checklist | Kết quả |
|---|---|---|
| Trước khi bắt đầu code | `development-readiness.md` | Ready hoặc Blocked |
| Trong suốt quá trình code | `ai-safety-checklist.md` | Pass / Fail / N/A |
| Khi cho rằng task đã xong | `implementation-dod.md` | Done / Not Done |
| Khi chuyển sang Code Review | `handover-checklist.md` | Ready for Review / Blocked |

## Vai trò từng file

| File | Vai trò | Ai dùng | Khi nào |
|---|---|---|---|
| `development-readiness.md` | Xác minh bằng chứng G1/G2/G3 đúng phiên bản, phạm vi task và DoR; không phê duyệt lại. Thiếu hoặc mâu thuẫn thì `Blocked` theo checklist. | Developer kiểm tra; AI hỗ trợ; Tech Lead xác nhận kết quả kiểm tra | Trước khi code |
| `ai-safety-checklist.md` | Kiểm soát ủy quyền, bảo vệ dữ liệu, an toàn mã nguồn do AI sinh ra và truy vết hoạt động của AI. | AI; Developer | Xuyên suốt task |
| `implementation-dod.md` | Tiêu chí hoàn thành của một task: AC, test đã chạy, bảo mật, tài liệu, rủi ro còn lại. | Developer | Trước khi tự nhận task xong |
| `handover-checklist.md` | Đảm bảo gói bàn giao (PR, test evidence, tác động kỹ thuật, tài liệu) đủ để Reviewer làm việc. Không tự đánh dấu G4 approved. | Developer | Khi chuyển sang 05 |

## Quy tắc sử dụng

- Chỉ đánh dấu `[x]` khi đã kiểm tra thực tế; không đánh dấu theo suy đoán.
- Mục không áp dụng ghi rõ N/A kèm lý do.
- Kết quả Fail hoặc Blocked phải ghi blocker, owner và hạn xử lý.
- Checklist là công cụ kiểm tra, không thay thế việc review của con người tại G3/G4.
