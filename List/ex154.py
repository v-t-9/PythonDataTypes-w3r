# Write a Python program to join two given list of lists of the same length, element wise.
# Original lists:
# [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# Join the said two lists element wise:
# [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
# Original lists:
# [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
# [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
# Join the said two lists element wise:
# [['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]

def join_lists(l1,l2):
    res = []
    for i , j in list(zip(l1,l2)):
        res.append((i+j))
    return res

if __name__ == "__main__":
    l1 = [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
    l2 = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
    l3 = [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
    l4 = [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
    print(join_lists(l1,l2))
    print(join_lists(l3,l4))