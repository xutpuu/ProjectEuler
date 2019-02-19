# Problem 3 
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def main():
    x = 600851475143
    y = 2
    z = 1
    while z != x:
        if is_prime(y):
            if x % y == 0:
                print(y)
                z = z * y
        y = y + 1

    print(z)
    print(is_prime(y))

main()