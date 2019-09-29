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
