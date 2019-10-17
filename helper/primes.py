from math import sqrt


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def primesList(limit):
    crosslimit = sqrt(limit)
    sieve = []
    result = []

    n = 1
    for n in range(limit):
        sieve.append(False)

    n = 4
    for n in range(n, limit, 2):
        sieve[n] = True

    n = 3
    for n in range(n, int(crosslimit), 2):
        if not sieve[n]:
            m = n * n
            for m in range(m, limit, 2 * n):
                sieve[m] = True

    n = 2
    for n in range(n, limit, 1):
        if not sieve[n]:
            result.append(n)

    return result


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    for p in range(3, int(n), 2):
        if n % p == 0 and is_prime(p):
            factors.append(p)
    if is_prime(int(n)):
        factors.append(int(n))
    return factors


def consecutive(l):
    c = 1
    consec = []
    while len(consec) < l:
        primes = set(prime_factors(c))
        if len(primes) == l:
            consec.append(c)
        else:
            consec = []
        c += 1
    print(consec)


def SieveOfEratosthenes(limit):
    limitn = limit + 1
    primes = dict()
    for i in range(2, limitn):
        primes[i] = True

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i] == True]
