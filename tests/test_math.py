import pytest

def add(a, b):
    return a + b


def division(a, b):
    if b == 0:
        raise ZeroDivisionError()
    return a / b




def test_division_by_zero_should_raise_error():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)

def test_add():
    assert add(3, 2) == 5
    
    
