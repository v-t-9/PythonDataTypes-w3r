# Write a Python program to find the second largest number in a list.

def second_largest_number(l):
    l1 = sorted(list(set(l)))
    return l1[-2]
if __name__ == "__main__":
    l1 = [2,5,12,1,45,2,6,12]
    l2 = [-2,-5,4,7,-7,8]
    print(second_largest_number(l1))
    print(second_largest_number(l2))