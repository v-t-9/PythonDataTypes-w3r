# Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red
def ordered_words(s):
    l = s.split(",")
    return sorted(list(set(l)))
    
if __name__ == "__main__":
    s = " red, white, black, red, green, black"
    print(ordered_words(s))
    