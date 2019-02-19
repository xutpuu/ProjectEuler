# Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = 2520
x = 11



def isDivisible ( number ):
    i = 1
    x = 21
    y = 0
    for i in range( 1, x, 1 ):
        if number % i == 0:
            y += 1
    if y == x - 1:
        return True
    else:
        return False

def main ():
    i = 1
    while True:
        i += 1
        if(isDivisible(i)):
            print(i)
            break
    

main()