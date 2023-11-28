# Write a Python program to sort a given list of strings(numbers) numerically.
# Original list:
# ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# Sort the said list of strings(numbers) numerically:
# [-500, -12, 0, 4, 7, 12, 45, 100, 200]

if __name__ == "__main__":
    l = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
    r = sorted(int(i) for i in l)
    print(r)