# Write a Python program to check whether a string contains all letters of the alphabet.


def all_letters_alphabet(s):
    r = list(set(s.lower()))
    while " " in r:
        r.remove(" ")
    return sorted(r) == lower_l


if __name__ == "__main__":
    s1 = "The quick brown fox jumps over the lazy dog"
    s2 = "The quick brown fox jumps over the lazy cat"
    lower_l = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v","w", "x","y", "z"]
    print(all_letters_alphabet(s1))
    print(all_letters_alphabet(s2))