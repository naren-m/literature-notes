# Block Cipher

A block cipher is a symmetric [[Encryption]] primitive in [[Cryptography]] that decomposes the input and processes one chunk (block) at a time.

The algorithm processes the blocks in order.
Basically, a block takes nibbles instead of eating an entire meal at one.

Would you like to add some salt to that sandwich? You can always seed your input with a unique value. When mixed in with normal [[Hashing]], this adds another level of unpredictability.

Block cipher modes such as CBC often depend on an [[Initialization Vector]] so repeated plaintext does not produce repeated ciphertext.

![Block Cipher](images/BlockCipher.png)
