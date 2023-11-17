# Write a Python program to create a list taking alternate elements from a given list.
# Original list:
# ['red', 'black', 'white', 'green', 'orange']
# List with alternate elements from the said list:
# ['red', 'white', 'orange']
# Original list:
# [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
# List with alternate elements from the said list:
# [2, 3, 0, 8, 4]
alternate_elements = lambda l: [l[i] for i in range(0,len(l),2)]
if __name__ == "__main__":
    l1 = ['red', 'black', 'white', 'green', 'orange']
    l2 = [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
    print(alternate_elements(l1))
    print(alternate_elements(l2))