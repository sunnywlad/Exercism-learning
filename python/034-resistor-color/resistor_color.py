COLOR_CODE = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

def color_code(color):
    if not isinstance(color, str):
        raise TypeError('You must enter a string')
    if color not in COLOR_CODE:
        raise ValueError('This is not a coded color')
    return COLOR_CODE[color]


def colors():
    return list(COLOR_CODE)
