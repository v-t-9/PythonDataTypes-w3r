#  Write a Python program to check if a nested list is a subset of another nested list.
# Original list:
# [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# [[1, 3], [13, 15, 17]]
# If the one of the said list is a subset of another.:
# True
# Original list:
# [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
# [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.:
# True
# Original list:
# [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
# [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.:
# False
def is_subset(l1,l2):
    r = []
    for i in l2:
        if i in l1 :
            r.append(True)
        else:
            r.append(False)
    
    return all(r)

        

if __name__ == "__main__":
    l1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
    l2 = [[1, 3], [13, 15, 17]]
    l3 = [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
    l4 = [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
    l5 = [[[3, 4], [5, 6]]]
    print(is_subset(l1,l2))
    print(is_subset(l3,l5))
    print(is_subset(l4,l5))