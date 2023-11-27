# Write a Python program to find the first even and odd number in a given list of numbers.
# Original list:
# [1, 3, 5, 7, 4, 1, 6, 8]
# First even and odd number of the said list of numbers:
# (4, 1)


def first_even_odd(l):
    even = [i for i in l if i % 2 == 0]
    odd = [i for i in l if i % 2 != 0]
    return even[0], odd[0]

if __name__ == "__main__":
   l =  [1, 3, 5, 7, 4, 1, 6, 8]
   print(first_even_odd(l))
