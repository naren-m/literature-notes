from cryptography.fernet import Fernet, MultiFernet

key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())
f = MultiFernet([key1, key2])

token = f.encrypt(b"Secret message!")
print(token)
result=f.decrypt(token)
print(result)

key3 = Fernet(Fernet.generate_key())
f2 = MultiFernet([key3, key2, key1])
rotated = f2.rotate(token)
print(rotated)
result=f2.decrypt(rotated)
print(result)