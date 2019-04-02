# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
import math
import time as t


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
    start = t.time()
    primes = primesList(100000000)
    print(len(str(primes[-5])))
    # for prime in primes:
    #     if len(str(prime)) == 10:
    #         print(prime)
    end = t.time()
    print("Total time taken:", end - start, "ms")

if __name__ == "__main__":
    main()
