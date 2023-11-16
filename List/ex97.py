# Write a Python program to remove sublists from a given list of lists that contain an element outside a given range.
# Original list:
# [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# After removing sublists from a given list of lists, which contains an element outside the given range:
# [[13, 14, 15, 17]]

def remove_sublist_with_element_outside_range(l,r1,r2):
    r = []
    for i in l:
        if min(i) >= r1 and max(i)<=r2:
            r.append(i)
    return r
if __name__ == "__main__":
    l = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
    r1 = 13
    r2 = 17
    print(remove_sublist_with_element_outside_range(l,r1,r2))