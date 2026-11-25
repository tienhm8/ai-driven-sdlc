# Biên bản Triển khai (Deployment Record)

> Nguồn duy nhất cho bằng chứng thực thi, sai lệch, sự cố và bàn giao sang Stage 08. `production-approval.md` (G6) chỉ liên kết tới file này.

## Metadata
- Deployment ID: `DEP-{{NUMBER}}`
- Release version:
- Environment:
- Artifact/image digest (SHA-256) thực tế:
- Commit SHA:
- Deployment plan (link, version):
- Rollback plan (link, version):
- Tham chiếu hồ sơ G6 (N/A cho non-production):
- Authorization ID / lượt bắt đầu `start_event_id` (nếu có; N/A cho non-production):
- Tham chiếu kết quả tin cậy (`action_result_ref`, nếu dùng Workflow Engine):
- Người thực hiện triển khai:
- Timestamp bắt đầu / kết thúc (timezone):
- Pipeline run:

## Thực thi: kế hoạch so với thực tế
| Checkpoint | Kế hoạch | Thực tế | Kết quả | Bằng chứng |
|---|---|---|---|---|
| {{STEP}} | {{PLAN}} | {{ACTUAL}} | Pass/Fail/Skipped | {{LINK}} |

- Sai lệch so với kế hoạch (và ai chấp thuận):
- Artifact digest thực tế có khớp G5 (và G6 nếu là Production): Yes / No / Chưa xác minh

## Sự cố
- Có sự cố trong khi triển khai: Yes / No
- Mô tả, thời điểm, mức độ, incident/change record:
- Đã thực hiện rollback: Yes / No (nếu Yes: phạm vi, thời điểm, ai quyết định)
- Dữ liệu: đã rollback/restore/forward-fix hay không (rollback ứng dụng không đồng nghĩa rollback dữ liệu):

## Xác minh
- Smoke test:
- Health check:
- Chỉ số error/latency:
- Kiểm tra nghiệp vụ và dữ liệu:
- Khoảng thời gian theo dõi monitoring và kết quả:

## Kết quả
- Kết quả: Thành công đã xác minh / Rollback đã xác minh (`rolled_back`) / Thất bại không thay đổi đích đã xác minh (`failed_no_changes`) / Chưa xác định.
- Chỉ ghi kết quả đã xác minh khi có bằng chứng tin cậy. Không coi rollout một phần, rollback chưa xác minh hoặc thiếu bằng chứng là thành công hay đủ điều kiện thử lại.
- Hành động tiếp theo và owner:

## Bàn giao cho Operations
Loại bàn giao (nếu áp dụng):
- [ ] **Bàn giao release sang Stage 08:** chỉ khi Production thành công đã xác minh.
- [ ] **Bàn giao thông tin sự cố:** ghi trạng thái thực tế, hành động đang mở và người xử lý. Không chuyển stage hay ghi release mới đã triển khai thành công.

| Mục | Nội dung / link |
|---|---|
| Phiên bản đang chạy tại môi trường đích và artifact digest | |
| Dashboard | |
| Alert rules | |
| Runbook | |
| On-call (đội, lịch, kênh escalation) | |
| SLI/SLO và RTO/RPO (giá trị hoặc tham chiếu) | |
| Kiến trúc và dependencies (tham chiếu) | |
| Known issues | |
| Residual risks (owner, thời hạn xử lý) | |
| Dữ liệu/feature flag cần theo dõi | |
| Người/đội nhận bàn giao | |
| Thời điểm nhận bàn giao (timezone) | |

## Ký xác nhận (con người)
- Deployment owner:
- Release Manager:
- Người tiếp nhận bàn giao (nếu có):
- Timestamp:
- Tham chiếu xác nhận kết quả triển khai:
