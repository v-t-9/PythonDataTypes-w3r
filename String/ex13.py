#  Write a Python script that takes input from the user and displays that input back in upper and lower cases.
to_upper = lambda x: x.upper()
to_lower = lambda x: x.lower()

if __name__ == "__main__":
    user_input = input("How old are you? ")
    print(to_upper(user_input))
    print(to_lower(user_input))