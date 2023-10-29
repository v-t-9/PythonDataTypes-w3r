# Write a Python program to get unique values from a list.

def unique_values_list(l):
    l1 = sorted(list(set(l)))
    return l1
if __name__ == "__main__":
    l = [2,5,12,1,45,2,6,12]
    print(unique_values_list(l))
   