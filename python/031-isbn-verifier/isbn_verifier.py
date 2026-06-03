import re

def formating(isbn):
    raw = re.sub(r'\s|-', '', isbn)
    if (len(raw) == 10
        and all(digit.isdigit() for digit in raw[0:9])
        and (raw[9] == 'X' or raw[9].isdigit())):
        return raw
    return False

def values(isbn):
    raw = formating(isbn)
    if raw:
        list_values = list((10 -  index) * int(digit) for index, digit in enumerate(raw[0:9]))
        if raw[9] == 'X':
            list_values += [10]
        else:
            list_values += [int(raw[9])]
        return list_values
    return False

def is_valid(isbn):
    list_values = values(isbn)
    if list_values:
        return sum(list_values) % 11 == 0
    return False
