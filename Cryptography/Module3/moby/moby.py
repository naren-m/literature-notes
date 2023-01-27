import zlib

prev_checksum=2789716996

fileObj= open("C:\Code\Python\cryptography\Module3\moby\Test.txt", "r")
fileText=fileObj.read()

checksum=zlib.crc32(bytes(fileText, 'UTf-8'))

if prev_checksum!=0:
    if checksum == prev_checksum:
        print("Verified")
    else:
        print("Not verified!")

fileObj.close()
 
print(fileText)
print(checksum)