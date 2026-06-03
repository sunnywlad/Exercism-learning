import numbers

def radius(dart_x, dart_y):
    if not all(isinstance(coord, numbers.Number) for coord in (dart_x, dart_y)):
        raise TypeError("Not 2 numbers")
    return dart_x * dart_x + dart_y * dart_y

def score(dart_x, dart_y):
    rad = radius(dart_x, dart_y)
    if rad > 100:
        return 0
    if rad > 25:
        return 1
    if rad > 1:
        return 5
    return 10
