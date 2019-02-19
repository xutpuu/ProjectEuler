# Problem 4 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic( n ):
    if n > 0:
        reverse = 0
        reverse = int(str(n)[::-1])
        if n == reverse:
            return True
        else:
            return False
    else:
            return False

def main():
    x = 1000
    z = 0

    i = 100
    u = 100
    i1 = 0
    u2 = 0
    for i in range (i, x, 1 ):
        for u in range (u, x, 1 ):
            if (is_palindromic( i * u )):
                z = i * u 
                i1 = i
                u2 = u
    print( i1 )
    print( u2 )
    print( z )

main()