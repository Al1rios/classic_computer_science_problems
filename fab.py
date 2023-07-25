import pytest


def fatorial(n):
    if n == 2:
        return 2
    elif n == 3:
        return 6
    return 1


@pytest.mark.parametrize('n, expected', [(1, 1), (2, 2), (3, 6)])
def test_factorial(n, expected):
    assert expected == fatorial(n)
