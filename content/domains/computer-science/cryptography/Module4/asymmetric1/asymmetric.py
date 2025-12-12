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

encrypted = encryptor.encrypt(b'encrypt this message')

decryptor = PKCS1_OAEP.new(privatekey)
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))
print(decrypted)
