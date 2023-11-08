# Write a Python program to flatten a given nested list structure.
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


def flatten_nested_list(l):
    res = []
    for i in l:
        if type(i) is list:
            for j in i:
                res.append(j)
        else:
            res.append(i)
    
    return res

if __name__ == "__main__":
    l = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
    print(flatten_nested_list(l))
