from ex114 import extract_element_list_tuples
# Write a Python program to sort a list of lists by a given index of the inner list.
# Original list:
# [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Sort the said list of lists by a given index ( Index = 0 ) of the inner list
# [('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
# Sort the said list of lists by a given index ( Index = 2 ) of the inner list
# [('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]

def sort_by_index_inner_list(l,n):
    l1 = sorted(extract_element_list_tuples(l,n))
    res = []
    for i in l1:
        for j in l:
            if i == j[n] :
                res.append(j)

    return res
if __name__ == "__main__":
    l = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
    n1 = 0
    n2 = 2
    print(sort_by_index_inner_list(l,n1))
    print(sort_by_index_inner_list(l,n2))
