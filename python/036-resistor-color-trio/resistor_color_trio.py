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
    return (COLOR_CODE[colors[0]] * 10 + COLOR_CODE[colors[1]]) * (10 ** COLOR_CODE[colors[2]])

def prefixing(number):
    if number >= 10 ** 9:
        return 'giga', number // (10 ** 9)
    if number >= 10 ** 6:
        return 'mega', number // (10 ** 6)
    if number >= 10 ** 3:
        return 'kilo', number // (10 ** 3)
    return '', number

def label(colors):
    if not isinstance(colors, list):
        raise TypeError('Enter the colors in an array')
    if len(colors) <= 2:
        raise ValueError('Enter three colors')
    if ((colors[0] not in COLOR_CODE)
            or (colors[1] not in COLOR_CODE)
            or (colors[2] not in COLOR_CODE)):
        raise ValueError('At least one of the colors entered isn\'t in the code')
    prefix, number = prefixing(value(colors))
    return f"{number} {prefix}ohms"
