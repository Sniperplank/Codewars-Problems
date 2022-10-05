# Probelm Description
"""
A twin prime is a prime number that is either 2 less or 2 more than another prime number—for example, either member of the twin prime pair (41, 43). In other words, a twin prime is a prime that has a prime gap of two. Sometimes the term twin prime is used for a pair of twin primes; an alternative name for this is prime twin or prime pair. (from wiki https://en.wikipedia.org/wiki/Twin_prime)

Your mission, should you choose to accept it, is to write a function that counts the number of sets of twin primes from 1 to n.

If n is wrapped by twin primes (n-1 == prime && n+1 == prime) then that should also count even though n+1 is outside the range.

Ex n = 10

Twin Primes are (3,5) (5,7) so your function should return 2!
"""

# Output Examples
"""
N/A
"""

# Problem Solution

import math
def twin_prime(n):
    primes = []
    sets = []
    for i in range(3, n):
        if i % 2 == 1:
            if is_prime(i):
                primes.append(i)
    for x in primes:
        if is_prime(x + 2):
            sets.append([x, x+2])
    return len(sets)
    
def is_prime(y):
    for x in range(2, int(math.sqrt(y))+1):
        if y % x == 0:
            return False
    return True
