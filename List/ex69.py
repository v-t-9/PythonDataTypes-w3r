#  Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]
def remove_duplicates(l):
    r = []
    for i in l:
        if i not in r:
            r.append(i)
    return r


if __name__ == "__main__":
    l1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    print(remove_duplicates(l1))
