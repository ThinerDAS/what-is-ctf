#!/usr/bin/python -u
"""
python -u provide easy way of unbuffered IO
"""

"""
for sys.stderr
"""
import sys

"""
str.split() will split the string into "words". It returns a list of words.
Example:
>>> '1003 + 136 = '.split()
['1003', '+', '136', '=']
>>> '1003 + 136 = '.split()[:3]
['1003', '+', '136']
"""
a, _, b = raw_input().split()[:3]

"""
Sometimes debug information is valuable.
Things printed at stderr can not be seen by peer, rather it would be seen by you!
Print diagnostic messages and flags here!
"""
print >>sys.stderr, 'a =', repr(a)
print >>sys.stderr, 'b =', repr(b)

"""
`a` and `b` are strings, so transform them into int, then do addition, and send it to server.
"""
ans = int(a) + int(b)
print >>sys.stderr, 'ans =', repr(ans)
print ans

"""
See peer's response.
"""
while True:
    print >>sys.stderr, raw_input()
