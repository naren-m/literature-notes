# Message Authentication Code (MAC)

A MAC verifies both the [[Integrity]] and Identification of a message.
The MAC consists of a keyed hash. This is a hash seeded with a [[private key]]
There are three aspects of a Mac:
- Creating a [[private key]]
- Signing a hash
- Verifying the MAC