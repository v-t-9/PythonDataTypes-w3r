from itertools import combinations
# 149. Write a Python program to get all possible combinations of the elements of a given list.
# Original list:
# ['orange', 'red', 'green', 'blue']
# All possible combinations of the said list's elements:
# [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]


def combinations_elements(l):
 res = []
 for i in range(len(l)+1):
    res = res + list(combinations(l,i))
 return res

if __name__ == "__main__":
 l = ['orange', 'red', 'green', 'blue']
 print(combinations_elements(l))