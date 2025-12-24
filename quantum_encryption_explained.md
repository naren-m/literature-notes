# How Quantum Computers Break Encryption: First Principles

[Jira confluence page](https://miggbo.atlassian.net/wiki/x/IwieVg)
- ## The Core Problem: Why Do We Need New Cryptography?
- ### Today's internet security relies on "hard math problems"
  
  When you visit a website securely (HTTPS), two things happen:
  
  1. **Key Agreement** – You and the server secretly agree on a shared password that nobody else knows
  2. **Authentication** – You verify you're actually talking to the real server, not an imposter
  
  Both rely on mathematical problems that are *extremely hard* for regular computers to solve (like factoring huge numbers). This hardness is what keeps your data safe.
  
  ---
- ### Quantum computers break these specific hard problems
  
  Quantum computers aren't "faster regular computers." They're fundamentally different machines that use quantum physics (superposition, entanglement) to solve *certain specific problems* exponentially faster.
  
  Unfortunately, the math problems protecting today's internet (RSA, elliptic curves) fall into that category. A sufficiently powerful quantum computer can crack them easily using something called **Shor's algorithm**.
  
  ---
- ### Encrypted data can be stored forever ("Harvest Now, Decrypt Later")
  
  Here's the scary part: An attacker can *record* your encrypted traffic today. It looks like gibberish now. But once quantum computers become powerful enough ("Q-day"), they can decrypt that old data.
  
  So if you send something sensitive today (medical records, trade secrets, government communications), it could be exposed 10-15 years from now.
  
  ---
- ### Use math problems that even quantum computers can't solve
  
  Cryptographers have found new mathematical foundations that resist quantum attacks:
- **[[Lattice-based encryption]]** (most popular today)
- **Hash-based**
- **Code-based**
- **Others**
  
  These have been studied for decades. NIST (US standards body) has now standardized specific algorithms:
- **ML-KEM** for key agreement
- **ML-DSA, SLH-DSA, FN-DSA** for signatures
  
  ---
- ### Key agreement and signatures have different urgency
  
  | | Key Agreement | Signatures/Certificates |
  |----|----|----|
  | **Threat** | Harvest-now-decrypt-later | Only vulnerable on Q-day |
  | **Urgency** | **Urgent NOW** | Less urgent, but harder |
  | **Difficulty** | Easy (software update) | Hard (bigger data, ecosystem changes) |
  
  **Key Agreement migration is mostly done!** Over 50% of internet traffic now uses post-quantum key agreement (X25519 + ML-KEM-768 hybrid).
  
  **Signatures are the hard part.** The new algorithms produce much larger signatures (~15KB vs ~100 bytes), creating performance/compatibility issues.
  
  ---
- ## Two Ways to Break Cryptography
  
  | Attack Type | How it works | Quantum Advantage |
  |----|----|----|
  | **Exploit the math structure** | Find a shortcut in the algorithm's design | **Massive** (Shor's algorithm) |
  | **Brute force** | Try every possible key until one works | **Modest** (Grover's algorithm) |
  
  ---
- ## Why RSA/ECC Breaks: Mathematical Structure
  
  RSA is based on this problem:
  
  > Given a very large number N, find the two prime numbers that multiply to make N.
  
  **Classical computers:** Must essentially try dividing by primes one by one. Takes astronomical time.
  
  **Quantum computers:** Shor's algorithm exploits the **mathematical structure** of multiplication/factoring. It's like finding a secret backdoor in the math itself.
  
  ---
- ## Why AES Doesn't Break: No Structure to Exploit
  
  AES is fundamentally different. It's designed to be a **"random-looking" scrambler**.
  
  ```
  Key + Data → [Scramble, Mix, Substitute, Repeat 14 times] → Ciphertext
  ```
  
  There's no mathematical relationship between input and output that can be exploited. The only way to break it:
  
  > **Try every possible key until you find the right one**
  
  ---
- ## Example: Breaking a Hypothetical AES-16
  
  AES-16 would mean a 16-bit key = 2¹⁶ = **65,536 possible keys**
- ### Classical Attack
  
  ```
  Try key 0000000000000000 → Decrypt → Garbage? Next.
  Try key 0000000000000001 → Decrypt → Garbage? Next.
  Try key 0000000000000010 → Decrypt → Garbage? Next.
  ...
  (worst case: 65,536 attempts)
  ```
  
  Average: ~32,768 tries. A laptop does this in milliseconds.
- ### Quantum Attack (Grover's Algorithm)
  
  Grover's provides a square-root speedup:
- Classical: 2¹⁶ = 65,536 tries
- Quantum: √(2¹⁶) = 2⁸ = **256 tries**
  
  Faster, but same fundamental approach — still just guessing keys.
  
  ---
- ## Scaling Up: Why AES-256 is Safe
  
  | Key Size | Classical Attempts | Quantum Attempts (Grover) |
  |----|----|----|
  | AES-16 (hypothetical) | 65,536 | 256 |
  | AES-128 | 2¹²⁸ ≈ 10³⁸ | 2⁶⁴ ≈ 10¹⁹ |
  | AES-256 | 2²⁵⁶ ≈ 10⁷⁷ | 2¹²⁸ ≈ 10³⁸ |
  
  Even with Grover's speedup:
- **2⁶⁴ operations** is borderline feasible (decades of work)
- **2¹²⁸ operations** is completely impossible (more operations than atoms in the universe)
  
  ---
- ## The Key Insight
  
  ```
  RSA/ECC:  Quantum finds a SHORTCUT through the math
          (like finding a secret tunnel through a mountain)
  
  AES:      Quantum just searches FASTER
          (like running instead of walking, but still must
           check every house in a city of 10³⁸ houses)
  ```
  
  ---
- ## Simple Analogy
  
  | Algorithm | Analogy |
  |----|----|
  | **RSA** | A combination lock where quantum computers figured out you can hear the clicks |
  | **AES** | A combination lock with no clicks, no hints — pure guessing, just slightly faster guessing |
  
  ---
- ## Bottom Line
  
  **AES-256 is quantum-safe** because even "slightly faster guessing" doesn't help when there are 2²⁵⁶ possibilities.
  
  The quantum threat is specifically about **key exchange** (RSA/ECC), not about **data encryption** (AES).
  
  ---
- ## Symmetric vs Asymmetric Summary
  
  | Type | Example | How it works | Quantum Threat |
  |----|----|----|----|
  | **Symmetric** | AES | Same key on both sides | **Safe** ✅ |
  | **Asymmetric** | RSA, ECC | Public/private key pair | **Broken** by Shor's algorithm ❌ |
  
  ---
  
  Source: [Post-Quantum Cryptography](https://blog.cloudflare.com/pq-2025/)