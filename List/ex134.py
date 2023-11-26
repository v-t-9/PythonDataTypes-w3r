# Write a Python program to find the difference between two lists including duplicate elements.
# Original lists:
# [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
# [1, 1, 2, 4, 5, 6]
# Difference between two said list including duplicate elements):
# [3, 3, 4, 7]

def difference_with_duplicates(l1,l2):
    r = l1
    for i in l2:
        r.remove(i)
    return r

if __name__ == "__main__":
    l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
    l2 = [1, 1, 2, 4, 5, 6]

    print(difference_with_duplicates(l1,l2))