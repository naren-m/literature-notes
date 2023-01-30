import hashlib
from hashlib import sha256
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast


def get_hash(value):
    hashobj=hashlib.new('sha256')
    hashobj.update(value)
    return hashobj.digest()

def generate_keys():
	modulus_length = 256*4
	privatekey = RSA.generate(modulus_length, Random.new().read)
	publickey = privatekey.publickey()
	return privatekey, publickey

def encrypt_data(key, plaintext):
    encryptor = PKCS1_OAEP.new(key)
    encrypted = encryptor.encrypt(plaintext)
    return encrypted

def decrypt_data(key, ciphertext):
    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(ast.literal_eval(str(ciphertext)))
    return decrypted


data=b'42'
hash1=get_hash(data)


privatekey, publickey=generate_keys()
encrypted=encrypt_data(publickey, hash1)


hash2=get_hash(data)

hash3=decrypt_data(privatekey, ast.literal_eval(str(encrypted)))


if hash2==hash3:
    print("Verified")
else:
    print("Not Verified")
