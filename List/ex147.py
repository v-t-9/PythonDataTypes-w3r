import random
# 147. Write a Python program to combine two lists into another list randomly.
# Original lists:
# [1, 2, 7, 8, 3, 7]
# [4, 3, 8, 9, 4, 3, 8, 9]
# Interleave two given list into another list randomly:
# [4, 1, 2, 3, 8, 9, 4, 3, 7, 8, 9, 8, 3, 7]
def combine_randomly(l1,l2):
    l = l1 + l2
    random.shuffle(l)
    return l

if __name__ == "__main__":
    l1 = [1, 2, 7, 8, 3, 7]
    l2 = [4, 3, 8, 9, 4, 3, 8, 9]
    print(combine_randomly(l1,l2))