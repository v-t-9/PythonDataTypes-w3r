#  Write a Python program to split a given list into two parts where the length of the first part of the list is given.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list: 3
# Splited the said list into two parts:
# ([1, 1, 2], [3, 4, 4, 5, 1])


def split_list_two(l,le):
    return l[:le], l[le:]


if __name__ == "__main__":
    l = [1, 1, 2, 3, 4, 4, 5, 1]
    le = 3
    print(split_list_two(l,le))