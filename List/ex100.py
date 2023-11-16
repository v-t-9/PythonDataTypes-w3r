# Write a Python program to extract common index elements from more than one given list.
# Original lists:
# [1, 1, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 7]
# [0, 1, 2, 3, 4, 5, 7]
# Common index elements of the said lists:
# [1, 7]
def common_index_elements(l1,l2,l3):
    l = zip(l1,l2,l3)
    res = []
    for i,j,k in l:
        if i == j  and i == k:
            res.append(i)
    return res

if __name__ == "__main__":
    l1 = [1, 1, 3, 4, 5, 6, 7]
    l2 = [0, 1, 2, 3, 4, 5, 7]
    l3 = [0, 1, 2, 3, 4, 5, 7]
    print(common_index_elements(l1,l2,l3))