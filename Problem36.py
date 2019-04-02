# The decimal number, 585 = 1001001001₂ (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
import time as t


def isPalidromic(num):
    reversedDecNum = int(str(num)[::-1])
    reversedBinNum = bin(reversedDecNum)[2:]
    if num == reversedDecNum:
        if str(bin(num)[2:]) == str(reversedBinNum)[::-1]:
            return True
        else:
            return False
    else:
        return False


def main():
    start = t.time()
    limit = 1000000
    sums = 0
    for i in range(limit):
        if isPalidromic(i):
            sums += i
    print(sums)
    end = t.time()
    print("Total time taken:", end - start, "ms")


if __name__ == "__main__":
    main()
