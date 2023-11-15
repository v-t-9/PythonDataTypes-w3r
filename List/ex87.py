# Write a Python program to read a matrix from the console and print the sum for each column. As input from the user, accept matrix rows, columns, and elements separated by a space (each row).
# Input rows: 2
# Input columns: 2
# Input of elements in a row (1, 2, 3):
# 1 2
# 3 4
# sum for each column:
# 4 6

def matrix_of_elements(rows,col,elem):
    mat = []
    for i in range(rows):
        a = []*col
        mat.append(a)
        
        e = [int(i) for i in elem.split(" ")]
        for j in range(col):
          
            mat[i][j] = e[j]
     
    return mat
if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    col = int(input("Enter number of columns: "))
    elem = input("Enter elements of a row separated by a space:")
    print(matrix_of_elements(rows, col, elem))



