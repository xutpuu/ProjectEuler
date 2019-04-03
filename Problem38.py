# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the
# concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
import time as t


def isUnusual(num):
    sorted_str = "".join(sorted(num))
    if sorted_str == "123456789":
        return True
    else:
        return False


def is_Num(num):
    numb = ""
    n = 0
    while len(numb) < 9:
        n += 1
        numb += str(num * n)
    if isUnusual(numb):
        return int(numb)
    else:
        return 0


def program():
    max_i = 1
    for i in range(2, 10000, 1):
        max_n = is_Num(i)
        if max_n > max_i:
            max_i = max_n
    print(max_i)


def main():
    start = t.time()
    program()
    end = t.time()
    print("Total time taken:", end - start, "ms")


if __name__ == "__main__":
    main()
