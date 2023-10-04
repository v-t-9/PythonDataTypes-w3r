from ex1 import len_str
# Write a Python function that takes a list of words and return the longest word and the length of the longest one.
def longest_word_length(l):
    l_len = list(map(len_str, l))
    max_len = max(l_len)
    word_pos = l_len.index(max_len)
    word = l[word_pos]
    return word, max_len


if __name__ == "__main__":
    l = [ "exercises", "function", "python", "word", "longest"]
    print(longest_word_length(l))