# Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
def remove_consecutive_duplicates(l):
    r = []
    
    l2 = l[1:]
    l2.append(None)
    for i, j in zip(l, l2):
        if i == j:
            continue
        else:
            r.append(i)


    return r
if __name__ == "__main__":
    l = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    print(remove_consecutive_duplicates(l))
