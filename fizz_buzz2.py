def fizz_buzz(n:int):
    """
    >>> fizz_buzz(2)
    1
    fizz
    >>> fizz_buzz(3)
    1
    fizz
    buzz
    >>> fizz_buzz(5)
    1
    fizz
    buzz
    fizz
    5
    >>> fizz_buzz(6)
    1
    fizz
    buzz
    fizz
    5
    fizzbuzz

    
    :param n:
    :return:
    """
    for number in range(1, n+1):
        if number % 2 == 0 and number % 3 == 0:
            print('fizzbuzz')
        elif number % 2 == 0:
            print('fizz')
        elif number % 3 == 0:
            print('buzz')
        else:
            print(number)

fizz_buzz(5)