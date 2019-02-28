# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# https://projecteuler.net/project/images/p015.gif
# How many such routes are there through a 20×20 grid?

size = 20

n = size + 1

matrix = [[1 for i in range(n)] for j in range(n)] 

for i in range(1,n,1):
    for j in range(1,n,1):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]


print("In a", size,"x",size ,"grid there are", matrix[size][size], "possible paths.")
