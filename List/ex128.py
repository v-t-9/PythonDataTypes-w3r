# Write a Python program to calculate the sum of the numbers in a list between the indices of a specified range.
# Original list:
# [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
# Range: 8 , 10
# Sum of the specified range:
# 29

def sum_num_range(l,min_r, max_r):
    c = 0
    for i in range(len(l)):
        if i >= min_r and i <= max_r:
            c = c + l[i]
    return c

if __name__ == "__main__":
    l = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
    min_r = 8
    max_r = 10
    print(sum_num_range(l, min_r, max_r))
