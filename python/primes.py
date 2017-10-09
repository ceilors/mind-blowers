#!/usr/bin/env python
import sys
from itertools import count


def sieve():
    primes = []
    for n in count(start=2):
        prime = True
        for p in primes:
            if n % p == 0:
                prime = False
                break
        if prime:
            primes.append(n)
            yield n


def primes_less_than(n):
    primes = []
    for p in sieve():
        if p > n:
            break
        primes.append(p)
    return primes


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(primes_less_than(int(sys.argv[1])))