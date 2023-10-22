from ex12 import num_word
# Write a Python program to find the second most repeated word in a given string.

def second_most_repeated(s):
    d = num_word(s)
    l = list(reversed(sorted(list(d.values()))))
    for i in d:
        if d[i] == l[1]:
            return i

if __name__ == "__main__":
    s = "red blue orange yellow red blue blue"
    print(second_most_repeated(s))
