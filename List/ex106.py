# Write a Python program to count integers in a given mixed list.
# Original list:
# [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of integers in the said mixed list:
# 6
def count_int(l):
    c = 0
    for i in l:
        if type(i) is int:
            c = c + 1
    return c
if __name__ == "__main__":
    l = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
    print(count_int(l))