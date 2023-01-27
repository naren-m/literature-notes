# Checksum

Checksums are created to provide data integrity but are considered lightweight hashes. Not every target of hashing requires a security-level hash, such as SHA-256.
Checksums are a highly performant and insecure hash.

Checksum -> Integrity

Checksums are used to validate the [[Integrity]] of the data.

[[Hashing]] is different than Checksum.


LOST BITS
Lost of bits during some sort of transformation is a frequent scenario for employing checksums.
- Compressing / Decompression
- Network transmission
- File transfer
- Data transformation
Note that these use cases do not raise security issues. Nonetheless, [[Integrity]] is still required.

MD5 should be enough.