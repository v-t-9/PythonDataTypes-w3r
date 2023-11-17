# Write a Python program to find the item with the most occurrences in a given list.
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# Item with maximum occurrences of the said list:
# 2

def num_occurrences(l):
    d = dict()
    for i in l:
        d[i] = l.count(i)

    for k,m in d.items():
        if m == max(d.values()):
            return k

if __name__ == "__main__":
    l = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
    print(num_occurrences(l))