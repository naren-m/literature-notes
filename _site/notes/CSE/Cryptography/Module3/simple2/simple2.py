from hashlib import sha256

message=b'42'

hashobj=sha256(message)

result=hashobj.hexdigest();

print(result)

