
# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    s = 0
    n = 2000000

    for i in range(n):
        if i > 1 and (is_prime(i)):
            print(i)
            s = s + i
    print("Sum of all prime number below {0:0d} is {1:d}".format(n,s))
        

main()