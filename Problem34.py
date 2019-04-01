# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def fact(number):
    if number <= 1:
        return 1
    else:
        return number * fact(number - 1)

sums = 0

for i in range(10,100000,1):
    s = 0
    for n in str(i):
        s += fact(int(n))
    if s == i:
        sums += s

print(sums)