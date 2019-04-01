# Problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed
# as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import math as m

limit = 28123


def isAbundant(number):
    if number == 1:
        return 1
    n = m.ceil(m.sqrt(number))
    total = 1
    divisor = 2
    while divisor < n:
        if number % divisor == 0:
            total += divisor
            total += number // divisor
        divisor += 1
    if n ** 2 == number:
        total += n
    if total > number:
        return True
    else:
        return False


abundentNumbers = []
for i in range(2, limit + 1):
    if isAbundant(i):
        abundentNumbers.append(i)

canBeAbundant = [False] * (limit + 1)
for i in range(0, len(abundentNumbers)):
    for j in range(i, len(abundentNumbers)):
        sumOfAbundants = abundentNumbers[i] + abundentNumbers[j]
        if sumOfAbundants <= limit:
            if canBeAbundant[sumOfAbundants] == False:
                canBeAbundant[sumOfAbundants] = True

sums = 0
for i in range(1, len(canBeAbundant)):
    if canBeAbundant[i] == False:
        sums += i

print(sums)
