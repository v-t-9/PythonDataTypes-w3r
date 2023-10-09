# Write a Python program to create a Caesar encryption.
def caesar_encryption(t, sh):
    lower_l = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v","w", "x","y", "z"]
    upper_l = ["A", "B", "C", "D", "E", "F", "G", "H", "I","J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V","W", "X","Y", "Z"]

    res = []
    for i in range(len(t)):
        if t[i].isupper():
            f = upper_l.index(t[i])
            res.append(upper_l[f+sh])
        elif t[i].islower():
            f = lower_l.index(t[i])
            res.append(lower_l[f+sh])
    return res

if __name__ == "__main__":
    text = input("Enter the text you want to encrypt: ")
    shift = int(input("Enter number of positions: "))
    print(caesar_encryption(text,shift))

