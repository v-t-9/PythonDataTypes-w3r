# Write a Python program to extract a specified column from a given nested list.
# Original Nested list:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Extract 1st column:
# [1, 2, 1]
# Original Nested list:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Extract 3rd column:
# [3, -5, 1]

def exctract_column(l,col):
    res = []
    for i in l:
       res.append(i[col-1])
    return res
            
if __name__ == "__main__":
    l1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
    col1 = 1
    l2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
    col2 = 3
    print(exctract_column(l1,col1))
    print(exctract_column(l2,col2))