# Write a Python program to remove existing indentation from all of the lines in a given text.
def without_indentation(t):
    l = t.split("\n")
    r = []
    res = ""
    for i in l:
         r.append(i.lstrip())
    for i in r:
          res = res + i + "\n"    
    return res

if __name__ == "__main__":
    t = """         Python is a high-level, general-purpose programming language. Its design philosophy  
                    emphasizes code readability with the use of significant indentation. Python is dynamically 
                    typed and garbage-collected. It supports multiple programming paradigms, including structured 
                    (particularly procedural), object-oriented and functional programming. It is often described 
                    as a "batteries included" language due to its comprehensive standard library. Guido van Rossum 
                    began working on Python in the late 1980s as a successor to the ABC programming language and 
                    first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000. Python 3.0, 
                    released in 2008, was a major revision not completely backward-compatible with earlier versions. 
                    Python 2.7.18, released in 2020, was the last release of Python 2. Python consistently ranks as 
                    one of the most popular programming languages. """

    
    print(without_indentation(t))