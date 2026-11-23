# Requirement Analysis - Đầu ra (Outputs)

## 1. Mục đích

Thư mục này chứa toàn bộ sản phẩm được tạo ra trong giai đoạn Requirement Analysis.

## 2. Sản phẩm dự kiến

| Artifact | Mô tả |
|---|---|
| requirement-analysis-report.md | Báo cáo tổng hợp phân tích |
| business-requirements.md | Tài liệu yêu cầu nghiệp vụ (BRD) |
| functional-requirements.md | Yêu cầu chức năng |
| non-functional-requirements.md | Yêu cầu phi chức năng |
| user-stories.md | Danh sách User Story |
| acceptance-criteria.md | Tiêu chí nghiệm thu |
| use-cases.md | Các trường hợp sử dụng |
| open-questions.md | Câu hỏi chưa được giải đáp |
| assumptions-and-constraints.md | Giả định và ràng buộc |
| requirement-traceability-matrix.md | Ma trận truy vết yêu cầu |
| G1-approval-record.md | Hồ sơ phê duyệt của con người |

## 3. Quy tắc đầu ra

1. Tuân theo template tương ứng.
2. Gán ID duy nhất cho mỗi yêu cầu.
3. Tham chiếu đến nguồn đầu vào.
4. KHÔNG bịa đặt yêu cầu chưa được xác nhận.
5. Ghi nhận các câu hỏi chưa được giải quyết.
6. Duy trì tính nhất quán giữa các artifact.
7. Cập nhật phiên bản và lịch sử thay đổi.
8. Phân biệt rõ thông tin do AI tạo ra với thông tin đã được con người phê duyệt.

## 4. Trạng thái phê duyệt

Các artifact sử dụng một trong các trạng thái sau:

- DRAFT (Nháp)
- UNDER_REVIEW (Đang review)
- APPROVED (Đã phê duyệt)
- REJECTED (Bị từ chối)
- SUPERSEDED (Đã được thay thế)

## 5. Quy tắc quan trọng

- Đầu ra do AI tạo ra ban đầu ở trạng thái DRAFT.
- Chỉ người có thẩm quyền mới được phê duyệt G1.
- Việc phê duyệt PHẢI được ghi nhận.
- Mọi thay đổi sau khi phê duyệt PHẢI có thể truy vết.
- Các artifact đã được phê duyệt trở thành đầu vào cho giai đoạn System Design.

## 6. Kiến trúc

```
outputs/
├── README.md                              # Quy tắc đầu ra và trạng thái phê duyệt
├── requirement-analysis-report.md         # Nhóm tổng quan: báo cáo phân tích
├── business-requirements.md               # Tài liệu yêu cầu nghiệp vụ (BRD)
├── functional-requirements.md             # Nhóm yêu cầu: chức năng
├── non-functional-requirements.md         # Nhóm yêu cầu: phi chức năng
├── user-stories.md                        # Nhóm mô tả: User Story
├── acceptance-criteria.md                 # Nhóm mô tả: tiêu chí nghiệm thu
├── use-cases.md                           # Nhóm mô tả: Use Case
├── open-questions.md                      # Nhóm làm rõ: câu hỏi còn mở
├── assumptions-and-constraints.md         # Nhóm làm rõ: giả định và ràng buộc
├── requirement-traceability-matrix.md     # Nhóm truy vết
└── G1-approval-record.md                  # Nhóm phê duyệt: hồ sơ G1
```

## 7. Vai trò từng file

| File | Vai trò | Người/AI tạo | Trạng thái ban đầu |
|---|---|---|---|
| `README.md` | Quy định cách tạo đầu ra, ID, trạng thái và quyền phê duyệt. | Framework | — |
| `requirement-analysis-report.md` | Tổng hợp kết quả phân tích, số lượng yêu cầu, rủi ro và mức sẵn sàng G1. Là tài liệu đầu tiên người review đọc. | AI | DRAFT |
| `business-requirements.md` | Tài liệu yêu cầu nghiệp vụ (BRD): ghi mục tiêu, nguồn, các yêu cầu nghiệp vụ (BRQ) và quy tắc nghiệp vụ (BR) liên quan. | AI | DRAFT |
| `functional-requirements.md` | Mô tả chi tiết yêu cầu chức năng (FR), actor, luồng và liên kết với BRQ. | AI | DRAFT |
| `non-functional-requirements.md` | Mô tả yêu cầu phi chức năng (NFR) với phương pháp đo và mục tiêu đã được xác nhận. | AI | DRAFT |
| `user-stories.md` | Chuyển FR/BRQ thành User Story theo định dạng As a / I want / So that. | AI | DRAFT |
| `acceptance-criteria.md` | Định nghĩa điều kiện nghiệm thu (Given / When / Then) cho từng User Story. | AI | DRAFT |
| `use-cases.md` | Mô tả luồng chính, luồng thay thế, luồng ngoại lệ và hậu điều kiện. | AI | DRAFT |
| `open-questions.md` | Sổ câu hỏi chưa được giải đáp, người phụ trách và tác động nếu chưa xử lý. Câu hỏi quan trọng chưa đóng sẽ chặn G1. | AI đề xuất, người xác nhận | OPEN |
| `assumptions-and-constraints.md` | Tổng hợp giả định (chưa / đã xác nhận), ràng buộc và rủi ro. | AI | Chưa xác nhận |
| `requirement-traceability-matrix.md` | Liên kết BRQ → FR → US → AC → UC → Test Case để phát hiện thiếu sót. | AI | — |
| `G1-approval-record.md` | Hồ sơ phê duyệt G1: artifact đã gửi, kết quả checklist, vấn đề còn mở và quyết định của Product Owner. | AI chuẩn bị; Product Owner quyết định | PENDING |
