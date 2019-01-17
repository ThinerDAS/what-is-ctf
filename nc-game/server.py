#!/usr/bin/python -u
"""
python -u provide easy way of unbuffered IO
"""

"""
random.randint(start, end) generate random integer between interval [start, end]
"""
import random
a = random.randint(3,1111)
b = random.randint(3,1111)

"""
Anything printed to stdout will be sent to peer.
"""
print a, '+', b, '='

"""
`raw_input()` gets a line from stdin, so it is the peer's response.
Notice that sometimes `raw_input(prompt_string)` is used. Try out yourself by putting a string inside the argument and see the result.
int(string_of_integer) transform the string into int
"""
x = int(raw_input())

"""
If peer has finished your goal, give them the prize.
"""
if x == a+b:
    print 'Correct! flag is flag{1234567890}'

