from CalculatorObject import Calculator

import pytest

@pytest.fixture
def test_cal():
    return Calculator()
    pass

def test_add_posive(test_cal):
    assert test_cal.add(3,5) == 8

def test_negitive(test_cal):
    assert test_cal.add(-2,-2) == -4

def test_normal_div(test_cal):
    assert test_cal.divide(2,2) == 1

def test_zero_dive(test_cal):
    with pytest.raises(ValueError):
        test_cal.divide(2,0)