#!/usr/bin/python -u

import random
import signal


def ri(i):
    return random.randint(1, 10+long(1.5**i))


def alarm_handler(x, y):
    print 'Time out! See you next time~'
    exit()


if __name__ == '__main__':
    signal.signal(signal.SIGALRM, alarm_handler)
    print "Solve equations for fun & profit! ^O^"
    for i in range(1000):
        signal.alarm(1+30//(i+1))
        while True:
            m = ri(i)
            a = ri(i) % m
            b = ri(i) % m
            c = (a*b) % m
            if c != 0:
                break
        s = long(raw_input('(x * {:d}) % {:d} == {:d}, x = '.format(b, m, c)))
        if (s*b-c) % m != 0:
            print 'Incorrect, Bye'
            exit()
    signal.alarm(0)
    print 'Congratulations, you solved all my equations, and here is your flag. Flag is heavy, be careful:'
    with open('flag') as f:
        print f.read()
