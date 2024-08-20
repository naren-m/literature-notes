import hashlib # hashlib module
import os.path # For file handling
from os import path
 
hash = hashlib.sha256()
 
file=open('c:\Code\Python\cryptography\Module3\streaming\\readme.md','rb')
chunk=''
while True:
    chunk = file.read(512) 
    if chunk == b'':
        break
    hash.update(chunk)

hash_value=hash.hexdigest()
print(hash_value)

file.close()