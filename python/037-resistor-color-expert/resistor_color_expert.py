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

TOLERANCE_CODE = {
    'grey': 0.05,
    'violet': 0.1,
    'blue': 0.25,
    'green': 0.5,
    'brown': 1,
    'red': 2,
    'gold': 5,
    'silver': 10
}

def value(colors):
    if len(colors) == 4:
        num0, num1, num2 = (COLOR_CODE[color] for color in colors[:3])
        num3 = TOLERANCE_CODE[colors[-1]]
        return (num0 * 10 + num1) * (10 ** num2), num3
    if len(colors) == 5:
        num0, num1, num2, num3 = (COLOR_CODE[color] for color in colors[:4])
        num4 = TOLERANCE_CODE[colors[-1]]
        return (num0 * 100 + num1 * 10 + num2) * (10 ** num3), num4
    return 0, 0

def prefixing(number):
    if number >= 10 ** 9:
        return 'giga', number / (10 ** 9)
    if number >= 10 ** 6:
        return 'mega', number / (10 ** 6)
    if number >= 10 ** 3:
        return 'kilo', number / (10 ** 3)
    return '', number

def resistor_label(colors):
    prefix, number = prefixing(value(colors)[0])
    if number.is_integer():
        number = int(number)
    tolerance = value(colors)[1]
    if tolerance == 0:
        return f"{number} {prefix}ohms"
    return f"{number} {prefix}ohms ±{tolerance}%"
