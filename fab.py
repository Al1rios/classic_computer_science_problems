import pytest


def fatorial(n):
    pr = 1
    for i in range(2, n + 1):
        pr *= i
    return pr



@pytest.mark.parametrize('n, expected', [(-1, 1), (1, 1), (2, 2), (3, 6), (5, 120)])
def test_factorial(n, expected):
    assert expected == fatorial(n)


def test_atri_func():
    fat = fatorial
    assert 120, fat(5)
    assert fat is fatorial

# >>> map(fatorial, range(1, 5))
# >>> list(_) verify range fatorial of 1 - 5
