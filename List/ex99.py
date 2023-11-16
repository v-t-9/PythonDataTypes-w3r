# Write a Python program to find the maximum and minimum values in a given heterogeneous list.
# Original list:
# ['Python', 3, 2, 4, 5, 'version']
# Maximum and Minimum values in the said list:
# (5, 2)


def max_min_heterogeneous_list(l):
    r = []
    for i in l:
        if type(i) is int:
            r.append(i)
    return max(r), min(r)
if __name__ == "__main__":
    l = ['Python', 3, 2, 4, 5, 'version']
    print(max_min_heterogeneous_list(l))