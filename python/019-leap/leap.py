def leap_year(year):
    """
    is the year divisible by 4 ?
    """
    a = ((year % 4) == 0)
    """
    is the year divisible by 100 ?
    """
    b = ((year % 100) == 0)
    """
    is the year divisible by 400 ?
    """
    c = ((year % 400) == 0)
    """
    calculating the boolean state
    """
    return a and ( not b or c )
