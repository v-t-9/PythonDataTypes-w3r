# Write a Python program to count the number of elements in a list within a specified range.
def count_range(l, n1, n2):
    c = 0
    for i in l:
        if i >=n1 and i<=n2:
            c = c + 1
    
    return c
if __name__ == "__main__":
    l = [2,5,12,1,45,2,6,12,30,35,43,47,50,55,59]
    n1 = 30
    n2 = 60
    print(count_range(l, n1, n2))