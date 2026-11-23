# AI Usage Policy

## Phạm vi
Áp dụng cho nhân sự, nhà thầu, AI agent và công cụ AI trong các hoạt động thuộc framework.

## Được phép
- Phân tích yêu cầu, tạo nháp tài liệu/thiết kế.
- Sinh code/test trong task và quyền được cấp.
- Review, phân tích log/metrics và đề xuất khắc phục.
- Tự động hóa kiểm tra lặp lại đã được phê duyệt.

## Có điều kiện
Cần review/approval phù hợp khi AI thay đổi logic nghiệp vụ, API, schema, authorization; xử lý dữ liệu cá nhân/nhạy cảm; thay đổi infrastructure, pipeline, IAM, security config; hoặc thực hiện hành động ghi/xóa/gửi ra ngoài/tác động hệ thống dùng chung.

## Không được phép
- Né kiểm soát, giả mạo approval hoặc che giấu hành động.
- Cung cấp secret/dữ liệu vượt quyền cho AI.
- Để AI tự phê duyệt Gate bắt buộc hoặc tự merge/deploy trái policy.
- Dùng output chưa kiểm chứng như sự thật; bịa nguồn, test result, benchmark hay approval.
- Đưa dữ liệu tổ chức vào dịch vụ chưa được phê duyệt.

## Minh bạch và trách nhiệm
Ghi nhận việc sử dụng AI khi policy yêu cầu. Người áp dụng phải kiểm tra tính đúng đắn, license, bảo mật và phù hợp trước khi sử dụng. Phân biệt đề xuất AI với quyết định đã được người có thẩm quyền thông qua.
