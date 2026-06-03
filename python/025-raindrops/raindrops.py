def is_3_div(number):
    return (number % 3) == 0
def is_5_div(number):
    return (number % 5) == 0
def is_7_div(number):
    return (number % 7) == 0

def convert(number):
    sound = ""
    if is_3_div(number):
        sound += "Pling"
    if is_5_div(number):
        sound += "Plang"
    if is_7_div(number):
        sound += "Plong"
    if not sound    :
        return str(number)
    return sound
