
from itertools import product
# Write a Python program to print all permutations with a given repetition number of characters of a given string.
def permutations(s, rep):
    res = []
    for i in product(s, repeat= rep):
        res.append(i)
    return res

if __name__ == "__main__":
    s = "abc"
    rep = 3
    res = []
    print(permutations(s,rep))
    