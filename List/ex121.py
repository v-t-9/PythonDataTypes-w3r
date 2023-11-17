# Write a Python program to find nested list elements that are present in another list.
# Original lists:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Intersection of said nested lists:
# [[12], [7, 11], [1, 5, 8]]
def find_nested_elements(l1,l2):
    res = [[j for j in i if j in l1] for i in l2]
    return res
    

if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    l2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
    print(find_nested_elements(l1,l2))