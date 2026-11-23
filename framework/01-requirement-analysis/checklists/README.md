# Danh sách kiểm tra Requirement Analysis (Checklists)

## Mục đích

Thư mục này chứa các checklist kiểm soát chất lượng cho giai đoạn Requirement Analysis.

## Thời điểm thực hiện checklist

| Checklist | Thời điểm thực hiện |
|---|---|
| 01 Tính đầy đủ của đầu vào (Input Completeness) | Trước khi phân tích |
| 02 Phân tích yêu cầu (Requirement Analysis) | Trong quá trình phân tích |
| 03 Chất lượng yêu cầu (Requirement Quality) | Sau khi tạo yêu cầu |
| 04 Mơ hồ và mâu thuẫn (Ambiguity and Conflict) | Sau khi tạo yêu cầu |
| 05 Yêu cầu phi chức năng (Non-Functional Requirements) | Trước khi hoàn tất |
| 06 Phê duyệt G1 (G1 Approval) | Trước khi chuyển sang System Design |

## Quy tắc thực hiện

- AI thực hiện các mục kiểm tra áp dụng được.
- Mỗi mục PHẢI có trạng thái Đạt, Không đạt hoặc Không áp dụng.
- Các mục không đạt PHẢI được ghi nhận.
- Các mục Không áp dụng PHẢI có lý do đi kèm.
- Cần có review của con người theo chính sách mức độ tự chủ.
- AI KHÔNG ĐƯỢC phê duyệt G1.

## Định nghĩa trạng thái

- PASS (Đạt): Đáp ứng tiêu chí.
- FAIL (Không đạt): Không đáp ứng tiêu chí.
- N/A (Không áp dụng): Không liên quan.
- PENDING (Chờ kiểm tra): Chưa được kiểm tra.

## Kiến trúc

```
checklists/
├── README.md                                   # Hướng dẫn thực hiện và trạng thái
├── 01-input-completeness-checklist.md          # Chạy trước khi phân tích
├── 02-requirement-analysis-checklist.md        # Chạy trong khi phân tích
├── 03-requirement-quality-checklist.md         # Chạy sau khi tạo yêu cầu
├── 04-ambiguity-and-conflict-checklist.md      # Chạy sau khi tạo yêu cầu
├── 05-non-functional-requirement-checklist.md  # Chạy trước khi hoàn tất
└── 06-G1-approval-checklist.md                 # Điều kiện trước khi chuyển System Design
```

## Vai trò từng file

| File | Vai trò | Thời điểm | Đầu ra kiểm tra |
|---|---|---|---|
| `README.md` | Quy định cách thực hiện checklist, trạng thái PASS / FAIL / N/A / PENDING và quyền của AI. | Đọc trước khi dùng | — |
| `01-input-completeness-checklist.md` | Xác nhận đầu vào đủ thông tin cơ bản (mục tiêu, phạm vi, bên liên quan, ràng buộc). | Trước phân tích | `inputs/` |
| `02-requirement-analysis-checklist.md` | Xác nhận quá trình phân tích đã bao phủ chức năng, phi chức năng, quy tắc, luồng và phụ thuộc. | Trong phân tích | `outputs/` |
| `03-requirement-quality-checklist.md` | Đánh giá từng yêu cầu theo 10 thuộc tính chất lượng: rõ ràng, đầy đủ, nhất quán, kiểm thử được, khả thi, v.v. | Sau khi tạo yêu cầu | `outputs/` |
| `04-ambiguity-and-conflict-checklist.md` | Tìm thuật ngữ mơ hồ, mâu thuẫn, quy tắc còn thiếu và giả định chưa xác minh. Mọi vấn đề phải vào `open-questions.md`. | Sau khi tạo yêu cầu | `outputs/open-questions.md` |
| `05-non-functional-requirement-checklist.md` | Đảm bảo các hạng mục NFR được xem xét và có tiêu chí đo lường. Không tự đặt con số khi chưa có. | Trước khi hoàn tất | `outputs/non-functional-requirements.md` |
| `06-G1-approval-checklist.md` | Tổng hợp điều kiện để Product Owner xét duyệt G1. AI không được tích điều kiện phê duyệt thay Product Owner. | Trước khi chuyển System Design | `outputs/G1-approval-record.md` |
