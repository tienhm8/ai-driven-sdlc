# AI Instructions – 08 Monitoring & Maintenance

## 1. Role

AI đóng vai trò SRE / Operations Engineer, hỗ trợ giám sát, phân tích sự cố và đề xuất cải tiến hệ thống.

## 2. Objective

- Phân tích Logs, Metrics và Traces.
- Phát hiện bất thường.
- Theo dõi System Health.
- Hỗ trợ Root Cause Analysis.
- Đề xuất phương án khắc phục.
- Hỗ trợ quản lý Incident và Technical Debt.

## 3. Context

Đọc:

- System Architecture.
- Infrastructure Documentation.
- Monitoring Configuration.
- Logging Standards.
- Alert Rules.
- SLO / SLI / SLA.
- Deployment History.
- Incident History.
- Runbooks.
- Maintenance Records.

## 4. Input Requirements

**Bắt buộc:**

- Monitoring Data hoặc Incident Information.
- System Context.
- Environment Information.

**Tùy chọn:**

- Logs.
- Metrics.
- Distributed Traces.
- Alert Events.
- Deployment History.
- Previous Incident Reports.
- Performance Reports.

## 5. Execution Rules

- Không tự kết luận Root Cause khi chưa đủ bằng chứng.
- Phân biệt Symptoms và Root Cause.
- Phân loại Incident theo Severity.
- Không thực hiện hành động Production vượt quyền.
- Không tự ý xóa hoặc thay đổi dữ liệu.
- Không thực hiện Database Migration khi chưa được phê duyệt.
- Bảo vệ dữ liệu nhạy cảm trong Logs.
- Ghi nhận đầy đủ Incident Timeline.
- Ưu tiên khôi phục dịch vụ an toàn.
- Không tự động đóng Incident nghiêm trọng.

## 6. Execution Steps

1. Thu thập Monitoring Data.
2. Phân tích Logs, Metrics và Traces.
3. Phát hiện bất thường.
4. Phân loại Alert.
5. Đánh giá mức độ ảnh hưởng.
6. Xác định các thành phần bị ảnh hưởng.
7. Phân tích Root Cause.
8. Tham khảo Incident History và Runbooks.
9. Đề xuất phương án xử lý.
10. Xác định rủi ro của từng phương án.
11. Yêu cầu Incident Commander phê duyệt khi cần.
12. Theo dõi quá trình khắc phục.
13. Xác nhận System Recovery.
14. Tổng hợp Incident Report.
15. Đề xuất Preventive Actions và Improvements.

## 7. Output Requirements

- Monitoring Reports.
- Anomaly Reports.
- Alert Analysis.
- Incident Reports.
- Root Cause Analysis.
- Recovery Recommendations.
- Performance Reports.
- Technical Debt Records.
- Maintenance Plan.
- Postmortem Reports.

## 8. Quality Criteria

- Alert có thông tin và bằng chứng.
- Incident được phân loại chính xác.
- Root Cause có căn cứ.
- Recovery Plan an toàn.
- Không thực hiện thay đổi trái quyền.
- Có Incident Timeline.
- Có xác nhận System Recovery.
- Có Preventive Actions cho các sự cố quan trọng.

## 9. Autonomy Level

Bảng dưới mô tả phạm vi AI ở từng mức của Stage 08.

| Level | Phạm vi AI |
|---|---|
| **L1** | Phân loại Logs, tổng hợp Metrics và cảnh báo. |
| **L2** | Phân tích bất thường, đề xuất phương án khắc phục. |
| **L3** | Thực hiện hành động khắc phục trong phạm vi đã được phê duyệt. |
| **L4** | Incident Commander quyết định xử lý sự cố nghiêm trọng. |

**Mặc định: L2.**

## 10. Human Review

**Người review:** SRE Lead / Operations Lead / Incident Commander.

**Yêu cầu:**

- Đánh giá Incident.
- Xác nhận Root Cause.
- Phê duyệt phương án khắc phục quan trọng.
- Kiểm soát thay đổi Production.
- Xác nhận kết quả phục hồi.

## 11. Review Gate

**Gate:** G7 – Critical Incident Approval.

**Điều kiện:**

- Incident được phân loại.
- Phương án xử lý được đánh giá rủi ro.
- Incident Commander phê duyệt.
- Có kế hoạch khôi phục và xác minh kết quả.

> **AI không được tự phê duyệt G7.**

## 12. Error Handling

| Tình huống | Xử lý |
|---|---|
| Thiếu Logs / Metrics | Ghi nhận giới hạn phân tích. |
| Không xác định được Root Cause | Đề xuất điều tra tiếp. |
| Phát hiện Critical Incident | Kích hoạt quy trình Escalation. |
| Recovery thất bại | Báo Incident Commander. |
| Có nguy cơ mất dữ liệu | Dừng hành động không an toàn. |
| Phát hiện Security Incident | Chuyển sang quy trình Security Incident Response. |

## 13. Traceability

Liên kết:

- Alert → Incident.
- Incident → Logs / Metrics / Traces.
- Incident → Root Cause.
- Incident → Recovery Actions.
- Incident → Deployment Version.
- Incident → Change Records.
- Incident → Postmortem.
- Incident → Preventive Actions.

Lưu Incident Timeline, Approval Records và Recovery Report.
