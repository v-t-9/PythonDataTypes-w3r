from ex102 import remove_punctuation
# Write a Python program to extract and display the name from a given Email address.
# Sample Data:
# ("john@example.com") -> ("john")
# ("john.smith@example.com") -> ("johnsmith")
# ("fully-qualified-domain@example.com") -> ("fullyqualifieddomain")


def extract_name_from_address(s):
    f = s.find("@")
    return remove_punctuation(s[:f])
if __name__ == "__main__":
    s1 = "john@example.com"
    s2 = "john.smith@example.com"
    s3 = "fully-qualified-domain@example.com"
    print(extract_name_from_address(s1))
    print(extract_name_from_address(s2))
    print(extract_name_from_address(s3))
