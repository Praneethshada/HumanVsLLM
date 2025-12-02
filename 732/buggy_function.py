import re

def replace_specialchar(text: str) -> str:
    """
    Replace spaces, commas, and dots with a colon.
    BUG: wrong regex and only replaces first occurrence.
    """
    return re.sub("[ ,.]", ":", text, count=1)
