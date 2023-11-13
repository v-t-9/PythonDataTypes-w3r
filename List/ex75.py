#  Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters.
# Original list:
# [1, 1, 2, 3, 4, 4.3, 5, 1]
# List reflecting the run-length encoding from the said list:
# [[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
# Original String:
# automatically
# List reflecting the run-length encoding from the said string:
# [[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
def runlen_encoding(l):
    c = 1
    res = []
    l2 = l[1:]
    l2.append(None)
    l3 = zip(l, l2)
    for i, j in l3:
        if i == j:
            c = c +1
            res.append([c,j])
        elif i != j and j != None:
            c = 1
            res.append([c,j])
    return res

def str_to_list(s):
    return [i for i in s]

if __name__ == "__main__":
    l = [1, 1, 2, 3, 4, 4.3, 5, 1]
    s = "automatically"
    print(runlen_encoding(l))
    print(runlen_encoding(str_to_list(s)))