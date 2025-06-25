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
	- [Spoofing](docs/cse/cryptography/spoofing/index/): theft of user credentials.
		- Compromise of [Authentication](docs/security/authentication/index/)
	- [Tampering](docs/cse/cryptography/tampering/index/): unauthorized data modification.
		- Compromise of [Integrity](docs/cse/cryptography/integrity/index/).
	- [Repudiation](docs/cse/cryptography/repudiation/index/): repudiation of activity.
		- Compromise of non-repudiation. (Trying to hide who we are) #TODO Circular definition fix it.
	- [Information Disclosure](docs/cse/cryptography/information-disclosure/index/): unauthorized access to data.
		- Compromise of [Confidentiality](docs/cse/cryptography/confidentiality/index/).
	- [Denial of Service](docs/cse/cryptography/denial-of-service/index/): prevent correct access to data or services.
		- Compromise of [Availability](docs/cse/cryptography/availability/index/).
	- [Elevation of Privilege](docs/cse/cryptography/elevation-of-privilege/index/): unauthorized upgrade in privilege.
		- Compromise of *authorization* .
-
- Notes:
	- These [Security Vulnerabilities](docs/security/security-vulnerabilities/index/) effect the core principles of [Cryptography](logseq/bak/cse/cryptography/cryptography/2024-11-29t01_57_40576zdesktop/), the [CIA Triad](logseq/bak/cse/cryptography/cia-triad/2024-11-01t08_11_36610zdesktop/)
	- Useful in deciding, based on the categorization, the best practices of how to defend or mitigate against current or future problems.