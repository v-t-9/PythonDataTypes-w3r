# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
def remove_element_pos(l):
    return l[1:4] 
if __name__ == "__main__":
    l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print(remove_element_pos(l))
