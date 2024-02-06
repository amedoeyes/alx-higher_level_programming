#!/usr/bin/python3

"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    """append_after"""
    content = ""
    with open(filename, "r") as fr:
        for line in fr:
            content += line
            if search_string in line:
                content += new_string
    with open(filename, "w") as fw:
        fw.write(content)
