from fizz_buzz import fizz_buzz


def test_divisible_by_two():
    assert fizz_buzz(2) == 'fizz'


def test_divisible_by_three():
    assert fizz_buzz(3) == 'buzz'


def test_divisible_by_two_and_three():
    assert fizz_buzz(6) == 'fizzbuzz'

def test_not_divisible():
    assert fizz_buzz(5) == 5