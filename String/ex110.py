from ex96 import separate_words_upper
# Write a Python program to insert space before every capital letter appears in a given word.
# Sample Data:
# ("PythonExercises") -> "Python Exercises"
# ("Python") -> "Python"
# ("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"

if __name__ == "__main__":
    s1 = "PythonExercises"
    s2 = "Python"
    s3 = "PythonExercisesPracticeSolution"
    print(separate_words_upper(s1).lstrip())
    print(separate_words_upper(s2).lstrip())
    print(separate_words_upper(s3).lstrip())
