# Risk Register
Risk là sự kiện chưa chắc chắn có thể ảnh hưởng mục tiêu. Issue là sự kiện đã xảy ra và thuộc `issue-log.md`.

## Scoring
Probability (P) và Impact (I): 1–5. Exposure = P × I.
Mức tham khảo: 1–4 Low, 5–9 Medium, 10–16 High, 17–25 Critical; điều chỉnh theo risk appetite của tổ chức.

No entries

| ID | Risk statement (cause–event–effect) | Category | P | I | Score | Response | Owner | Trigger / Due | Status | Residual | Hồ sơ risk / bằng chứng acceptance |
|---|---|---|---:|---:|---:|---|---|---|---|---|---|

Review theo cadence dự án và trước Gate liên quan. Risk Critical/High phải escalation. Nếu risk xảy ra, tạo `ISS-*` và liên kết. Cấp ID dạng `RISK-0001`. Risk acceptance cần approver, rationale, mitigation và review date; dẫn đến risk record hoặc phê duyệt gốc, không chép lại bằng chứng.
