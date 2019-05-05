# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each
# of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d₁ be the 1ˢᵗ digit, d₂ be the 2ⁿᵈ digit, and so on. In this way, we note the following:

# d₂d₃d₄=406 is divisible by 2
# d₃d₄d₅=063 is divisible by 3
# d₄d₅d₆=635 is divisible by 5
# d₅d₆d₇=357 is divisible by 7
# d₆d₇d₈=572 is divisible by 11
# d₇d₈d₉=728 is divisible by 13
# d₈d₉d₁₀=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print("[*] Total time taken: {} sec.".format(end - start))
        return return_value

    return wrapper


def isUnusual(num):
    sorted_str = "".join(sorted(num))
    if sorted_str == "0123456789":
        return True
    else:
        return False


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

def convert(list): 
    s = [str(i) for i in list] 
    res = int("".join(s)) 
    return(res) 

@benchmark
def main():
    print("Begin")
    pandigital = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    l = all_perms(pandigital)
    n = 0
    for i in l:
        if (
            (i[1] * 100 + i[2] * 10 + i[3]) % 2 == 0
            and (i[2] * 100 + i[3] * 10 + i[4]) % 3 == 0
            and (i[3] * 100 + i[4] * 10 + i[5]) % 5 == 0
            and (i[4] * 100 + i[5] * 10 + i[6]) % 7 == 0
            and (i[5] * 100 + i[6] * 10 + i[7]) % 11 == 0
            and (i[6] * 100 + i[7] * 10 + i[8]) % 13 == 0
            and (i[7] * 100 + i[8] * 10 + i[9]) % 17 == 0
        ):
            n += convert(i)
    print(n)


if __name__ == "__main__":
    main()
