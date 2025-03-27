import re

"""
Creates a dict with all words in a given text and num of letters in it
"""


# using regex makes parsing much simpler, they are used in compiler parsing like yylex so why not use them here.
def long_cat_is_long(text):
    return {word: len(word) for word in re.findall(r'\b[a-zA-Z]+\b', text)}


def main():
    print(long_cat_is_long("Bla bla bla tralala 123"))


if __name__ == "__main__":
    main()
