# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
import math as m

limit = 2000000
crosslimit = m.sqrt(limit)
sieve = []

n = 1
for n in range(limit):
    sieve.append(False)

n = 4
for n in range(n,limit,2):
    sieve[n]=True

n = 3
for n in range(n,int(crosslimit),2):
    if not sieve[n]:
        m = n * n
        for m in range(m,limit,2*n):
            sieve[m] = True

sum = 0
n = 2
for n in range(n,limit,1):
    if not sieve[n]:
        sum = sum + n

print(sum)