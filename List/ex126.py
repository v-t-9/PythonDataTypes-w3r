# Write a Python program to interleave multiple lists of the same length.
# Original list:
# list1: [1, 2, 3, 4, 5, 6, 7]
# list2: [10, 20, 30, 40, 50, 60, 70]
# list3: [100, 200, 300, 400, 500, 600, 700]
# Interleave multiple lists:
# [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]

def interleave_lists(l1,l2,l3):
    return [j for i in zip(l1,l2,l3) for j in i]

if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 = [10, 20, 30, 40, 50, 60, 70]
    l3 = [100, 200, 300, 400, 500, 600, 700]
    print(interleave_lists(l1,l2,l3))
