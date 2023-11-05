# Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

insert_string_at_beginning = lambda l,s: [ s + str(i) for i in l]
if __name__ == "__main__":
    l = [1,2,3,4]
    s = "emp"
    print(insert_string_at_beginning(l,s))