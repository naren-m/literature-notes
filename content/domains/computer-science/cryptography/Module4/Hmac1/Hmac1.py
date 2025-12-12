import hashlib
import hmac

hmac1 = hmac.new(b'info 1', b'1234', hashlib.md5)
hmac2 = hmac.new(b'info 2', b'1234', hashlib.sha1)

print("MD5", hmac1.hexdigest())
print("SHA1", hmac2.hexdigest())