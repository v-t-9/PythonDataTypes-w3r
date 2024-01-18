# 146. Write a Python program to compute the sum of digits of each number in a given list.
# Original tuple:
# [10, 2, 56]
# Sum of digits of each number of the said list of integers:
# 14
# Original tuple:
# [10, 20, 4, 5, 'b', 70, 'a']
# Sum of digits of each number of the said list of integers:
# 19
# Original tuple:
# [10, 20, -4, 5, -70]
# Sum of digits of each number of the said list of integers:
# 19

def sum_digits_numbers(l):
    res = []
    li = [str(abs(i)) for i in l if type(i) == int]

    for i in li:
        if len(i) > 1:
            for j in i:
                res.append(int(j))
        else:
            res.append(int(i))


    return sum(res)

if __name__ == "__main__":
    l1 = [10, 2, 56]
    l2 = [10, 20, 4, 5, 'b', 70, 'a']
    l3 = [10, 20, -4, 5, -70]
    print(sum_digits_numbers(l1))
    print(sum_digits_numbers(l2))
    print(sum_digits_numbers(l3))