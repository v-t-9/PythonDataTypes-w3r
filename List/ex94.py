# Write a Python program to count the number of unique sublists within a given list.
# Original list:
# [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# Number of unique lists of the said list:
# {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
# Original list:
# [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
# Number of unique lists of the said list:
# {('green', 'orange'): 2, ('black',): 1, ('white',): 1}

def unique_sublists(l):
    d = dict()
    for i in l:
        if i not in d.values():
            d[tuple(i)] = l.count(i)
    return d

if __name__ == "__main__":
    l1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
    l2 = [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
    print(unique_sublists(l1))
    print(unique_sublists(l2))
    