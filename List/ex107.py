# Write a Python program to remove a specified column from a given nested list.
# Original Nested list:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# After removing 1st column:
# [[2, 3], [4, 5], [1, 1]]
# Original Nested list:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# After removing 3rd column:
# [[1, 2], [-2, 4], [1, -1]]
def remove_column(l,col):

    for i in l:
       del i[col-1]
    return l
            
if __name__ == "__main__":
    l1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
    col1 = 1
    l2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
    col2 = 3
    print(remove_column(l1,col1))
    print(remove_column(l2,col2))