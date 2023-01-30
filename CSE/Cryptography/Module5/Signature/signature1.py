from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

from Crypto import Random

def generate_keys():
	modulus_length = 256*4
	privatekey = RSA.generate(modulus_length, Random.new().read)
	publickey = privatekey.publickey()
	return privatekey, publickey


privatekey, publickey=generate_keys()
message = b'To be signed'

h = SHA256.new(message)
signature = pkcs1_15.new(privatekey).sign(h)


h2 = SHA256.new(message)
try:
	pkcs1_15.new(publickey).verify(h2, signature)
	print("The signature is valid.")
except (ValueError, TypeError):
	print("The signature is not valid.")