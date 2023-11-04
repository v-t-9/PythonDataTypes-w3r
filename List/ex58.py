# Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

replace_last_element = lambda l1,l2: l1[:len(l1)-1] + l2

if __name__ == "__main__":
    l1 = [1, 3, 5, 7, 9, 10]
    l2 = [2, 4, 6, 8]
    print(replace_last_element(l1,l2))