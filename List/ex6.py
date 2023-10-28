
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
last = lambda l: l[-1]
sort_by_last_element_of_tuple = lambda l:  sorted(l,key=last)

if __name__ == "__main__":
    l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_by_last_element_of_tuple(l))