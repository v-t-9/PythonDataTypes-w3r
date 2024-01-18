# Write a Python program to check if a given element occurs at least n times in a list.
# Original list:
# [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
# Check if 3 occurs at least 4 times in a list:
# True
# Check if 0 occurs at least 5 times in a list:
# True
# Check if 8 occurs at least 3 times in a list:
# False

def it_occurs(l, n, o):
    li = [i for i in l if i == n]
    if len(li) >= o:
        return True
    return False

if __name__ == "__main__":
    l = [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
    n1 = 3
    o1 = 4
    n2 = 0
    o2 = 5
    n3 = 8
    o3 = 3
    print(it_occurs(l,n1,o1))
    print(it_occurs(l,n2,o2))
    print(it_occurs(l,n3,o3))
