# Write a Python program to find all the values in a list that are greater than a specified number.

greater_than = lambda l,n:[i for i in l if i > n]
if __name__ == "__main__":
    l = [100, 25, 43, 72, 59, 12, 132, 145]
    n = 50
    print(greater_than(l,n))