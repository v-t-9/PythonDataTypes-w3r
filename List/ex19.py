# Write a Python program to calculate the difference between the two lists.

difference_between_lists = lambda l1, l2: list(set(l1) - set(l2)) + list(set(l2) - set(l1)) 

if __name__ == "__main__":
    l1 = [1,2, 2,3,4,5]
    l2 = [4,5,6,7,8,8]
    print(difference_between_lists(l1,l2))