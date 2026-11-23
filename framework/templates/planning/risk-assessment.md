# Đánh giá Rủi ro (Risk Assessment)

## Metadata
- Risk ID: `RISK-{{NUMBER}}`
- Project / Workstream: `{{PROJECT}}`
- Ngày đánh giá: `{{DATE}}`
- Owner: `{{RISK-OWNER}}`
- Status: Identified / Analyzing / Mitigating / Accepted / Closed
- Tham chiếu liên quan (requirement / task / ADR): `{{REFERENCES}}`

## 1. Mô tả rủi ro
Do `{{CAUSE}}`, có thể xảy ra `{{UNCERTAIN-EVENT}}`, dẫn đến `{{IMPACT}}`.

## 2. Phân loại
- Category: Technical / Security / Delivery / Schedule / Cost / Vendor / Compliance / Operational / Other
- Mục tiêu bị ảnh hưởng:
- Component / giai đoạn bị ảnh hưởng:
- Trigger / dấu hiệu cảnh báo sớm:
- Giả định:

## 3. Chấm điểm
| Tiêu chí | Điểm | Lý do |
|---|---:|---|
| Likelihood (khả năng xảy ra) | 1–5 | {{RATIONALE}} |
| Impact (mức tác động) | 1–5 | {{RATIONALE}} |
| Điểm tiềm tàng (L × I) | 1–25 | {{SCORE}} |
| Khả năng còn lại (residual likelihood) | 1–5 | {{SCORE}} |
| Tác động còn lại (residual impact) | 1–5 | {{SCORE}} |
| Điểm còn lại (L × I) | 1–25 | {{SCORE}} |

Gợi ý phân mức: 1–4 Low, 5–9 Medium, 10–16 High, 17–25 Critical. Ưu tiên ma trận rủi ro đã được tổ chức phê duyệt nếu có.

## 4. Chiến lược xử lý
- Chiến lược: Avoid / Mitigate / Transfer / Accept
- Biện pháp phòng ngừa:
- Phương án dự phòng (contingency):
- Nguồn lực cần thiết:
- Ngày mục tiêu:

| Action ID | Hành động | Owner | Hạn xử lý | Status | Bằng chứng |
|---|---|---|---|---|---|
| `RA-001` | {{ACTION}} | {{OWNER}} | {{DATE}} | Open | {{LINK}} |

## 5. Rủi ro còn lại và phụ thuộc
- Rủi ro còn lại:
- Phụ thuộc:
- Ngưỡng escalation:
- Rủi ro liên quan:

## 6. Chấp nhận / Escalation
- Yêu cầu chấp nhận rủi ro: Yes / No
- Lý do nghiệp vụ:
- Người có thẩm quyền chấp nhận:
- Quyết định / timestamp:
- Ngày hết hạn / ngày review lại:

## 7. Theo dõi
- Tần suất review:
- Lần review tiếp theo:
- Trigger đánh giá lại:
- Tiêu chí đóng rủi ro:

## 8. Lịch sử
| Ngày | Cập nhật bởi | Thay đổi |
|---|---|---|
| {{DATE}} | {{OWNER}} | Đánh giá ban đầu |
