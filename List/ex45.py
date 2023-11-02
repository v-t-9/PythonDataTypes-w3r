# Write a Python program to convert a pair of values into a sorted unique array.
def pair_values_unique_array(l):
    res = list(set([j for i in l for j in i]))
    return res

if __name__ == "__main__":
    l = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
    print(pair_values_unique_array(l))
