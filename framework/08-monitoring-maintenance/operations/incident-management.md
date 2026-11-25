# Incident Management

## Mục tiêu
Khôi phục dịch vụ an toàn, giảm tác động, duy trì thông tin nhất quán và học hỏi sau sự cố.

## Kích hoạt
Tạo incident khi gián đoạn/suy giảm đáng kể, vi phạm/nguy cơ vi phạm SLO, ảnh hưởng dữ liệu, security/privacy event hoặc cần phối hợp nhiều nhóm. Mức ưu tiên alert quyết định cách định tuyến và phản hồi ban đầu, không tự động trở thành incident severity.

## Incident severity

On-call đề xuất và IC hoặc người được phân công xác nhận mức độ theo ma trận đã duyệt của dự án; cập nhật khi có bằng chứng mới. Tham khảo các tiêu chí sau, không dùng thay cho ngưỡng, thời hạn phản hồi hay quy tắc G7 của dự án:

| Mức | Tác động đã xác minh |
|---|---|
| SEV-1 | Gián đoạn nghiêm trọng/phạm vi rộng hoặc rủi ro dữ liệu/bảo mật ở mức khẩn cấp |
| SEV-2 | Suy giảm lớn, ảnh hưởng nhiều người dùng hoặc chức năng trọng yếu |
| SEV-3 | Tác động giới hạn, có workaround hoặc không ảnh hưởng chức năng trọng yếu |
| SEV-4 | Tác động thấp nếu policy vẫn yêu cầu mở incident; tín hiệu chỉ cần theo dõi có thể không phải incident |

## Vai trò
- **IC:** điều phối, ưu tiên, quyết định/phê duyệt theo thẩm quyền.
- **Technical Lead:** điều tra và đề xuất mitigation.
- **SRE/Operations:** thực thi runbook được phép.
- **Communications Lead:** cập nhật stakeholder.
- **Scribe:** ghi timeline, quyết định, actions, evidence.

## Quy trình
1. Detect & declare: ghi thời điểm, nguồn alert, người báo.
2. Triage: service, environment, blast radius, user impact, data/security risk, recent changes.
3. Mobilize: chỉ định IC và vai trò; mở incident channel theo policy.
4. Mitigate: ưu tiên biện pháp giảm tác động, có thể đảo ngược; xin G7 approval khi cần.
5. Communicate: cập nhật impact, workaround và thời điểm cập nhật tiếp; không suy đoán nguyên nhân.
6. Recover: rollback/failover/restore theo runbook; kiểm tra SLI, health, data integrity.
7. Resolve & close: người được chỉ định theo incident policy xác nhận bằng chứng phục hồi và tiêu chí đóng. Nếu còn trạng thái degraded hoặc rủi ro cần chấp nhận, ghi quyết định của người có thẩm quyền theo risk policy. Thông báo stakeholder và lưu người duyệt đóng, thời điểm và follow-up.
8. Learn: tại bước đóng, xác định có cần RCA/postmortem theo policy dự án (ví dụ sự cố major/critical, mất dữ liệu hoặc vi phạm SLO đáng kể). Nếu cần, ghi owner và hạn theo policy; nếu không, ghi lý do. Theo dõi corrective actions với owner, hạn và tiêu chí xác minh. Phân tích hệ thống và quy trình, không đổ lỗi cá nhân.

## G7
Dùng [chính sách G7](../../governance/human-review-gates/G7-incident-approval.md) trước hành động ứng phó thuộc gate. Ghi phê duyệt cho đúng incident và phiên bản phương án; kiểm tra quyền executor riêng. Break-glass chỉ theo policy và phải hậu kiểm. Đóng sự cố và ký RCA là quyết định riêng, không dùng G7 thay cho các quyết định đó.

## Incident record
Dùng [mẫu Incident Report](../templates/incident-report.md) và [quy ước lưu đầu ra](../outputs/README.md).
