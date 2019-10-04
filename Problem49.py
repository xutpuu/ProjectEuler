# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

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


def orderStr(n):
    s = str(n)
    return "".join(sorted(s))


def sequence(n):
    lim = 10 ** n
    primes = pr.primesList(lim)
    for i in primes:
        if (
            i + 3330 in primes
            and i + 6660 in primes
            and orderStr(i) == orderStr(i + 3330) == orderStr(i + 6660)
        ):
            print(str(i) + str(i + 3330) + str(i + 6660))


@benchmark
def main():
    sequence(4)


if __name__ == "__main__":
    main()
