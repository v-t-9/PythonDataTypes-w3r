# Write a Python program to append the same value/a list multiple times to a list/list-of-lists.
# Add a value(7), 5 times, to a list:
# ['7', '7', '7', '7', '7']
# Add 5, 6 times, to a list:
# [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
# Add a list, 4 times, to a list of lists:
# [[1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]
# Add a list, 3 times, to a list of lists:
# [[5, 6, 7], [1, 2, 5], [1, 2, 5], [1, 2, 5]]

def add_value(v, l = [], n = 0):
    for i in range(n):
        l.append(v)
    return l
if __name__ == "__main__":
    v1 = 7
    v2 = 6
    v3 = 4
    v4 = 3
    v5 = 5
    l1 = [1,2,3,4]
    l2 = [1,2,5]
    l3 = [[5,6,7]]
    print(add_value(v1,[], v5))
    print(add_value(v5, l1, v2))
    print(add_value(l2,[], v3))
    print(add_value(l2,l3, v4))