# pip install bcrypt

import bcrypt  

password = "password"
 
password = password.encode('utf-8')
 
hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashedPassword)

#password="xyz"
#password=password.encode('utf-8')

if bcrypt.checkpw(password, hashedPassword):
    print("Matched")
else:
    print("Not matched")