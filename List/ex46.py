# Write a Python program to select the odd items from a list.
def odd_num(l):
    return [i for i in l if i % 2 != 0]
        
if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print(odd_num(l))

   
 