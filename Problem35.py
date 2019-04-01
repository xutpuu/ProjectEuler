# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

import math


def countDigits(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt


def primesList(limit):
    crosslimit = math.sqrt(limit)
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


def main():
    rez = []
    limits = 1000000
    primes = primesList(limits)
    for num in primes:
        digit = countDigits(num)
        powTen = pow(10, digit - 1)
        count = 0
        for i in range(digit - 1):
            firstDigit = num // powTen
            left = num * 10 + firstDigit - (firstDigit * powTen * 10)
            num = left
            if left in primes:
                count += 1
        if count > 0 and count == digit - 1:
            rez.append(num)

    print(len(rez))


if __name__ == "__main__":
    main()
