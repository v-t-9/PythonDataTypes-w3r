# Write a Python program to iterate over all pairs of consecutive items in a given list.
# Original lists:
# [1, 1, 2, 3, 3, 4, 4, 5]
# Iterate over all pairs of consecutive items of the said list:
# [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]

if __name__ == "__main__":
   l = [1, 1, 2, 3, 3, 4, 4, 5]
   print(list(zip(l, l[1:])))