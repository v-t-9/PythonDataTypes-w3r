# Write a Python program that returns a string sorted alphabetically by the first character of a given string of words.
# Sample Data:
# ("Red Green Black White Pink") -> "Black Green Pink Red White"
# ("Calculate the sum of two said numbers given as strings.") -> ("Calculate as given numbers of sum said strings. the two")
# ("The quick brown fox jumps over the lazy dog.") -> ("The brown dog. fox jumps lazy over quick the")
def sort_alphabetically_1st_char(s):
        l = s.split()
        l.sort()
        return l
if __name__ == "__main__":
    s1 = "Red Green Black White Pink"
    s2 = "Calculate the sum of two said numbers given as strings."
    s3 = "The quick brown fox jumps over the lazy dog."
    print(sort_alphabetically_1st_char(s1))
    print(sort_alphabetically_1st_char(s2))
    print(sort_alphabetically_1st_char(s3))