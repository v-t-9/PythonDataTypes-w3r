import random
# Write a Python program to extract a given number of randomly selected elements from a given list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Selected 3 random numbers of the above list:
# [4, 4, 1]

if __name__ == "__main__":
    l = [1, 1, 2, 3, 4, 4, 5, 1]
    n = 3
    random_selection = random.sample(l,n)
    print(random_selection)