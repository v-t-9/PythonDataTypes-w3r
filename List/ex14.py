# Write a Python program to print the numbers of a specified list after removing even numbers from it.
remove_even_num = lambda l: [i for i in l if i % 2 == 0]
    
if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(remove_even_num(l))