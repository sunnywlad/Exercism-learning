def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if isinstance(number, bool) or not isinstance(number, int) or number < 1:
        raise ValueError('Classification is only possible for positive integers.')
    factor_sum = sum((div for div in range(1, number // 2 + 1) if number % div == 0))
    if number == factor_sum:
        return 'perfect'
    if number < factor_sum:
        return 'abundant'
    return 'deficient'
