#!/usr/bin/python -i

from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

Local = True

if Local:
    host = '127.0.0.1'
    port = 2323
else:
    import sys
    default_host = '192.168.122.233'
    host = sys.argv[1] if len(sys.argv) > 1 else default_host
    port = 2303


def xgcd(x, y):
    a1, a2 = 1, 0
    b1, b2 = 0, 1
    c1, c2 = x, y
    while c2 != 0:
        d = c1//c2
        a1, a2 = a2, a1-d*a2
        b1, b2 = b2, b1-d*b2
        c1, c2 = c2, c1-d*c2
    return c1, a1, b1


def solve(b, m, c):
    # for i in xrange(m):
    #    if (i*b) % m == c:
    #        res = i
    #        break
    g, c1, _ = xgcd(b, m)
    # b*c1 == g
    assert c % g == 0
    q = c//g
    res = (c1*q) % m
    assert (res*b-c) % m == 0
    return res


r = remote(host, port)

print r.recvline()
for i in range(1000):
    s = r.recvuntil('x =')
    s = s.split(',')[0].split('*')[1].strip()
    v1 = s.split(')')[0]
    l = s.split()
    v2 = l[2]
    v3 = l[4]
    print v1, v2, v3
    r.sendline(str(solve(int(v1), int(v2), int(v3))))


pl = ''

r.send(pl)
raw_input('continue ->')
pl = ''

r.interactive()
