import pytest
import sys

sys.path.append(".")

from practice.error_handling import safe_division 





def test_divide_normal():
    assert safe_division(10, 2) == 5



def test_type_error():
    with pytest.raises(TypeError):
        safe_division("a", 1)


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        safe_division(5, 0)

def test_float_division():
    assert safe_division(7.5, 2.5) == 3.0
