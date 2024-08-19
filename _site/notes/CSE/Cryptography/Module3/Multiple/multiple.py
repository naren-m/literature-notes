from hashlib import sha256

message=b'42'
hashobj1=sha256(message)
result=hashobj1.hexdigest();
print(result)

message=b'4'
hashobj2=sha256(message)
hashobj2.update('2'.encode('ascii')  )
result=hashobj2.hexdigest();
print(result)






