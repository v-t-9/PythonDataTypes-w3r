# Write a Python program to extract the nth element from a given list of tuples.
# Original list:
# [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Extract nth element ( n = 0 ) from the said list of tuples:
# ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
# Extract nth element ( n = 2 ) from the said list of tuples:
# [99, 96, 94, 98]

def extract_element_list_tuples(l,n):
    res = []
    for i in l:
        res.append(i[n])
    return res


if __name__ == "__main__":
    l = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
    n1 = 0
    n2 = 2
    print(extract_element_list_tuples(l,n1))
    print(extract_element_list_tuples(l,n2))