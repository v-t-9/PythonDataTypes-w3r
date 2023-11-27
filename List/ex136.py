# Write a Python program to remove duplicate words from a given list of strings.
# Original String:
# ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
# After removing duplicate words from the said list of strings:
# ['Python', 'Exercises', 'Practice', 'Solution']

if __name__ == "__main__":
    l = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
    print(list(set(l)))