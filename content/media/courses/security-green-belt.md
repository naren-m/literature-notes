---
title: "Security Green Belt"
date: 2021-02-03
type: literature
category: "course/security"
tags: [security, cisco, xss, csrf, tls, ssl, buffer-overflow, aes-gcm, course-notes]
status: done
course: "Security Green Belt (Cisco internal)"
publisher: "Cisco Virtual"
field: CSE
topic: [Security]
source: "https://www.notion.so/be5af4122a4b466387b4b96ee4f2a9a6"
related: []
---

# Security Green Belt — course notes

Cisco internal MOOC on secure coding, web security attack classes, cryptography primitives, and TLS server implementation with Cisco's SSL library. The notes below are migrated from the Notion page; status was marked **Done** but with `Status = Not Started` — so these are working notes that were collected during a partial pass rather than a complete curriculum run.

## Key names and acronyms

- **XSS** — Cross-Site Scripting
- **CSRF** — Cross-Site Request Forgery
- **SOP** — Same-Origin Policy
- External reference: [CAPEC — Common Attack Pattern Enumeration](http://capec.mitre.org/index.html)

## CSRF — Cross-Site Request Forgery

Also written "XSRF", pronounced "sea-surf".

**Intent.** Force a user to unintentionally make a request to any domain. Because the browser attaches relevant cookies automatically, the victim appears authenticated to the target.

**Remediation.**

- Encrypted tokens
- Double-submit cookies
- Synchronizer tokens

OWASP has a standard CSRF prevention cheat sheet; follow that.

## XSS — Cross-Site Scripting

Two screenshots in the source page illustrated the attack flow; diagrams not migrated. XSS lets an attacker inject script into a trusted page's DOM, which then executes with the victim's origin privileges. Preventions are output encoding (context-aware), CSP, input validation, and HttpOnly cookies.

## Attack detail: buffer / heap / memory overflow

### Software engineering — Next-gen encryption

**AES-GCM** (Advanced Encryption Standard — Galois Counter Mode) was the recommended symmetric cipher mode. GCM provides authenticated encryption: confidentiality + integrity in one primitive.

### Using Safe C

- The **CWE Top 25 Most Dangerous Software Errors** is the canonical checklist.
- Classic buffer overflow: buffer copy without checking input size.
- **Safe C constraint handler** — invoked when an error condition is detected; registered at system start-up. Possible actions:
  - Ignore error
  - Log error with identifying trace data
  - Kill the process
  - Even reset the system
- Defining constraint handlers saves time and ensures notification.
- `strlen()` is unbounded and dangerous when the string is not NULL-terminated.
- Unbounded calls to avoid: `strlen()`, `strcmp()`, `strcpy()`.

## Implementing a TLS Server with Cisco SSL

Steps, in order:

1. **Select protocol version.**
   - SSL 3.0 / TLS 1.0 / TLS 1.1 / TLS 1.2 — corresponding methods: `TLSv1_2_server_method()`, `TLSv1_1_server_method()`, `TLSv1_server_method()`, `SSLv3_server_method()`, `SSLv23_server_method()`.
2. **Load local certificate and private key.** Required.
   - Loads the X.509 certificate and private key the server uses to identify itself to the TLS client.
   - The server cert should be signed by a valid trust chain known to the client.
   - `SERVER_CERT` may also contain CA certificates presented to the client during handshake.
3. **Enable single-use ephemeral DH and ECDH keys.**
   - Some cipher suites use ephemeral Diffie-Hellman keys.
   - Single-use ephemeral keys should be **enabled** for secure TLS (forward secrecy).
   - Same for ECDH keys when using an ECC certificate.
   - **Disable SSL 2.0** via options on the context.
4. **Load DH and ECDH parameters for ephemeral key exchange.**
   - DH params: used for DH ephemeral key exchange. Parameters should not be hard-coded in the application (sample code does not follow this rule). Generation is slow; do it once per product-deployment instance, during first-time setup.
   - ECDH params: used for ECDH ephemeral exchange. Select the desired ECC curve, then generate a new key. Also must not be hard-coded.
5. **Optional: enable specific cipher suites.**
   - Specify the subset of suites the server will accept.
   - Use this API to disable insecure ciphers (RC4, MD5, etc.).
6. **Load trusted root certificates.**
7. **Load certificate and private key** (application-level).
8. **Optional: enable peer authentication** (mutual TLS).
9. **Open listening socket and wait for incoming request.**

## Open threads

- Migrate the embedded CSRF / buffer-overflow / AES-GCM / TLS diagrams if the S3 attachments remain accessible (the Notion page had presigned URLs that will have expired).
- Pair with [[rfc-draft-sztp-csr]] — zero-touch provisioning CSR work overlaps with the TLS/cert handling described here.
- Optional promotion: lift the "Safe C" checklist and "TLS server init steps" into standalone permanent notes under `content/domains/` once they're used in real code.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/be5af4122a4b466387b4b96ee4f2a9a6). See [[notion-migration]] and [[courses-library]].*
