# Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

if __name__ == "__main__":
    color1 = ["red", "orange", "green", "blue", "white"]
    color2 = ["black", "yellow", "green", "blue"]
    print(list(set(color1).difference(color2)))
    print(list(set(color2).difference(color1)))