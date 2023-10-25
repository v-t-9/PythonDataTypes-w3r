from difflib import SequenceMatcher
# Write a Python program to find string similarity between two given strings.
# Sample Output:
# Original string:
# Python Exercises
# Python Exercises
# Similarity between two said strings:
# 1.0
# Original string:
# Python Exercises
# Python Exercise
# Similarity between two said strings:
# 0.967741935483871
# Original string:
# Python Exercises
# Python Ex.
# Similarity between two said strings:
# 0.6923076923076923
# Original string:
# Python Exercises
# Python
# Similarity between two said strings:
# 0.5454545454545454
# Original string:
# Java Exercises
# Python
# Similarity between two said strings:
# 0.0
def similar_str(s1, s2):
    return SequenceMatcher(None, s1, s2).ratio()

if __name__ == "__main__":
    s1 = "Python Exercises"
    s2 = "Python Exercises"
    s3 = "Python Exercise"
    s4 = "Python Ex."
    s5 = "Java"
    s6 = "Python"

    print(similar_str(s1, s2))
    print(similar_str(s1, s3))
    print(similar_str(s1, s4))
    print(similar_str(s1, s6))
    print(similar_str(s5, s6))