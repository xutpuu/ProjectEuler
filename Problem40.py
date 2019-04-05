# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dₙ represents the nth digit of the fractional part, find the value of the following expression.
# d₁ × d₁₀ × d₁₀₀ × d₁₀₀₀ × d₁₀₀₀₀ × d₁₀₀₀₀₀ × d₁₀₀₀₀₀₀
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
    num = "0."
    digit = 1
    n = 1
    for i in range(limit + 2):
        num += str(i)
    while n <= 1000000:
        digit *= int(num[n + 2])
        n *= 10
    print(digit)


if __name__ == "__main__":
    main()
