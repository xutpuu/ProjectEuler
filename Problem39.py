# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
import math
import time as t


def per_RightAngleTriangle(a, b, c):
    p = 120
    return p * (p - 2 * a) % (2 * (p - a))



# a² + b² = c²
# a + b + c = p
# c = p - a - b
# a² + b² = (p - a - b)² = p² + a² + b² - 2pa - 2pb + 2ab
# b = (p² - 2pa) / (2p - 2a)
# a < c and b < c
# a ≤ b < c 
def program():
    maxCounter = 0
    result = 0
    for p in range(2, 1000, 2):
        counter = 0
        for a in range(2, p // 3):
            #(p² - 2pa) / (2p - 2a) if replace / on % and recieve 0 it will mean that b is correct for rigth angle triangle
            if p * (p - 2 * a) % (2 * (p - a)) == 0: 
                counter += 1
            if counter > maxCounter:
                maxCounter = counter
                result = p
    print(result)


def main():
    start = t.time()
    program()
    print(per_RightAngleTriangle(20,48,52))
    end = t.time()
    print("Total time taken:", end - start, "ms")


if __name__ == "__main__":
    main()
