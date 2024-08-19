# pip install bcrypt

import bcrypt  

password = "password"
 
password = password.encode('utf-8')

# salt = bcrypt.gensalt(rounds=16)
 
hashedPassword = bcrypt.hashpw(password, salt)

print(hashedPassword)

if bcrypt.checkpw(password, hashedPassword):
    print("Matched")
else:
    print("Not matched")