---
layout: "default"
title: "Rfc1831"
tags:
  - articles
word_count: 360
created: "2025-06-25T14:36:45.428900"
modified: "2025-06-25T14:36:45.428900"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Docs"
    url: "/topics/docs//"
  - title: "Highlights"
    url: "/topics/docs/highlights//"
  - title: "Articles"
    url: "/topics/docs/highlights/articles//"
  - title: "Rfc1831"
    url: "/topics/docs/highlights/articles/rfc1831//"
---
---
layout: "default"
title: "Rfc1831"
tags:
  - articles
word_count: 323
created: "2024-11-28T18:24:53.203487"
modified: "2024-11-28T18:24:53.203487"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Highlights"
    url: "/topics/highlights//"
  - title: "Articles"
    url: "/topics/highlights/articles//"
---
# Rfc1831

![img](https://readwise-assets.s3.amazonaws.com/static/images/article0.00998d930354.png)

## Metadata

- Author: datatracker.ietf.org

- Full Title: Rfc1831(RPC: Remote Procedure Call Protocol Specification Version 2)

- Category: #articles

- URL: https://datatracker.ietf.org/doc/html/rfc1831

### Highlights

- A network service is a collection of one or more remote programs
- A remote program implements one or more remote procedures;
  - the procedures, their parameters, and results are documented in the specific program's protocol specification
- The ONC RPC protocol is based on the remote procedure call model,
  which is similar to the local procedure call model. In the local
  case, the caller places arguments to a procedure in some well-
  specified location (such as a register window). It then transfers
  control to the procedure, and eventually regains control. At that
  point, the results of the procedure are extracted from the well-
  specified location, and the caller continues execution.
- The remote procedure call model is similar. One thread of control
  logically winds through two processes: the caller's process, and a
  server's process. The caller process first sends a call message to
  the server process and waits (blocks) for a reply message. The call
  message includes the procedure's parameters, and the reply message
  includes the procedure's results. Once the reply message is
  received, the results of the procedure are extracted, and caller's
  execution is resumed
- 7. RPC PROTOCOL REQUIREMENTS
     The RPC protocol must provide for the following:
     (1) Unique specification of a procedure to be called.
     (2) Provisions for matching response messages to request messages.
     (3) Provisions for authenticating the caller to service and
     vice-versa.
- The RPC call message has three unsigned integer fields -- remote
  program number, remote program version number, and remote procedure
  number -- which uniquely identify the procedure to be called.
- Therefore, the
  call message also has in it the RPC version number, which is always
  equal to two for the version of RPC described here.
