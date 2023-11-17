# Write a Python program to compute average of two given lists.
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 4, 5, 7, 8]
# Average of two lists:
# 3.823529411764706


avg_lists = lambda l1,l2:(sum(l1) + sum(l2))/(len(l1)+len(l2))
if __name__ == "__main__":
    l1 = [1, 1, 3, 4, 4, 5, 6, 7]
    l2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
    print(avg_lists(l1,l2))