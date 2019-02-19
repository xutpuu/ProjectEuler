x = 1
y = 2
z = x + y
sum = 0

while x < 4000000:
    z = x
    x = x + y #3
    y = z
    print(x)
    print(y)


print(sum)
print(x)

