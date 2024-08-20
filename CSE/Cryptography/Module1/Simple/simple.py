message='Hello, world!'

digest=hash(message)

#result=hex(digest)

result=format(digest, 'X')

print(result)
