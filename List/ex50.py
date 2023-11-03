#  Write a Python program to sort a list of nested dictionaries.
subkey_value = lambda a : a["key"]["subkey"]
if __name__ == "__main__":
    my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
    print(sorted(my_list, key= subkey_value, reverse= True))
    