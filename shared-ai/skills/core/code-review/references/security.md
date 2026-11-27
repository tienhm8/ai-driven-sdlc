# Review checklist: security (OWASP Top 10, quick pass)

Check the common defects visible in the diff. A change to authentication, authorization, sensitive data, or external input also needs the `owasp` skill or a security review.

- Missing server-side authorization, especially per-record (fetching by ID without an ownership check: IDOR/BOLA).
- Assigning all input to an object (mass assignment) instead of accepting only validated fields.
- Injection: string concatenation into queries, system commands, templates, or paths.
- Output not encoded for its context (XSS).
- Returning or logging sensitive fields, tokens, or secrets.
- Uploads: no check of type, size, content, or storage location.
- Calling user-supplied URLs (SSRF); file paths from input (path traversal).
- No rate limit at sensitive points (login, OTP, password reset).
