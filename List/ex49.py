# Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

def list_to_dict(l1, l2):

    res = [ {"color_name" : i, "color_code" : j} for i,j in zip(l1,l2)]
    return res
    

if __name__ == "__main__":
    colors = ["Black", "Red", "Maroon", "Yellow"]
    codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
    print(list_to_dict(colors, codes))
