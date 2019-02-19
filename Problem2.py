y = 1
x = 2
z = 0
sum = 0


print(y)
print(x)

while x < 4000000:
    z = x
    x = x + y #3
    y = z
    print(x)
    print(y)


print(sum)
print(x)

