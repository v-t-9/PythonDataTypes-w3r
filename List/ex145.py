import random
# Write a Python program to generate a number in a specified range except for some specific numbers.
# Generate a number in a specified range (1, 10) except [2, 9, 10]
# 7
# Generate a number in a specified range (-5, 5) except [-5,0,4,3,2]
# -4

def generate_number_except(r,e):
    l = []
    mi,ma = r
    for i in range(mi, ma):
        if i not in e:
            l.append(i)
    return random.choice(l)


if __name__ == "__main__":
    r1 = (1,10)
    e1 = [2, 9, 10]
    r2 = (-5,5)
    e2 = [-5,0,4,3,2]
    print(generate_number_except(r1,e1))
    print(generate_number_except(r2,e2))