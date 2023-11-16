# Write a Python program to scramble the letters of a string in a given list.
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# After scrambling the letters of the strings of the said list:
# ['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']


def scramble_letters(l):
    res = ["".join(set(i)) for i in l]
    return res
if __name__ == "__main__":
    l = ['Python', 'list', 'exercises', 'practice', 'solution']
    print(scramble_letters(l))