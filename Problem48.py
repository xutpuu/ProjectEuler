# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


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
    s = 0
    for i in range(1,1001):
        s += i**i
    print(str(s)[-10:])

if __name__ == "__main__":
    main()