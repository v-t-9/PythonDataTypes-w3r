# Write a Python program to round every number in a given list of numbers and print the total sum multiplied by the length of the list.
# Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# Result:
# 243
def round_sum_multiply(l):

    return sum([ round(i) for i in l]) * len(l)


if __name__ == "__main__":
    l = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
    print(round_sum_multiply(l))