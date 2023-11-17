# Write a Python program to find the maximum and minimum product of pairs of tuples within a given list.
# The original list, tuple :
# [(2, 7), (2, 6), (1, 8), (4, 9)]
# Maximum and minimum product from the pairs of the said tuple of list:
# (36, 8)
def max_min_product(l):
    prod = []
    p = 0
    for i,j in l:
            p = i * j
            prod.append(p)
    return max(prod), min(prod)

if __name__ == "__main__":
    l = [(2, 7), (2, 6), (1, 8), (4, 9)]
    print(max_min_product(l))