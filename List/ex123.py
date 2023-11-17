# Write a Python program to reverse strings in a given list of string values.
# Original lists:
# ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
def reverse_strings_in_list(l):
    return [ i[::-1] for i in l]
if __name__ == "__main__":
    l = ['Red', 'Green', 'Blue', 'White', 'Black']
    print(reverse_strings_in_list(l))