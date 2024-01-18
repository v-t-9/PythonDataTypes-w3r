# Write a Python program to reverse a given list of lists.
# Original list:
# [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
# Reverse said list of lists:
# [['white', 'black', 'pink'], ['green', 'blue'], ['orange', 'red']]
# Original list:
# [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
# Reverse said list of lists:
# [[2, 3, 4, 2, 4], [0, 2, 4, 5], [1, 2, 3, 4]]


if __name__ == "__main__":
    l1 = [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
    l2 = [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
    print(l1[::-1])
    print(l2[::-1])