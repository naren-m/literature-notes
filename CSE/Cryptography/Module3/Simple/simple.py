import hashlib

from hashlib import sha256

message=b'42'
hashobj=hashlib.new('sha256')
hashobj.update(message)
print(hashobj.hexdigest())
