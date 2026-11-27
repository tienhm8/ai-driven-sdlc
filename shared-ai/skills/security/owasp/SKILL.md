---
name: owasp
description: "Run a defensive security review of code or a design: identify assets and trust boundaries, classify risks against OWASP Top 10:2025, verify controls, and record regression tests. Use for security-sensitive changes; no exploit development."
metadata:
  owasp-top-10: "2025"
  owasp-asvs: "5.0.0"
---

# OWASP defensive review

Scope: defensive review within the authorized scope. Do not write exploits, probe systems you were not given, or test against production.

1. Identify the assets (data, credentials, capabilities) and the trust boundaries the change touches: where untrusted input enters, where identity is established, and which resources it can reach.
2. Classify each risk against the OWASP Top 10:2025 categories. The Top 10 is an **awareness and classification** list, not a pass/fail standard. Take verifiable requirements from OWASP ASVS (version 5.0.0, cited as `v5.0.0-<chapter>.<section>.<requirement>`) and from the framework's [security standards](../../../../framework/standards/security/security-standards.md).
3. For each risk, check the control that is meant to stop it and whether it is actually in effect: access checks on the server for the specific resource, parameterized queries, output encoding or sanitizing, safe configuration, and handling of errors. A control that exists in code but is not wired or not reached is not a control.
4. Record each finding with location, trigger condition, impact, and a mitigation, and add a defensive regression test where one is possible. Do not put secrets, tokens, or personal data into reports or tests; redact evidence.
5. State what you did not review and which assumptions you relied on.

## OWASP Top 10:2025 (categories, for classification)

A01 Broken Access Control · A02 Security Misconfiguration · A03 Software Supply Chain Failures · A04 Cryptographic Failures · A05 Injection · A06 Insecure Design · A07 Authentication Failures · A08 Software or Data Integrity Failures · A09 Security Logging and Alerting Failures · A10 Mishandling of Exceptional Conditions.

## Where this applies in the two bases

[OWASP in this stack](references/owasp-in-this-stack.md) maps these categories to the concrete places in `aisoft-backend` and `base-web` to inspect. Open it for a review of either repository. For identity and permission mechanisms use the `authentication` and `authorization` skills.
