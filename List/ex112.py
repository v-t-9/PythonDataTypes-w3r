# Write a Python program to check whether a specified list is sorted or not.
# Original list:
# [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!
# True
# Original list:
# [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
# Is the said list is sorted!
# False
def is_sorted(l):
    if l == sorted(l):
        return True
    else:
        return False

if __name__ == "__main__":
    l1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
    l2 = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
    print(is_sorted(l1))
    print(is_sorted(l2))