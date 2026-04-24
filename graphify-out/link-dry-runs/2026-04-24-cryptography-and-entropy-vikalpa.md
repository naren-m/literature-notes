# Link Enhancement Dry Run - Cryptography and Entropy/Vikalpa
Date: 2026-04-24

Scope:
- Single domain: `content/domains/computer-science/cryptography`
- Cross domain: `content/research/entropy-vikalpa` linking outward to cryptography and Sanskrit/Yoga concept notes

No note files were modified. Candidates below are exact insertion previews.

## Single-Domain Candidates

### D1 - high
- Source: `content/domains/computer-science/cryptography/Data Sensitivity.md:8`
- Target: `[[Information Disclosure]]` (`content/domains/computer-science/cryptography/Information Disclosure.md`)
- Reason: Exact mention of an existing STRIDE/security note in a short list of sensitivity consequences.

Current:
> - Information disclosure

Suggested:
> - [[Information Disclosure|Information disclosure]]

### D2 - high
- Source: `content/domains/computer-science/cryptography/Digital signatures.md:3`
- Target: `[[Public Key]]` (`content/domains/computer-science/cryptography/Public Key.md`)
- Reason: Digital signatures explicitly describe private/public key verification; Public Key is an existing concept note.

Current:
> Digital Signature = [[Hashing]] + [[Encryption]] (encrypted with Private key and decrypted by Public key)

Suggested:
> Digital Signature = [[Hashing]] + [[Encryption]] (encrypted with Private key and decrypted by [[Public Key|Public key]])

### D3 - high
- Source: `content/domains/computer-science/cryptography/Digital signatures.md:6`
- Target: `[[Confidentiality]]` (`content/domains/computer-science/cryptography/Confidentiality.md`)
- Reason: The note contrasts digital signatures with a CIA-triad property that already has a permanent note.

Current:
> - Does NOT provide Confidentiality

Suggested:
> - Does NOT provide [[Confidentiality|Confidentiality]]

### D4 - high
- Source: `content/domains/computer-science/cryptography/Digital signatures.md:8`
- Target: `[[Integrity]]` (`content/domains/computer-science/cryptography/Integrity.md`)
- Reason: Integrity is the core property digital signatures protect and already has a note.

Current:
> Digital signatures are a combination of hashing and encryption to verify the identity of a sender and integrity of the message.

Suggested:
> Digital signatures are a combination of hashing and encryption to verify the identity of a sender and [[Integrity|integrity]] of the message.

### D5 - high
- Source: `content/domains/computer-science/cryptography/Digital signatures.md:11`
- Target: `[[Spoofing]]` (`content/domains/computer-science/cryptography/Spoofing.md`)
- Reason: The STRIDE threat is listed by name and has a matching note.

Current:
> - Spoofing

Suggested:
> - [[Spoofing|Spoofing]]

### D6 - high
- Source: `content/domains/computer-science/cryptography/Digital signatures.md:12`
- Target: `[[Tampering]]` (`content/domains/computer-science/cryptography/Tampering.md`)
- Reason: The STRIDE threat is listed by name and has a matching note.

Current:
> - Tampering

Suggested:
> - [[Tampering|Tampering]]

### D7 - high
- Source: `content/domains/computer-science/cryptography/Digital signatures.md:13`
- Target: `[[Repudiation]]` (`content/domains/computer-science/cryptography/Repudiation.md`)
- Reason: The STRIDE threat is listed by name and has a matching note.

Current:
> - Repudiation

Suggested:
> - [[Repudiation|Repudiation]]

### D8 - medium-high
- Source: `content/domains/computer-science/cryptography/ECC memory.md:3`
- Target: `[[Tampering]]` (`content/domains/computer-science/cryptography/Tampering.md`)
- Reason: The sentence uses tampering in the security sense while discussing Rowhammer mitigation.

Current:
> Error Correcting Code Memory (ECC memory) is supposedly resilient to [[Rowhammer]] attacks. ECC memory detects bit tampering and amazingly corrects the change. This would seem to be an effective mitigation.

Suggested:
> Error Correcting Code Memory (ECC memory) is supposedly resilient to [[Rowhammer]] attacks. ECC memory detects bit [[Tampering|tampering]] and amazingly corrects the change. This would seem to be an effective mitigation.

### D9 - medium-high
- Source: `content/domains/computer-science/cryptography/ENTROPY.md:4`
- Target: `[[Cryptography]]` (`content/domains/computer-science/cryptography/Cryptography.md`)
- Reason: The opening definition explicitly situates entropy inside cryptography.

