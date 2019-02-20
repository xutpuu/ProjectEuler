# Problem 7 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?

n = 10001

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main( n ):
    z = 0
    i = 100000
    while z < n:
        i += 1
        if is_prime(i):
            z += 1
    print(i,is_prime(i), z)

main(n)