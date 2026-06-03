import re

def is_isogram(string):
    cleaned = re.sub(r'\s|-', '', string).lower()
    return len(cleaned) == len(set(cleaned))
