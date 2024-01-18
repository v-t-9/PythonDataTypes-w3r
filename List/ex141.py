# Write a Python program to remove empty lists from a given list of lists.
# Original list:
# [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
# After deleting the empty lists from the said lists of lists
# ['Red', 'Green', [1, 2], 'Blue']
def remove_empty_lists(l):
    res = []
    for i in l:
        if type(i) != list:
            res.append(i)
        if type(i) == list and len(i) != 0:
            res.append(i)
    return res

if __name__ == "__main__":
    l = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
    print(remove_empty_lists(l))