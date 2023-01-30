msg = 'Hello, world'
digest = hash(msg)

print('Digest {}, Digest in hex {}'.format(digest, format(digest, 'X')))