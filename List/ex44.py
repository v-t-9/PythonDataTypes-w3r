#  Write a Python program to generate groups of five consecutive numbers in a list.

if __name__ == "__main__":
    r = [[5*i + j for j in range(1,6)] for i in range(5)]
    print(r)
    
        
    