# Write a Python program to reverse each list in a given list of lists.
# Original list of lists:
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# Reverse each list in the said list of lists:
# [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]

def reverse_list_in_list(l):
    res =  [i[::-1] for i in l]
    return res

if __name__ == "__main__":
    l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(reverse_list_in_list(l))
