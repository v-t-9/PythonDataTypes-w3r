#  Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises


def last_part_str(s):
    p = []
    for i in range(len(s)):
        if s[i] == "/":
            p.append(i)
    return s[:p[-1]]

if __name__ == "__main__":
    s1 = "https://www.w3resource.com/python-exercises"
    print(last_part_str(s1))