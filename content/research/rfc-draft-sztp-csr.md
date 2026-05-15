---
title: "RFC Draft for SZTP CSR extension"
date: 2020-08-20
type: research
category: "CSE/security"
tags: [security, rfc, sztp, rfc8572, pki, csr, onboarding]
status: incomplete
source: "Notion Notes DB — working notes on an IETF SZTP CSR extension draft"
related: [resurrecting-duckling-model]
---

# RFC Draft for SZTP CSR extension

Working notes on a draft extension to **RFC 8572** (Secure Zero Touch Provisioning, SZTP) that adds the ability for an onboarding device to generate a Certificate Signing Request (CSR) and obtain an owner-issued identity certificate (e.g., LDevID) as part of onboarding.

## What is it?

The draft extends RFC 8572 to enable the device to:

1. Announce that it can generate a new key pair to use for its CSR.
2. Obtain an identity certificate (e.g., LDevID) as part of owner information (OI).
3. Let the **server** identify the device in its own terms — using an owner-issued certificate rather than the manufacturer's.

Two modes are added to the `input` parameter of the `get-bootstrapping-data` RPC:

### `csr-support`

Used by the device to tell the server it can generate CSRs.

- **`key-generation`** — presence indicates the device can generate a new asymmetric key pair. In its absence, the server may request a CSR using the key associated with the device's existing IDevID / LDevID / SUDI. Carries a list of supported key algorithms.
- **`csr-generation`** — specifies the device's ability to generate a CSR, with a list of supported formats.

### `csr`

Used by the device to send its CSR to the server in the format the server selected via `request-info`.

- **`request-type`** — mandatory; a choice among PKCS#10, CMC (Certificate Management over CMS), and CMP (Certificate Management Protocol).

### YANG module sketch — `ietf-sztp-bootstrap-server`

```
module: ietf-sztp-bootstrap-server
   rpcs:
     +---x get-bootstrapping-data
        +---w input
        |  +---w signed-data-preferred?   empty
        |  +---w hw-model?                string
        |  +---w os-name?                 string
        |  +---w os-version?              string
        |  +---w nonce?                   binary
        |  +---w sztp-csr:csr-support!
        |  |  +---w sztp-csr:key-generation!
        |  |  |  +---w sztp-csr:supported-algorithms
        |  |  |     +---w sztp-csr:algorithm-identifier*   binary
        |  |  +---w sztp-csr:csr-generation
        |  |     +---w sztp-csr:supported-formats
        |  |        +---w sztp-csr:format-identifier*   identityref
        |  +---w sztp-csr:csr!
        |     +---w (sztp-csr:request-type)
        |        +--:(sztp-csr:p10)  +---w sztp-csr:p10?   ct:csr
        |        +--:(sztp-csr:cmc)  +---w sztp-csr:cmc?   binary
        |        +--:(sztp-csr:cmp)  +---w sztp-csr:cmp?   binary
        +--ro output
           +--ro reporting-level?    enumeration {onboarding-server}?
           +--ro conveyed-information    cms
           +--ro owner-certificate?      cms
           +--ro ownership-voucher?      cms
```

### Intermediate response — `request-info` in `error-info`

The server tells the device to sign a specific CSR:

- `selected-algorithm`
- `selected-format`
- `cert-req-info` — a fully-populated `CertificateRequestInfo` the device signs to produce the CSR. When absent, the device falls back to the structure defined in its IDevID (SUDI).

```
module: ietf-restconf
  +--ro errors
     +--ro error* []
        +--ro error-type       enumeration
        +--ro error-tag        string
        +--ro error-app-tag?   string
        +--ro error-path?      instance-identifier
        +--ro error-message?   string
        +--ro error-info
           +--ro request-info
              +--ro key-generation!
              |  +--ro selected-algorithm
              |     +--ro algorithm-identifier    binary
              +--ro csr-generation
              |  +--ro selected-format
              |     +--ro format-identifier    identityref
              +--ro cert-req-info?    binary
```

## How does the flow work?

1. Device advertises the `csr-support` node in its `get-bootstrapping-data`.
2. If the server wants a CSR, it responds with **HTTP 405 (Method Not Allowed)** carrying the CSR details. *(This is flagged as strange in the working notes — why not a 2xx variant or `449 Retry With`?)*
3. Device re-sends `get-bootstrapping-data` with the `csr` node populated.
4. Server responds with OI containing a signed identity certificate.
   - How the cert is delivered is out of scope for the draft. Options include `pre-configuration-script` or `configuration` nodes.
   - The server should also configure the issuer's signing certificate.

## Why?

The goal is to give the device a **unique identity in the owner's network** with a certificate that the owner controls — rather than relying on the manufacturer's identity. SUDI continues to serve as the identifier, but the cert is owner-issued to maintain a common model across vendors.

Generating a new key serves a dual purpose:

1. Lets the device apply for a digital identity certificate via CSR.
2. The random bytes act as a **nonce** that protects against replay attacks.

## Open questions

- What is LDevID? *(Answer: it's the customer's SUDI-equivalent — an owner-issued local device identity certificate.)*
- Why respond with an error (405) instead of a 2xx variant? Still unresolved in the notes.

## Related

- [[resurrecting-duckling-model]] — the imprint-stage TOFU problem this extension is trying to bound.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/0586d9ac10eb42f5b4bd2dde208639f5). See [[notion-migration]].*
