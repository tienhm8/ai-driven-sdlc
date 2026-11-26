---
name: authentication
description: "Design or review defensive authentication: identity provider use, token verification, session lifetime, and logging. Use when a change touches login, token handling, or an identity guard."
---

# Authentication

1. Use the approved identity provider and library; do not build custom token formats or password schemes. Take identity only from a verified token, never from a field the client supplies.
2. Verify the token fully: signature against the provider's keys, issuer, audience, expiry, and the allowed algorithms. Set each explicitly from configuration. A verification that checks only the signature does not establish that the token was meant for this service.
3. Define the session lifetime and how a token is revoked or refreshed to match the risk of the data. Handle verification failure as unauthenticated (401) without revealing why.
4. Never write tokens, passwords, or keys to logs, error messages, source control, or browser storage that scripts can read unless that is the approved design. Store passwords only as salted, slow hashes at a reviewed cost.
5. Test with fixtures: missing, malformed, expired, wrong-issuer, wrong-audience, and tampered tokens must be rejected, and a valid token must succeed. Do not use real credentials.

## This stack

Backend guards, SSO verification, and what to confirm in `aisoft-backend` are in the NestJS skill's [authentication reference](../../backend/nestjs/references/authentication.md) and the [OWASP map](../owasp/references/owasp-in-this-stack.md). Frontend session and permission handling are in the Umi Max skill's [routing and access reference](../../frontend/umi-max/references/routing-access.md). Use those instead of restating them here.
