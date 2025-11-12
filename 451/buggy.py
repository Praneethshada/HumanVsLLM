import re

def remove_whitespaces(text1):
    # BUG: removes only normal spaces, not tabs/newlines
    return re.sub(r" +", "", text1)
