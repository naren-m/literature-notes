# HMAC

HMAC is a hash that is seeded with a secret key. The two elements of HMAC.
• Hashing algorithm
• Authentication
HMAC can use a variety of hashing algorithms:

md5 --- sha1
sha224 --- sha256
sha384 --- black2b
black2s --- and others

Here is the implementation for HMAC in Python.
Call the hmac.new function to great new hashing used the password and the designated hashing algorithm.
hmac.new(plaintext, password, hashing algorithm)
import hashlib import hmac
hmac1 = hmac.new(b'info 1', b'1234', hashlib.md5)
hmac2 = hmac.new(b'info 2', b'1234', hashlib.sha1)
print("MD5", hmac1.hexdigest())
print("SHA1", hmac2.hexdigest())