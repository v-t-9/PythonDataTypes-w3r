#Write a Python program to remove the K'th element from a given list, and print the updated list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After removing an element at the kth position of the said list:
# [1, 1, 3, 4, 4, 5, 1]


def remove_k_element(l,k):
    return l[:k-1] +  l[k:]
if __name__ == "__main__":
    l = [1, 1, 2, 3, 4, 4, 5, 1]
    k = 3
    print(remove_k_element(l,k))