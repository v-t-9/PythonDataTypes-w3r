# Write a Python program to access multiple elements at a specified index from a given list.
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# Index list:
# [0, 3, 5, 7, 10]
# Items with specified index of the said list:
# [2, 4, 9, 2, 1]
def access_multiple_elements(l,ind):
    res = [ l[i] for i in range(len(l)) if i in ind]
    return res
if __name__ == "__main__":
    l = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
    ind = [0, 3, 5, 7, 10]
    print(access_multiple_elements(l,ind))