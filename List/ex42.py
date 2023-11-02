# Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h
def missing_additional_values(l1,l2):

    a = [i for i in l2 if i not in l1]

    m = [i for i in l1 if i not in l2]
    return "Missing values: {} \nAdditional values {}".format(a,m)
if __name__ == "__main__":
    list1 = ['a', 'b', 'c', 'd', 'e', 'f']
    list2 = ['d', 'e', 'f', 'g', 'h']
    print(missing_additional_values(list1, list2))