# Audit Policy

## Mục tiêu
Bảo đảm hoạt động AI và quyết định governance có thể truy vết, kiểm tra và điều tra.

## Phạm vi
Agent/model/tool identity và quyền; task/action có tác động; artifact/version/hash; human review, Gate approval, exception/risk acceptance; CI/test/security evidence; deployment và incident events.

## Tài liệu
- `audit-trail-standard.md`: event, metadata và integrity.
- `retention-and-access.md`: quyền truy cập, lưu trữ, bảo vệ và disposition.

## Nguyên tắc
Thu thập tối thiểu nhưng đủ chứng minh ai làm gì, khi nào, trên đối tượng nào và kết quả. Không ghi raw secret/token hoặc PII không cần thiết. Log có kiểm soát truy cập và chống sửa/xóa phù hợp rủi ro. Retention phải được cấu hình theo luật, hợp đồng và policy; framework không tự đặt thời hạn pháp lý. Audit log không thay thế approval chính thức.
