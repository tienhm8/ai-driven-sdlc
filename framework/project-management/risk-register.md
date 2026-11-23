# Risk Register
Risk là sự kiện chưa chắc chắn có thể ảnh hưởng mục tiêu. Issue là sự kiện đã xảy ra và thuộc `issue-log.md`.

## Scoring
Probability (P) và Impact (I): 1–5. Exposure = P × I.
Mức tham khảo: 1–4 Low, 5–9 Medium, 10–16 High, 17–25 Critical; điều chỉnh theo risk appetite của tổ chức.

| ID | Risk statement (cause–event–effect) | Category | P | I | Score | Response | Owner | Trigger / Due | Status | Residual |
|---|---|---|---:|---:|---:|---|---|---|---|---|
| RSK-001 | | | | | | Avoid / Mitigate / Transfer / Accept | | | Open | |

Review theo cadence dự án và trước Gate liên quan. Risk Critical/High phải escalation. Nếu risk xảy ra, tạo `ISS-*` và liên kết. Risk acceptance cần approver, rationale, mitigation và review date.
