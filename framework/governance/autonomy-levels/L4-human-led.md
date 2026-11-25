# L4 – Human-Led Decision

Theo [chính sách mức tự chủ](../ai-governance/ai-autonomy-levels.md), người có thẩm quyền quyết định và kích hoạt hành động L4. AI chỉ tư vấn, phân tích, mô phỏng, tổng hợp bằng chứng và nêu phương án.

**Ví dụ:** phê duyệt cuối cùng yêu cầu nghiệp vụ; quyết định bảo mật trọng yếu/residual risk nghiêm trọng; production operation rủi ro cao; migration dữ liệu quan trọng; incident nghiêm trọng.

AI có thể tóm tắt bằng chứng, đánh giá tác động và soạn checklist hoặc runbook nháp. Kể cả khi đã có lệnh hoặc phê duyệt, AI không được phê duyệt, cấp quyền, kích hoạt hay thực thi hành động L4.

Người có thẩm quyền có thể trực tiếp thực thi hoặc kích hoạt pipeline nếu policy cho phép. Trước khi chạy, pipeline phải có quyền thực thi riêng, giới hạn theo đúng hành động, phiên bản và đích đã duyệt. Nếu bất kỳ yếu tố nào không khớp, dừng và yêu cầu đánh giá lại. Ghi audit cho quyết định phê duyệt, lần kích hoạt và kết quả thực thi; áp dụng separation of duties khi policy yêu cầu.
