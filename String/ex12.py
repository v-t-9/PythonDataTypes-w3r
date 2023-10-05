# Write a Python program to count the occurrences of each word in a given sentence.
def num_word(s):
    r = dict()
    l = s.split(" ")
    for i in l:
        r[i] = l.count(i)
    return r

if __name__ == "__main__":
    s = "Hello how are you?"
    print(num_word(s))