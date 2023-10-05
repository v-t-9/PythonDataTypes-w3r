# Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def add_tags(t,w):
    text = "<{}>{}</{}>".format(t, w, t)
    return text


if __name__ == "__main__":
    print(add_tags('i', 'Python'))
    print(add_tags('b', 'Python Tutorial'))