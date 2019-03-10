# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

fibonachi = []
fibonachi.append(1) 
fibonachi.append(1) 
l = 1
fib = 1
i = 1

while l < 1000:
    fib = fibonachi[i-1]+fibonachi[i]
    fibonachi.append(fib)
    i += 1
    l = len(str(fib))

i1 = fibonachi.index(fibonachi[-1]) + 1
print(i1)