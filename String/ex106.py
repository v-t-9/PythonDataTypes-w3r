from ex67 import remove_consecutive_duplicates
# Write a Python program to remove repeated consecutive characters and replace them with single letters and print a updated string.
# Sample Data:
# ("Red Green White") -> "Red Gren White"
# ("aabbbcdeffff") -> "abcdef"
# ("Yellowwooddoor") -> "Yelowodor"

if __name__ == "__main__":
    s1 = "Red Green White"
    s2 = "aabbbcdeffff"
    s3 = "Yellowwooddoor"
    print(remove_consecutive_duplicates(s1))
    print(remove_consecutive_duplicates(s2))
    print(remove_consecutive_duplicates(s3))