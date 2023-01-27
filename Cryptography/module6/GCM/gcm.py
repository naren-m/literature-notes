from Crypto.Cipher import AES

data=b'42'
key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_GCM)

nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
try:
    cipher.verify(tag)
    print("The message is authentic:", plaintext)
except ValueError:
    print("Key incorrect or message corrupted")
