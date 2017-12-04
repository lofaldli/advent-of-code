import hashlib
from aocd import data

def md5(secret, salt):
    return hashlib.md5(secret.encode() + b'%d' % (salt)).digest()


def solve(secret, target):
    for salt in range(10000000):
        hash = ''.join([format(x, '02x') for x in md5(secret, salt)])
        if hash[:len(target)] == target:
            return salt

print('part 1:', solve(data, '00000'))
print('part 2:', solve(data, '000000'))
