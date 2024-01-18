# Write a Python program to extract every first or specified element from a given two-dimensional list.
# Original list of lists:
# [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
# Extract every first element from the said given two dimensional list:
# [1, 4, 7]
# Extract every third element from the said given two dimensional list:
# [3, 6, 9]

def extract_element(l, n):
    res = []
    for i in range(len(l)):
        res.append(l[i][n])
    return res

if __name__ == "__main__":
    l = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
    n1 = 0
    n2 = 2
    print(extract_element(l,n1))
    print(extract_element(l,n2))