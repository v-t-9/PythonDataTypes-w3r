# Write a Python program to Zip two given lists of lists.
# Original lists:
# [[1, 3], [5, 7], [9, 11]]
# [[2, 4], [6, 8], [10, 12, 14]]
# Zipped list:
# [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]


def zip_lists(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if i == j:
                l1[i].extend(l2[j])
    return l1
if __name__ == "__main__":
    l1 = [[1, 3], [5, 7], [9, 11]]
    l2 = [[2, 4], [6, 8], [10, 12, 14]]
    print(zip_lists(l1,l2))