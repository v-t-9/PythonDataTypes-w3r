# Write a Python program to find the difference between consecutive numbers in a given list.
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# Difference between consecutive numbers of the said list:
# [0, 2, 1, 0, 1, 1, 1]
# Original list:
# [4, 5, 8, 9, 6, 10]
# Difference between consecutive numbers of the said list:
# [1, 3, 1, -3, 4]

def difference_between_consecutive_numbers(l):
    res = []
    for i,j in zip(l,l[1:]):
        diff = j-i
        res.append(diff)
    return res
if __name__ == "__main__":
    l1 = [1, 1, 3, 4, 4, 5, 6, 7]
    l2 = [4, 5, 8, 9, 6, 10]
    print(difference_between_consecutive_numbers(l1))
    print(difference_between_consecutive_numbers(l2))
