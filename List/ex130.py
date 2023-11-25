# Write a Python program to count the same pair in three given lists.
# Original lists:
# [1, 2, 3, 4, 5, 6, 7, 8]
# [2, 2, 3, 1, 2, 6, 7, 9]
# [2, 1, 3, 1, 2, 6, 7, 9]
# Number of same pair of the said three given lists:
# 3
def count_same_pair(l1,l2,l3):
    c = 0
    for i,j,k in zip(l1,l2, l3):
        if i == j and j  == k:
            c = c + 1
    
    return c


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6, 7, 8]
    l2 = [2, 2, 3, 1, 2, 6, 7, 9]
    l3 = [2, 1, 3, 1, 2, 6, 7, 9]
    print(count_same_pair(l1,l2,l3))
