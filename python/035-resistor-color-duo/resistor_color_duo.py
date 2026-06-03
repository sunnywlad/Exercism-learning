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

def value(colors):
    if not isinstance(colors, list):
        raise TypeError('Enter the colors in an array')
    if len(colors) <= 1:
        raise ValueError('Enter two colors')
    if (colors[0] not in COLOR_CODE) or (colors[1] not in COLOR_CODE):
        raise ValueError('At least one of the colors entered isn\'t in the code')
    return COLOR_CODE[colors[0]] * 10 + COLOR_CODE[colors[1]]
