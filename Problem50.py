# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import helper.primes as pr


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print("[*] Total time taken: {} sec.".format(end - start))
        return return_value

    return wrapper


@benchmark
def main():
    limit = 1000000
    primes = pr.SieveOfEratosthenes(limit)
    num = []

    for p in primes:
        num.append(p)

    l = len(num)

    largest = 0
    length = 0
    lastj = l

    print("start")
    for i in range(l):
        for j in range(i + length, lastj):
            sol = sum(num[i:j])
            if sol < limit:
                if sol in primes:
                    length = j - i
                    largest = sol
            else:
                lastj = j + 1
                break
    print(largest)


if __name__ == "__main__":
    main()
