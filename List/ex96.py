# Write a Python program to sort a given list of lists by length and value.
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

def sort_by_length_and_value(l):
    r = sorted(l)
    r.sort(key= len)
    return r
if __name__ == "__main__":
    l = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
    print(sort_by_length_and_value(l))
