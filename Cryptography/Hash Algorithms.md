# Hash Algorithms

A [[Hash Algorithms]] will convert variable length data into a fixed length encoded result, which is called a digest. Any change to the data, even a single bit, can cause a radically different digest being generated using the hash algorithm.
Here are the attributes of a secure hash algorithm:
- One way – must use brute force to reverse
- Should be fast
- Memory efficient

## One-way:
as mentioned [[Hashing]] algorithms are one way.

## Collision resistant:
it is unlikely, if not impossible, for an attacker to uncover collision, where two inputs have the same hash.

## Performant
hashes must be highly performant. Slow hashes are hard to scale which is necessary for many use cases.

[[Hashing]] algorithms are also referred to as ciphers, where block ciphers are the most common. There are various approaches to creating hashes:
- Block cipher
- Stream cipher
- Keyed hash

Hash Algorithms: SHA256(Good balance between compute and security), SHA512(more compute intense)
At present, the most common hashing algorithm is SHA-256.

SHA-256 is a member of the SHA 2 family of algorithms and creates a 256-bit digest.
For example, SHA-384 and SHA-512 are also included in the SHA 2 family.
Although more secure, there is a performance trade-off when using SHA-384 and SHA-512.
SHA-3 is available but not widely used.
