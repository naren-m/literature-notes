from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)
data_encrypted = f.encrypt(
    b"So long and thanks for all the business")

#temp=format(int.from_bytes(data_encrypted, byteorder ='big'), 'X')
#(temp)
print(data_encrypted)
data_decrypted=f.decrypt(data_encrypted)
print(data_decrypted)
