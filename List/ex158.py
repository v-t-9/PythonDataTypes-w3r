#  Write a Python program to find the maximum and minimum values in a given list of tuples.
# Original list with tuples:
# [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
# Maximum and minimum values of the said list of tuples:
# (78, 60)
def max_min(l):
    n = [j for i in l for j in i if type(j) == int]
    return min(n), max(n)
if __name__ == "__main__":
    t = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
    print(max_min(t))
