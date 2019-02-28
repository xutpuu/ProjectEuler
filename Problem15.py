# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# https://projecteuler.net/project/images/p015.gif
# How many such routes are there through a 20×20 grid?

size = 2

n = size + 1

matrix = [[0 for x in range(n)] for y in range(n)] 

for row in matrix:
    for cell in row: 
        print(cell)

print(matrix)
