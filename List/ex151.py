# Write a Python program to find the maximum and minimum values in a given list within a specified index range.
# Original list:
# [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
# Index range:
# 3 to 8
# Maximum and minimum values of the said given list within index range:
# (5, 0)
def max_min_range(l,r):
    mi, ma = r
    li = [l[i] for i in range(mi, ma)]
    return max(li), min(li)

if __name__ == "__main__":
    l = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
    r = (3,8)
    print(max_min_range(l,r))