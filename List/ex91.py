# Write a Python program to find a list with maximum and minimum lengths.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
# (3, [3, 5, 7])
# List with minimum length of lists:
# (1, [0])
# Original list:
# [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
# (4, [1, 34, 5, 7])
# List with minimum length of lists:
# (1, [12])
def min_max_len(l):
    min_max = [len(i) for i in l]
    mi = min(min_max)
    ma = max(min_max)
    pos_mi = min_max.index(mi)
    pos_ma = min_max.index(ma)
    return "List with minimum length of lists:\nLength:{}\nList:{}\nList with maximum length of lists:\nLength:{}\nList:{}".format(mi, l[pos_mi], ma, l[pos_ma])
if __name__ == "__main__":
    l1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
    l2 = [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
    l3 = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
    print(min_max_len(l1))
    print(min_max_len(l2))
    print(min_max_len(l3))