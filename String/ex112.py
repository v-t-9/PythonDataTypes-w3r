#  Write a Python program to calculate the sum of two numbers given as strings. Return the result in the same string representation.
# Sample Data:
# ( "234242342341", "2432342342") -> "236674684683"
# ( "", "2432342342") -> False ( "1000", "0") -> "1000"
# ( "1000", "10") -> "1010"
def sum_num_str(a,b):
    res = 0
    if a == "" or b == "":
        return False
    else:
        res  = int(a) + int(b)
        return str(res)
if __name__ == "__main__":
    s1 = "234242342341"
    s2 = "2432342342"
    s3 = ""
    s4 = "1000"
    s5 = "0"
    s6 = "10"
    print(sum_num_str(s1,s2))
    print(sum_num_str(s2,s3))
    print(sum_num_str(s4,s5))
    print(sum_num_str(s4,s6))