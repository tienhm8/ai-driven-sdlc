# Requirement Analysis - Đầu vào (Inputs)

## 1. Mục đích

Thư mục này chứa toàn bộ tài liệu đầu vào cần thiết cho giai đoạn Requirement Analysis.

AI PHẢI đọc và phân tích các tài liệu đầu vào liên quan trước khi tạo ra các artifact yêu cầu.

## 2. Nguồn đầu vào

Tài liệu đầu vào có thể bao gồm:

- Tài liệu yêu cầu nghiệp vụ.
- Mô tả quy trình nghiệp vụ.
- Đề xuất dự án.
- Ghi chú phỏng vấn bên liên quan.
- Tài liệu hệ thống hiện có.
- Đặc tả API hiện có.
- Tài liệu cơ sở dữ liệu hiện có.
- Yêu cầu pháp lý và tuân thủ quy định.
- Quy tắc và chính sách nghiệp vụ.

## 3. Quy tắc đầu vào

1. KHÔNG giả định rằng thông tin còn thiếu là đúng.
2. Nhận diện thông tin chưa đầy đủ hoặc mâu thuẫn.
3. Phân biệt sự kiện với giả định.
4. Ghi nhận nguồn của mỗi yêu cầu quan trọng.
5. KHÔNG bịa đặt yêu cầu nghiệp vụ.
6. Đặt câu hỏi làm rõ khi cần thiết.

## 4. Đầu vào bắt buộc

Cần có sẵn các thông tin sau:

- Mục tiêu nghiệp vụ.
- Phạm vi nghiệp vụ.
- Các bên liên quan chính.
- Bối cảnh hệ thống hiện có (nếu có).
- Các ràng buộc đã biết.

## 5. Đầu ra

Tài liệu đầu vào được dùng để tạo các artifact được định nghĩa trong `../outputs/`.

## 6. Trách nhiệm

- Người cung cấp tài liệu: Project Team / Business Analyst
- Người review đầu vào: Business Analyst / Product Owner
- Người thực hiện phân tích: AI Agent

## 7. Kiến trúc

```
inputs/
├── README.md                          # Hướng dẫn chuẩn bị đầu vào
├── input-document-register.md         # Sổ đăng ký tài liệu và trạng thái
├── business-context.md                # Bối cảnh, mục tiêu, phạm vi nghiệp vụ
├── stakeholder-information.md         # Bên liên quan và thẩm quyền quyết định
├── existing-system-context.md         # Hệ thống hiện có, tích hợp, hạn chế
└── constraints-and-assumptions.md     # Ràng buộc và giả định ban đầu
```

## 8. Vai trò từng file

| File | Vai trò |
|---|---|
| `README.md` | Quy định nguồn đầu vào, quy tắc xử lý và người chịu trách nhiệm. |
| `input-document-register.md` | Ghi nhận từng tài liệu đầu vào, phiên bản và trạng thái (Đã cung cấp, Chờ xử lý, Đã review...). Là điểm kiểm tra đầu tiên của Checklist 01. |
| `business-context.md` | Cung cấp bối cảnh nghiệp vụ, vấn đề, mục tiêu và tiêu chí thành công. Là nguồn gốc để tạo `business-requirements.md`. |
| `stakeholder-information.md` | Xác định ai là bên liên quan và ai có thẩm quyền phê duyệt, giải quyết xung đột, thay đổi phạm vi. Là căn cứ để xác định người phụ trách câu hỏi và G1. |
| `existing-system-context.md` | Mô tả hệ thống hiện có, công nghệ, tích hợp và yêu cầu di chuyển dữ liệu. Là căn cứ cho yêu cầu tích hợp và phi chức năng. |
| `constraints-and-assumptions.md` | Ghi nhận ràng buộc và giả định chưa được xác minh. Các giả định này được chuyển sang `outputs/assumptions-and-constraints.md`. |
