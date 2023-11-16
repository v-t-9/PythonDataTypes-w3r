from itertools import groupby
# Write a Python program to extract specified number of elements from a given list, which follows each other continuously.
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# Extract 2 number of elements from the said list which follows each other continuously:
# [1, 4]
# Original lists:
# [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
# Extract 4 number of elements from the said list which follows each other continuously:
# [4]


def extract_elements_continuously(l,n):
    res = []
    for i,j in groupby(l):
        if len(list(j)) == n:
            res.append(i)
    return res
if __name__ == "__main__":
    l1 = [1, 1, 3, 4, 4, 5, 6, 7]
    n1 = 2
    l2 = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
    n2 = 4
    print(extract_elements_continuously(l1,n1))
    print(extract_elements_continuously(l2,n2))