# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
import math
import time as t


def per_RightAngleTriangle(a, b, c):
    s = a**2 + b**2
    if c == math.sqrt(s):
        return a + b + c
    else:
        return 0


def program():
    limit = 100
    counter = 0
    for a in range(1, limit):
        for b in range(1, limit):
            for c in range(1, limit):
                if per_RightAngleTriangle(a, b, c) == 120:
                    print(a, b, c)
                    counter += 1
    print(counter)


def main():
    start = t.time()
    program()
    end = t.time()
    print("Total time taken:", end - start, "ms")


if __name__ == "__main__":
    main()
