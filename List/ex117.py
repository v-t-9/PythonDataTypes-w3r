#  Write a Python program to remove all elements from a given list that are present in another list.
# Original lists:
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2: [2, 4, 6, 8]
# Remove all elements from 'list1' present in 'list2:
# [1, 3, 5, 7, 9, 10]
def remove_elements_in_list_present_in_another_list(l1,l2):
    return [ i for i in l1 if i not in l2]
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = [2, 4, 6, 8]
    print(remove_elements_in_list_present_in_another_list(list1,list2))