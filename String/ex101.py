# Write a Python program to add two strings as if they were numbers (positive integer values). Return a message if the numbers are strings.
# Sample Output:
# 42
# Error in input!
# Error in input!
def add_str_as_numbers(n1,n2):
    if n1.isnumeric() and n2.isnumeric():
            res = int(n1) + int(n2)
            return res
    else:
        return f"Error in input!"

if __name__ == "__main__":
    n1 = "10"
    n2 = "32"
    n3 = "22.6"
    n4 = "100"
    n5 = "-200"

    print(add_str_as_numbers(n1,n2))
    print(add_str_as_numbers(n1,n3))
    print(add_str_as_numbers(n4,n5))