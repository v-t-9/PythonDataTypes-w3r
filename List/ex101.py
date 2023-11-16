# Write a Python program to sort a given matrix in ascending order according to the sum of its rows.
# Original Matrix:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# Original Matrix:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]

def sort_ascending_sum(l):
    res = sorted(l, key=sum)
    return res

if __name__ == "__main__":
    l1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
    l2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
    print(sort_ascending_sum(l1))
    print(sort_ascending_sum(l2))