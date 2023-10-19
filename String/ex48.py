# Write a Python program to swap commas and dots in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"
def swap_commas_dots(s):
    r = ""
    for i in s:
        if i == ".":
            r = r + ","
        elif i == ",":
            r = r + "."
        else:
            r = r + i
    return r

if __name__ == "__main__":
    s = "32.054,23"
    print(swap_commas_dots(s))