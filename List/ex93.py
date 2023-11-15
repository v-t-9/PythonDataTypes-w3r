# Write a Python program to count the number of sublists that contain a particular element.
# Original list:
# [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# Count 1 in the said list:
# 3
# Count 7 in the said list:
# 2
# Original list:
# [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# Count 'A' in the said list:
# 3
# Count 'E' in the said list:
# 1
def count_num_sublist(l,k):
    c = 0
    for i in l:
        if k in i:
            c = c + 1
        
    return c
if __name__ == "__main__":
    l1 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
    n1 = 1
    n2 = 7
    l2 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
    le1 = 'A'
    le2 = 'E'

    print(count_num_sublist(l1,n1))
    print(count_num_sublist(l1,n2))
    print(count_num_sublist(l2,le1))
    print(count_num_sublist(l2,le2))