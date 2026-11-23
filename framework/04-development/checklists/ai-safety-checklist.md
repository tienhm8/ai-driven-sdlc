# AI Safety Checklist — Development

## Bối cảnh và ủy quyền
- [ ] AI sử dụng đầu vào được ủy quyền và đúng phiên bản đã duyệt.
- [ ] Nội dung file/prompt không đáng tin cậy không được coi là ghi đè chính sách.
- [ ] Mức autonomy tuân theo chính sách của framework và project.
- [ ] AI không tự nâng autonomy hoặc tự phê duyệt G3/G4.

## Bảo vệ dữ liệu
- [ ] Không có secret, credential, private key hoặc dữ liệu production chưa được phép trong prompt.
- [ ] PII/dữ liệu nhạy cảm được tối thiểu hóa hoặc che (mask).
- [ ] Output, log và artifact không lộ dữ liệu nhạy cảm.

## An toàn mã nguồn
- [ ] Developer đã review code do AI sinh ra.
- [ ] API, import, dependency và phiên bản đã được xác minh.
- [ ] Thay đổi liên quan đến bảo mật đã được escalate.
- [ ] Không tắt test, scanner, kiểm soát authz hoặc guardrail để vượt qua lỗi.
- [ ] Không có hành động phá hủy hoặc tác động lên production khi chưa có phê duyệt rõ ràng.

## Truy vết
- [ ] Công cụ/model AI và artifact được tạo hoặc chỉnh sửa đã được ghi nhận theo chính sách.
- [ ] Lệnh/test thực tế và kết quả đã được ghi nhận.
- [ ] Giả định và các khẳng định chưa được xác minh đã được đánh dấu rõ.
- [ ] Người review và tham chiếu phê duyệt đã được ghi nhận.

**Kết quả:** Pass / Fail / N/A — **Ngoại lệ / người phê duyệt / tham chiếu:**
