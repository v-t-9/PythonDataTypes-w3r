# Write a Python program to rotate a given list by a specified number of items in the right or left direction.
# original List:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Rotate the said list in left direction by 4:
# [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
# Rotate the said list in left direction by 2:
# [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
# Rotate the said list in Right direction by 4:
# [8, 9, 10, 1, 2, 3, 4, 5, 6]
# Rotate the said list in Right direction by 2:
# [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]

def rotate_list(l,st,n):
    if st == "left":
        return l[n:] + l[:n]
    if st == "right":
        return l[-n:] + l[:-n]
if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    r_o_l1 = "right"
    r_o_l2 = "left"
    n1 = 2
    n2 = 4
    print(rotate_list(l,r_o_l1, n2))
    print(rotate_list(l,r_o_l1, n1))
    print(rotate_list(l,r_o_l2, n1))
    print(rotate_list(l,r_o_l2, n2))