# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
import math


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print("[*] Total time taken: {} sec.".format(end - start))
        return return_value

    return wrapper


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


def countDigits(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt


def isUnusual(num):
    sorted_str = "".join(sorted(num))
    if sorted_str == "1234567":
        return True
    else:
        return False


def pandigital():
    m = 0
    primes = primesList(100000000)
    for i in primes:
        if isUnusual(str(i)) and i > m:
            m = i
    print(m)


@benchmark
def main():
    print("Begin")
    pandigital()


if __name__ == "__main__":
    main()
