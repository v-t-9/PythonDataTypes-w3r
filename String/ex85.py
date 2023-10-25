# Write a Python program to convert a given Bytearray to a Hexadecimal string.
# Sample Output:
# Original Bytearray :
# [111, 12, 45, 67, 109]
# Hexadecimal string:
# 6f0c2d436d

def bytearray_to_hexadecimal(a):
        res = ""
        for i in a:
            res = res + "{0:x}".format(i)
        
        return res 

if __name__ == "__main__":
        b_a = [111, 12, 45, 67, 109]
        print(bytearray_to_hexadecimal(b_a))