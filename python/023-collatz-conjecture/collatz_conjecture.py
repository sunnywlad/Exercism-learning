def steps(number):
    if isinstance(number, int) and number > 0:
        step = 0
        calcul = number
        while calcul != 1:
            if calcul % 2 == 0:
                calcul = calcul // 2
            else:
                calcul = 3 * calcul + 1
            step += 1
        return step
    raise ValueError("Only positive integers are allowed")
