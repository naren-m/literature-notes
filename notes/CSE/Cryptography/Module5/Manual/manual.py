import hashlib
from hashlib import sha256

message=b'42'
hashobj=hashlib.new('sha256')
hashobj.update(message)
#print(hashobj.hexdigest())


from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast

def generate_keys():
	modulus_length = 256*4
	privatekey = RSA.generate(modulus_length, Random.new().read)
	publickey = privatekey.publickey()
	return privatekey, publickey


privatekey, publickey=generate_keys()

encryptor = PKCS1_OAEP.new(publickey)

encrypted = encryptor.encrypt(hashobj.digest())


message=b'42'
hashobj2=hashlib.new('sha256')
hashobj2.update(message)
print(hashobj2.hexdigest())


decryptor = PKCS1_OAEP.new(privatekey)
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

print(hashobj2.digest())
print(decrypted)

if decrypted==hashobj2.digest():
    print("Verified")
else:
    print("Not Verified")
