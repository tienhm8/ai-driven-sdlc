# QA Sign-off – Gate G5

## Release/test cycle
- Project/release, test cycle:
- Requirement version:
- Artifact URI/version và SHA-256 (`artifact_sha256`):
- G4 review/merge reference, verified merge commit SHA và bằng chứng merge:
- Verified build provenance (`provenance_ref`):
- Environment / cấu hình đã xác minh (tham chiếu feature flag nếu dùng để giới hạn phạm vi):
- Test plan/report version và TESTRUN IDs:
- Sign-off date:

## Quality summary
| Metric | Result | Target/criteria | Status |
|---|---|---|---|
| Critical test execution | | | |
| Requirement coverage | | | |
| Risk coverage | | | |
| Pass/Fail/Blocked/Not Run | | | |
| Critical/High open defects | | | |
| Regression | | | |
| Security/non-functional checks | | | |

## Open defects & residual risks
| ID | Severity | Impact | Mitigation | Risk owner | Disposition / approver / expiry / evidence |
|---|---|---|---|---|---|
| | | | | | |

## Coverage gaps & limitations
Liệt kê requirement chưa test, scenario loại trừ, flaky test, environment limitation và rationale.

## QA recommendation
- [ ] Go
- [ ] Conditional Go (chỉ là khuyến nghị QA)
- [ ] No-Go
- [ ] Blocked

Rationale/follow-up (điều kiện, owner, thời hạn và risk acceptance nếu áp dụng):

## G5 approval
- Review ID và tham chiếu/phiên bản gói review:
- SHA-256 gói review (`review_context_sha256`):
- Trạng thái tổng hợp G5 và tham chiếu trên platform:

Ghi quyết định riêng của từng approver theo [gate policy](../../governance/human-review-gates/gate-policy.md#lifecycle); không dùng khuyến nghị QA làm trạng thái tổng hợp. QA Lead và Product Owner phải là hai người riêng biệt, duyệt đúng artifact và gói review ở trên. Áp dụng [quy tắc G5](../../governance/human-review-gates/G5-qa-approval.md) và QA Sign-off Checklist của Stage 06.

| Role | Name | Decision | Timestamp | Evidence/reference |
|---|---|---|---|---|
| QA Lead | | | | |
| Product Owner | | | | |
| Security/Domain approver (if required) | | | | |

## Audit
Audit event IDs / exception references:

Chỉ ghi phê duyệt từ quyết định của con người; khuyến nghị AI không phải human approval. Không ghi secret, token hay PII không cần thiết.
