# Write a Python program to get the index of the first element that is greater than a specified element.
# Original list:
# [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
# Index of the first element which is greater than 73 in the said list:
# 4
# Index of the first element which is greater than 21 in the said list:
# 1
# Index of the first element which is greater than 80 in the said list:
# 5
# Index of the first element which is greater than 55 in the said list:
# 3
def index_first_element_greater_than(l,n):
    for i in l:
        if i > n:
            return l.index(i)

if __name__ == "__main__":
    l = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
    n1 = 73
    n2 = 21
    n3 = 80
    n4 = 55
    print(index_first_element_greater_than(l, n1))
    print(index_first_element_greater_than(l, n2))
    print(index_first_element_greater_than(l, n3))
    print(index_first_element_greater_than(l, n4))