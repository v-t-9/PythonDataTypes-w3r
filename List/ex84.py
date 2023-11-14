# Write a Python program to round the numbers in a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
# Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# Minimum value: 4
# Maximum value: 22
# Result:
# 20 25 45 55 60 70 80 90 110

def round_min_max_multiply_unique_ascending(l):
    r = " "
    ma = max([ round(i) for i in l])
    mi = min([ round(i) for i in l])
    mul = sorted(list(set([ round(i)*5 for i in l])))
    for i in mul:
        r = r + str(i) + " "

    return "Minimum: {} \nMaximum: {}\nNumbers:{}".format(mi,ma,r)

if __name__ == "__main__":
    l = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
    print(round_min_max_multiply_unique_ascending(l))
