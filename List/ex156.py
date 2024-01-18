from ex155 import add_lists
# Write a Python program to add two given lists of different lengths, starting on the right.
# Original lists:
# [2, 4, 7, 0, 5, 8]
# [3, 3, -1, 7]
# Add said two lists from right:
# [2, 4, 10, 3, 4, 15]
# Original lists:
# [1, 2, 3, 4, 5, 6]
# [2, 4, -3]
# Add said two lists from right:
# [1, 2, 3, 6, 9, 3]
def add_lists_right(l1, l2):
    return add_lists(l1[::-1], l2[::-1])[::-1]
if __name__ == "__main__":
    l1 = [2, 4, 7, 0, 5, 8]
    l2 = [3, 3, -1, 7]
    l3 = [1, 2, 3, 4, 5, 6]
    l4 = [2, 4, -3]
    print(add_lists_right(l1,l2))
    print(add_lists_right(l3,l4))

