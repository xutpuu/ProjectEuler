# Problem 3 
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def main():
    n = 600851475143
    i = 2

    while i < n:
        if is_prime(i):
            if n % i == 0:
                print(i)
        i += 1
    
def is_prime(a):
    x = True 
    for i in (2, a):
            while x:
               if a%i == 0:
                   x = False
               else:
                   x = True

main()
