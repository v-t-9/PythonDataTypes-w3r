# Write a Python program to check whether a string starts with specified characters.
start_str = lambda a,b: a.startswith(b)
if __name__ == "__main__":
    s = "w3resource.com"
    s_char = "w3"
    print(start_str(s,s_char))