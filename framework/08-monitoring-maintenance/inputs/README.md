# Inputs – Monitoring & Maintenance

Giai đoạn 08 nhận tham chiếu từ SDLC 01–07 và dữ liệu runtime. Không cần sao chép toàn bộ tài liệu/source code; ưu tiên liên kết có version/commit, owner và timestamp.

## Nguồn đầu vào

| Nguồn | Bằng chứng cần tham chiếu | Bắt buộc / khi áp dụng |
|---|---|---|
| [07 – Deployment](../../07-deployment/workflow.md) | Deployment Record xác minh Production thành công; phiên bản đang chạy, môi trường, dashboard/alert, runbook (kèm rollback), on-call/escalation, rủi ro còn lại, người tiếp nhận và thời điểm | Bắt buộc khi bàn giao release vào 08 |
| Runtime | Dashboard SLI/SLO hoặc tiêu chí vận hành, nguồn metrics/logs/traces/alerts theo phạm vi giám sát; ticket và khoảng thời gian truy vấn khi điều tra | Bắt buộc có nguồn quan sát vận hành; chi tiết theo service và work item |
| 01 – Requirement Analysis | NFR, luồng nghiệp vụ trọng yếu và tiêu chí tác động | Khi xác định baseline/SLO hoặc đánh giá impact |
| 02 – System Design | Kiến trúc, ADR, dependency map, thiết kế backup/DR và phân loại dữ liệu | Khi thiết lập hoặc thay đổi phạm vi giám sát, ứng phó hay DR |
| 03 – Task Planning | Backlog, owner và cam kết còn mở | Khi chuyển tiếp follow-up hoặc nợ kỹ thuật |
| 04 – Development | Commit/build reference và thay đổi instrumentation, cấu hình hoặc dependency | Khi truy vết change hoặc điều tra incident |
| 05 – Code Review | Review/G4 record và rủi ro kỹ thuật được ghi nhận | Khi cần truy vết quyết định hoặc giới hạn của thay đổi |
| 06 – Testing & QA | QA/G5 evidence, giới hạn test và defect/rủi ro được bàn giao | Khi đánh giá rủi ro còn lại hoặc đối chiếu hành vi production |

Nếu Stage 07 chưa xác minh triển khai thành công, chỉ tiếp nhận thông tin sự cố khi cần; không ghi nhận bàn giao release hoàn tất. Ghi các đầu vào còn thiếu cùng owner xử lý; không đánh dấu hoàn tất bàn giao nếu thiếu bằng chứng bắt buộc.

## Quy ước
- Snapshot chỉ khi cần bảo toàn evidence; ghi source, timestamp/timezone, query và retention.
- Không lưu secret, credential, raw PII hoặc production dump trong repo.
- Giới hạn quyền theo data classification.
- Ghi rõ dữ liệu thiếu/stale; missing telemetry không đồng nghĩa healthy.

## Intake record
Ghi service/project, môi trường, phiên bản đang chạy, Deployment Record, Service Owner, người tiếp nhận và thời điểm bàn giao, on-call/escalation, dashboard/alert, runbook/rollback và rủi ro còn lại. Khi áp dụng, thêm architecture/dependency, SLI/SLO, RTO/RPO, DR, recent changes, telemetry/ticket và owner xử lý đầu vào còn thiếu. Ghi timestamp và timezone của bằng chứng.
