from hashlib import sha256

message=b'42'
first_sha=sha256(message)
temp=bin(int.from_bytes(
	first_sha.digest(), 'big'))
double_sha=sha256(temp.encode('utf-8'))

result=double_sha.hexdigest();
print(result)