Current:
> Entropy is a measure of randomness or unpredictability in information systems. In cryptography, it represents the amount of uncertainty in a random variable or the quality of randomness available for cryptographic operations.

Suggested:
> Entropy is a measure of randomness or unpredictability in information systems. In [[Cryptography|cryptography]], it represents the amount of uncertainty in a random variable or the quality of randomness available for cryptographic operations.

## Cross-Domain Candidates

### C1 - high
- Source: `content/research/entropy-vikalpa/Comprehensive_Shannon_Entropy_Vikalpa_Research.md:5`
- Target: `[[Entropy]]` (`content/domains/computer-science/cryptography/ENTROPY.md`)
- Reason: Research note names Shannon Entropy as one side of the bridge; ENTROPY is the durable cryptography/information-theory concept note.

Current:
> This document presents comprehensive research into the potential connections between Shannon Entropy from information theory and Vikalpa from the Yoga Sutras.

Suggested:
> This document presents comprehensive research into the potential connections between [[Entropy|Shannon Entropy]] from information theory and Vikalpa from the Yoga Sutras.

### C2 - high
- Source: `content/research/entropy-vikalpa/Comprehensive_Shannon_Entropy_Vikalpa_Research.md:5`
- Target: `[[Vikalpa]]` (`content/domains/humanities/sanskrit-literature/Vikalpa.md`)
- Reason: Research note names Vikalpa as the other side of the bridge; Vikalpa is the durable Sanskrit/Yoga concept note.

Current:
> This document presents comprehensive research into the potential connections between Shannon Entropy from information theory and Vikalpa from the Yoga Sutras.

Suggested:
> This document presents comprehensive research into the potential connections between Shannon Entropy from information theory and [[Vikalpa]] from the Yoga Sutras.

### C3 - high
- Source: `content/research/entropy-vikalpa/Entropy_Vikalpa_Research_Abstract.md:6`
- Target: `[[Entropy]]` (`content/domains/computer-science/cryptography/ENTROPY.md`)
- Reason: The abstract frames Shannon entropy as the information-theory anchor for the research.

Current:
> This research investigates the relationship between Shannon entropy from information theory and vikalpa (mental alternatives) from Patanjali's Yoga Sutras, proposing the first systematic mathematical framework bridging 2,500-year-old consciousness analysis with contemporary neuroscience.

Suggested:
> This research investigates the relationship between [[Entropy|Shannon entropy]] from information theory and vikalpa (mental alternatives) from Patanjali's Yoga Sutras, proposing the first systematic mathematical framework bridging 2,500-year-old consciousness analysis with contemporary neuroscience.

### C4 - high
- Source: `content/research/entropy-vikalpa/Entropy_Vikalpa_Research_Abstract.md:6`
- Target: `[[Vikalpa]]` (`content/domains/humanities/sanskrit-literature/Vikalpa.md`)
- Reason: The abstract defines vikalpa directly and should point to the concept note.

Current:
> This research investigates the relationship between Shannon entropy from information theory and vikalpa (mental alternatives) from Patanjali's Yoga Sutras, proposing the first systematic mathematical framework bridging 2,500-year-old consciousness analysis with contemporary neuroscience.

Suggested:
> This research investigates the relationship between Shannon entropy from information theory and [[Vikalpa|vikalpa]] (mental alternatives) from Patanjali's Yoga Sutras, proposing the first systematic mathematical framework bridging 2,500-year-old consciousness analysis with contemporary neuroscience.

### C5 - medium-high
- Source: `content/research/entropy-vikalpa/Entropy_Vikalpa_Research_Abstract.md:32`
- Target: `[[YogaSutras]]` (`content/domains/humanities/sanskrit-literature/yoga_sutras/YogaSutras.md`)
- Reason: The narrative abstract names Yoga Sutras as the source tradition; a YogaSutras note exists.

Current:
> The human capacity for conceptual thinking—what the ancient Yoga Sutras term "vikalpa" or mental alternatives—has remained largely unmeasured by modern science despite its central role in consciousness and cognitive flexibility.

Suggested:
> The human capacity for conceptual thinking—what the ancient [[YogaSutras|Yoga Sutras]] term "vikalpa" or mental alternatives—has remained largely unmeasured by modern science despite its central role in consciousness and cognitive flexibility.

## Review Notes
- I excluded generic or noisy candidates such as `README`, `INDEX`, `test`, bibliography-only `Sutra` matches, and heading-only links.
- I would apply high-confidence candidates first. Medium-high candidates are still plausible but worth manual review.
- Existing `ENTROPY.md` and `Vikalpa.md` already link to each other, so this dry run does not duplicate that connection.
