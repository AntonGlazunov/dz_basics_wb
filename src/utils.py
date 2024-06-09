import os


def read_file():
    index = open(os.path.join("index.html"), 'r', encoding="utf-8")
    result = index.read()
    return result

