# The nᵗʰ term of the sequence of triangle numbers is given by, tₙ = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding
# these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t₁₀.
# If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
# common English words, how many are triangle words?
import sys

fname = "p042_words.txt"

try:
    f = open(fname, "r")
except IOError:
    print("Could not read file:", fname)
    sys.exit()


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print("[*] Total time taken: {} sec.".format(end - start))
        return return_value

    return wrapper


def triangleNumbers(length):
    triangleList = []
    for i in range(1, length):
        triangleList.append(i * (i + 1) / 2)
    return triangleList


lettersWeight = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}


def converter(word):
    value = 0
    for l in word:
        value += lettersWeight[l]
    return value


@benchmark
def main():
    print("Begin")
    counter = 0
    triangles = triangleNumbers(1000)

    for line in f:
        str = line.split(",")
    
    for w in str:
        if converter(w.replace('"', "")) in triangles:
            counter += 1
    
    print(counter)



if __name__ == "__main__":
    main()
