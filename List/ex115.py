#  Write a Python program to check if the elements of a given list are unique or not.
# Original list:
# [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
# Is the said list contains all unique elements!
# False
# Original list:
# [2, 4, 6, 8, 10, 12, 14]
# Is the said list contains all unique elements!
# True

def unique_elements(l):
    if len(l) != len(list(set(l))):
        return False
    else:
        return True

if __name__ == "__main__":
    l1 = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
    l2 = [2, 4, 6, 8, 10, 12, 14]
    print(unique_elements(l1))
    print(unique_elements(l2))
