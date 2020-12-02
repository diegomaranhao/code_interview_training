def fizz_buzz(n: int):
    """
    >>> fizz_buzz(5)
    5
    >>> fizz_buzz(2)
    'fizz'
    >>> fizz_buzz(3)
    'buzz'
    >>> fizz_buzz(6)
    'fizzbuzz'


    :param n:
    :return:
    """
    if n % 2 == 0 and n % 3 == 0:
        return "fizzbuzz"
    elif n % 2 == 0:
        return "fizz"
    elif n % 3 == 0:
        return "buzz"
    else:
        return n
