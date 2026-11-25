# Security Review Template

> Dùng khi thay đổi thuộc phạm vi security review. Các mục nhanh có trong [security-checklist](../checklists/security-checklist.md) được mở rộng ở đây; phần phạm vi/trust boundary, bằng chứng và kết luận chuyên môn chỉ có trong mẫu này. Severity dùng thang chung Critical/High/Medium/Low/Info ([human-review.md](../human-review.md#4-phân-loại-finding)).

## Metadata
- PR / commit:
- Reviewer:
- Security reviewer (nếu cần):
- System/data classification:
- Threat model/reference:

## Scope & trust boundaries
- Entry points:
- External inputs:
- Trust boundaries:
- Sensitive data:
- Privileged operations:

## Review areas
- [ ] Authentication and session management
- [ ] Authorization / least privilege / object-level access
- [ ] Input validation and output encoding
- [ ] Injection (SQL/NoSQL/OS/template/LDAP)
- [ ] Cryptography and key/secret handling
- [ ] Sensitive data storage, transport and logging
- [ ] File upload/download and path traversal
- [ ] SSRF, deserialization and unsafe redirects
- [ ] Dependency and supply-chain risk
- [ ] Rate limiting, abuse and denial of service
- [ ] Security headers, CORS and CSRF where applicable
- [ ] Audit logging and error disclosure

## Findings
| ID | Severity | Location | Evidence / attack scenario | Impact | Remediation | Status |
|---|---|---|---|---|---|---|
| | | | | | | |

## Verification
- Static scan:
- Dependency scan:
- Tests/manual validation:
- Limitations:

## Decision
- Security recommendation: Pass / Changes Required / Blocked
- Required remediation:
- Accepted risk (must name approver and expiry):
- Human security approver:
- Date:
