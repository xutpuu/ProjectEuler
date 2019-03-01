# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

counter=[0]
def seq(number):
    counter[0] += 1
    if number == 1:
        return 1
    else:
        if number % 2 == 0:
            return seq(number/2)
        else:
            return seq(3*number + 1)

i = 1
chain = 0
maxI = 0
n = 1000000
for i in range(1,n,1):
    counter[0] = 0
    seq(i)
    if chain < counter[0]:
        chain = counter[0]
        maxI = i

print(maxI)