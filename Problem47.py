# The first two consecutive numbers to have two distinct prime factors are:

#       14 = 2 × 7
#       15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

#       644 = 2² × 7 × 23
#       645 = 3 × 5 × 43
#       646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
from helper.primes import prime_factors


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print("[*] Total time taken: {} sec.".format(end - start))
        return return_value

    return wrapper


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

@benchmark
def main():
    consecutive(4)

if __name__ == "__main__":
    main()
