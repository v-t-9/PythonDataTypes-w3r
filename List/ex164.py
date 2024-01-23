# Write a Python program to get items from a given list with specific conditions.
# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Number of Items of the said list which are even and greater than 45
# 5
def even_greater_than(l,n):
    c = 0
    for i in l:
        if i > 45 and i % 2 == 0:
            c = c + 1
    return c
if __name__ == "__main__":
    l = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
    n = 45
    print(even_greater_than(l,n))