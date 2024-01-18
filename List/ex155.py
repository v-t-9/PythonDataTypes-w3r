# Write a Python program to add two given lists of different lengths, starting on the left.
# Original lists:
# [2, 4, 7, 0, 5, 8]
# [3, 3, -1, 7]
# Add said two lists from left:
# [5, 7, 6, 7, 5, 8]
# Original lists:
# [1, 2, 3, 4, 5, 6]
# [2, 4, -3]
# Add said two lists from left:
# [3, 6, 0, 4, 5, 6]

def add_lists(l1,l2):

    while len(l1)>len(l2):
        l2.append(0)
    while len(l2)>len(l1):
        l1.append(0)
    res = [i + j for i,j in list(zip(l1,l2))]
    return res

if __name__ == "__main__":
    l1 = [2, 4, 7, 0, 5, 8]
    l2 = [3, 3, -1, 7]
    l3 = [1, 2, 3, 4, 5, 6]
    l4 = [2, 4, -3]
    print(add_lists(l1, l2))
    print(add_lists(l3, l4))