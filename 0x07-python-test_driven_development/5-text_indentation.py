#!/usr/bin/python3

"""Defines text_indentation function"""


def text_indentation(text):
    """Prints text with 2 new lines after
    each of these characters: ., ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    prev = 0
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[prev:i + 1].strip(" "), end="\n\n")
            prev = i + 1
