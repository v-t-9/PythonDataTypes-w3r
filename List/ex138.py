# Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings.
# Original list:
# [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings:
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']


def sort_int_first(l):
    n = sorted([i for i in l if type(i) == int])
    s = sorted([i for i in l if type(i) == str])
    r = n + s
    return r



if __name__ == "__main__":
    l = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
    print(sort_int_first(l))
