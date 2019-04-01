# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


ways = 0
target = 200

a = target
while a >= 0:
    b = a
    while b >= 0:
        c = b
        while c >= 0:
            d = c
            while d >= 0:
                e = d
                while e >= 0:
                    f = e
                    while f >= 0:
                        g = f
                        while g >= 0:
                            ways += 1
                            g -= 2
                        f -= 5
                    e -= 10
                d -= 20
            c -= 50
        b -= 100
    a -= 200


print(ways)
