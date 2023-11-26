# Write a Python program to count the frequency of consecutive duplicate elements in a given list of numbers.
# Original lists:
# [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
# Consecutive duplicate elements and their frequency:
# ([1, 2, 4, 5], [1, 3, 3, 4])

def frequency_consecutive_duplicates(l):
    n = list(set(l))
    fr = [l.count(i) for i in n]
    return n, fr

if __name__ == "__main__":
    l = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
    print(frequency_consecutive_duplicates(l))