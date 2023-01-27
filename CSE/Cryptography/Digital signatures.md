# Digital signatures

Digital Signature = [[Hashing]] + [[Encryption]] (encrypted with Private key and decrypted by Public key)
- Use asymmetric encryption.
- Sender creates a digital signature while the receiver verifies the signature.
- Does NOT provide Confidentiality

Digital signatures are a combination of hashing and encryption to verify the identity of a sender and integrity of the message.

Digital signatures potentially defend against several vulnerabilities in [[STRIDE]]:
- Spoofing
- Tampering
- Repudiation

Digital signatures are a combination of hashing and encryption. This potentially resolves several vulnerabilities identified within STRIDE:
- Spoofing
- Tampering
- Information disclosure*
- Repudiation


## Sender

Digital signatures are useful for sending data securely with identity. It is a combination of a hash and asymmetric encryption.
Here are the steps to create a digital signature for a message / data:
1. Create a hash of the message
2. Encrypt the hash with the private key. The result is a digital signature.
3. Send the digital signature to the receiver with the message


## Receiver

The recipient receives the signature and plaintext. Before using the plaintext, verify the signature.
1. Hash (hash 1) the plaintext
2. Decrypt the signature and extricate the hash (hash 2)
3. Compare the two hashes. If the same, the signature has been verified.