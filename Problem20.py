# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!


def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number - 1)


sum = 0
for i in str(fact(100)):
    sum += int(i)

print(sum)
