sum = 0
i = 1

for i in range(1, 1000):
    if i % 3 == 0:
        sum = sum + i 
    elif i % 5 == 0:
        sum = sum + i 

print(sum)