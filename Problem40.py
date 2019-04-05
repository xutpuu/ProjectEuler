# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dₙ represents the nth digit of the fractional part, find the value of the following expression.
# d₁ × d₁₀ × d₁₀₀ × d₁₀₀₀ × d₁₀₀₀₀ × d₁₀₀₀₀₀ × d₁₀₀₀₀₀₀
import time


def program(limit):
    num = "0."
    digit = 1
    n = 1
    for i in range(limit + 2):
        num += str(i)
    while n <= 1000000:
        digit *= int(num[n + 2])
        n *= 10
    print(digit)


def main():
    start = time.time()
    program(1000000)
    end = time.time()
    print("Total time taken:", end - start, "ms")


if __name__ == "__main__":
    main()
