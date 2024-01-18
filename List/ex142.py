# Write a Python program to sum a specific column of a list in a given list of lists.
# Original list of lists:
# [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# Sum: 1st column of the said list of lists:
# 12
# Sum: 2nd column of the said list of lists:
# 15
# Sum: 4th column of the said list of lists:
# 9
def sum_col(l,c):
  res = 0
  for i in range(len(l)):
     res += l[i][c] 
  return res
        
if __name__ == "__main__":
    l = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
    c = 1
    print(sum_col(l, c))
    