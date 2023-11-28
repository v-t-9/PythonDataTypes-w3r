from ex114 import extract_element_list_tuples
# Write a Python program to remove a specific item from a given list of lists.
# Original list of lists:
# [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
# Remove 1st list from the saod given list of lists:
# [['Maroon', 'Yellow', 'Olive'], ['#800000', '#FFFF00', '#808000'], ['rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
# Remove 2nd list from the saod given list of lists:
# [['Red', 'Yellow', 'Olive'], ['#FF0000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
# Remove 4th list from the saod given list of lists:
# [['Red', 'Maroon', 'Yellow'], ['#FF0000', '#800000', '#FFFF00'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)']]

def remove_element_list_of_lists(l,n):
    e = extract_element_list_tuples(l,n)
    for i in l:
        for j in i:
            if j in e:
                i.remove(j)
         
    return l
if __name__ == "__main__":
   l=  [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
   n1 = 0
   n2 = 1
   n3 = 2
   n4 = 3
   #print(remove_element_list_of_lists(l, n1))
   #print(remove_element_list_of_lists(l, n2))
   #print(remove_element_list_of_lists(l, n3))
   print(remove_element_list_of_lists(l, n4))