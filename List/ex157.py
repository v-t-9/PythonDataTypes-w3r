# Write a Python program to interleave lists of varying lengths.
# Original lists:
# [2, 4, 7, 0, 5, 8]
# [2, 5, 8]
# [0, 1]
# [3, 3, -1, 7]
# Interleave said lists of different lengths:
# [2, 2, 0, 3, 4, 5, 1, 3, 7, 8, -1, 0, 7, 5, 8]

def interleave_lists(l1,l2,l3,l4):
    res = []
    ma = max([len(l1), len(l2), len(l3), len(l4)])
    for i in range(ma):
        if i < len(l1):
            res.append(l1[i])
        if i < len(l2):
            res.append(l2[i])
        if i < len(l3):
            res.append(l3[i])
        if i < len(l4):
            res.append(l4[i])
    return res


if __name__ == "__main__":
    l1 = [2, 4, 7, 0, 5, 8]
    l2 = [2, 5, 8]
    l3 = [0, 1]
    l4 = [3, 3, -1, 7]
    print(interleave_lists(l1,l2,l3,l4))