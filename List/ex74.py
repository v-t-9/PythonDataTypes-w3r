from itertools import groupby
# Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]


def pack_into_sublists(l):
    res = []
    for key,group in groupby(l):
         res.append(list(group))
    return res
if __name__ == "__main__":
    l = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    print(pack_into_sublists(l))