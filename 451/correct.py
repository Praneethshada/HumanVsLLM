import re

def remove_whitespaces(text1):
    # removes all whitespace (spaces, tabs, newlines)
    return re.sub(r"\s+", "", text1)
