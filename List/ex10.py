# Write a Python program to find the list of words that are longer than n from a given list of words.
words_longer_than_n = lambda l, n:  [i for i in l if len(i) > n]

if __name__ == "__main__":
    l =["red", "blue", "orange", "green", "yellow", "magenta"]
    n = 4
    print(words_longer_than_n(l,n))