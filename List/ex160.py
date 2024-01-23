#  Write a Python program to remove the first specified number of elements from a given list satisfying a condition.
# Remove the first 4 number of even numbers from the following list:
# [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
# Output:
# [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]
# Original list:
# [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
# Remove first 4 even numbers from the said list:
# [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]
def remove_first_num_elements(l,n):
    c = 1
    res = []
    for i in l:
        if i % 2 != 0 or c>n:
            res.append(i)
        else:
            c+=1

    return res
if __name__ == "__main__":
    l1 = [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
    l2 = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
    n = 4
    print(remove_first_num_elements(l1,n))
    print(remove_first_num_elements(l2,n))