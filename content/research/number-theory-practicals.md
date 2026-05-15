---
title: "Number Theory Practicals"
date: 2020-05-26
type: research
category: "Math/number-theory"
tags: [math, number-theory, divisibility, primes, gcd, lcm]
status: incomplete
source: "Notion Notes DB, companion to a YouTube number-theory series"
related: [logarithms]
---

# Number Theory Practicals

Working notes on elementary number theory — subsets of numbers, divisibility, primes, GCD/LCM, unit-digit tricks. Captured alongside a YouTube number-theory series.

## Subsets of numbers

- **Integers** — `..., -2, -1, 0, 1, 2, ...`
- **Whole numbers** — non-negative integers.
- **Natural numbers** (counting numbers) — `1, 2, 3, ...`

## Even, odd, perfect squares

- **Even**: `2k`.
- **Odd**: `2k + 1`.
- **Perfect square**: `k²`.

## Pythagorean triplets

Three positive integers `a, b, c` such that `a² + b² = c²`. Smallest example: `(3, 4, 5)`.

## Divisibility

**Definition.** `a` divides `b` if `b / a` leaves no remainder.

### Divisibility rules

- **By 0**: divisible by all non-zero integers (though division *by* 0 is undefined).
- **By 2**: last digit is even.
- **By 4 (= 2²)**: last two digits divisible by 4.
- **By 8 (= 2³)**: last three digits divisible by 8.
- **By 3**: sum of digits divisible by 3.
- **By 9**: sum of digits divisible by 9.
- **By 5**: last digit is 0 or 5.
- **By 10**: last digit is 0.
- **By 6**: divisible by both 2 and 3.
- **By 12**: divisible by both 3 and 4.

*Sample problem*: `12A3B` is divisible by both 4 and 9; `A ≠ B`. Find `A`. *(Answer from notes: A=1, B=2.)*

## Primes

- **Prime**: natural number with exactly two positive divisors (1 and itself).
- **Composite**: natural number with more than two positive divisors.
- **Relatively prime**: two numbers whose only positive common divisor is 1. Example: `8` and `13` are coprime; `13` and `26` are not.
- **`1` is neither prime nor composite** — divisors aren't distinct.

### Sieve of Eratosthenes

List `1..N`, cross out multiples of each prime starting from 2. To check whether `n` is prime, only test primes up to `√n`.

### Useful facts

- Only even prime: **`2`**.
- `n² − n + 41` generates primes for `n = 1..40` (not for `n = 41`).
- **Goldbach's conjecture**: every even integer `> 4` is the sum of two primes. *(A conjecture is a statement that seems to hold but hasn't been proven.)*

### Sample problems

- Smallest composite coprime to both 30 and 91 — requires finding a composite whose prime factors avoid `{2,3,5,7,13}`; smallest is `121 = 11²`.
- Smallest composite not divisible by the first 8 primes (`2,3,5,7,11,13,17,19`): `23² = 529`.

## Greatest Common Divisor (GCD)

"Greatest" means the *largest* divisor common to both numbers.

### Euclidean algorithm

`gcd(a, b) = gcd(min(a,b), |a − b|)` — repeated subtraction (or, more efficiently, repeated remainder).

*Example*: `gcd(180, 270) = gcd(180, 90) = gcd(90, 90) = 90`.

## Least Common Multiple (LCM)

"Least" means the *smallest* common multiple.

**Method**: prime-factor both numbers; for each prime that appears, take the *highest* power.

*Example*: `lcm(84, 270)`. `84 = 2²·3·7`, `270 = 2·3³·5`. LCM = `2²·3³·5·7 = 3780`.

Another trick: for the *least perfect-square common multiple* of 3 and 8, raise each prime factor to an even power: `9 · 16 = 144`.

## Relationship between GCD and LCM

For positive integers `a, b, c`:

- `gcd(ac, bc) = c · gcd(a, b)`
- `lcm(ac, bc) = c · lcm(a, b)`
- **`a · b = gcd(a,b) · lcm(a,b)`** — the key identity.

*Example*: `gcd(800, 1800) = 200 · gcd(4, 9) = 200 · 1 = 200`; `lcm(800, 1800) = 200 · lcm(4, 9) = 200 · 36 = 7200`. Check: `800 · 1800 = 1,440,000 = 200 · 7200`. ✓

**Intuition**: GCD is the product of common prime factors raised to the *lowest* shared power; LCM is the product of all prime factors raised to the *highest* power seen in either number.

## Number of factors

If `n = p₁^a · p₂^b · p₃^c · ...`, then the total number of divisors is `(a+1)(b+1)(c+1)...`.

*Example*: `200 = 2³ · 5²` → `(3+1)(2+1) = 12` divisors.

**Even divisors of 168**: `168 = 2³·3·7`. Force at least one factor of 2: don't add 1 to the exponent of 2. Count = `3 · (1+1) · (1+1) = 12`.

## Unit digits and last two digits

- `2ⁿ` unit digits cycle with period 4: `2, 4, 8, 6, 2, 4, 8, 6, ...`
- Unit digit of `a^n` depends only on unit digit of `a` and `n mod 4` (or cycle length for the particular base).
- **Perfect-square unit digits**: only `0, 1, 4, 5, 6, 9` (never `2, 3, 7, 8`).
- **Unit digit of `n!`**: for `n ≥ 5`, always `0` (contains `2 × 5`).

## Related

- [[logarithms]] — exponents and log identities lean on the same multiplicative structure.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/0aeea30c5cdb40f5bcda37782c078c6e). See [[notion-migration]].*
