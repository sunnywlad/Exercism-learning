def is_armstrong_number(number):
    stringify = str(number)
    length = len(stringify)
    return number == sum (int(digit) ** length for digit in stringify)
