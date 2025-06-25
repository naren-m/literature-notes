---
layout: "default"
title: "index"
tags:
  - TODO
word_count: 246
created: "2025-06-25T14:36:45.446591"
modified: "2025-06-25T14:36:45.446591"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Docs"
    url: "/topics/docs//"
  - title: "Cse"
    url: "/topics/docs/cse//"
  - title: "Cryptography"
    url: "/topics/docs/cse/cryptography//"
  - title: "Stride"
    url: "/topics/docs/cse/cryptography/stride//"
---
---
layout: "default"
title: "STRIDE"
tags:
  - TODO
word_count: 106
created: "2024-11-28T18:24:53.170250"
modified: "2024-11-28T18:24:53.170250"
backlinks:
  - title: "Security Vulnerabilities"
    url: "security/security-vulnerabilities/"
  - title: "2024_10_07"
    url: "journals/2024_10_07/"
  - title: "Cryptography"
    url: "cse/cryptography/cryptography/"
  - title: "Digital signatures"
    url: "cse/cryptography/digital-signatures/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-01t08_11_36626zdesktop/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-29t01_57_40576zdesktop/"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Cse"
    url: "/topics/cse//"
  - title: "Cryptography"
    url: "/topics/cse/cryptography//"
---
- STRIDE(acronym) is categorization of vulnerabilities.
	- [Spoofing](cse/cryptography/spoofing/): theft of user credentials.
		- Compromise of [Authentication](security/authentication/)
	- [Tampering](cse/cryptography/tampering/): unauthorized data modification.
		- Compromise of [Integrity](cse/cryptography/integrity/).
	- [Repudiation](cse/cryptography/repudiation/): repudiation of activity.
		- Compromise of non-repudiation. (Trying to hide who we are) #TODO Circular definition fix it.
	- [Information Disclosure](cse/cryptography/information-disclosure/): unauthorized access to data.
		- Compromise of [Confidentiality](cse/cryptography/confidentiality/).
	- [Denial of Service](cse/cryptography/denial-of-service/): prevent correct access to data or services.
		- Compromise of [Availability](cse/cryptography/availability/).
	- [Elevation of Privilege](cse/cryptography/elevation-of-privilege/): unauthorized upgrade in privilege.
		- Compromise of *authorization* .
-
- Notes:
	- These [Security Vulnerabilities](security/security-vulnerabilities/) effect the core principles of [Cryptography](logseq/bak/cse/cryptography/cryptography/2024-11-29t01_57_40576zdesktop/), the [CIA Triad](logseq/bak/cse/cryptography/cia-triad/2024-11-01t08_11_36610zdesktop/)
	- Useful in deciding, based on the categorization, the best practices of how to defend or mitigate against current or future problems.